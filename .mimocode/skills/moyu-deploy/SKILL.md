---
name: moyu-deploy
description: Deploy moyu-platform services to remote K8s cluster via SSH. Handles middleware YAML rendering, SCP upload, kubectl apply, rollout wait, and pod health verification. Use when user asks to deploy, update, or verify moyu services on the remote server.
---

# moyu-deploy

Deploy moyu-platform components to the remote K8s cluster. Covers middleware (MySQL, Redis, Nacos, RocketMQ) and application services (admin, user, order, face, miniapp).

## Prerequisites

- `sshpass` installed locally (`brew install sshpass`)
- Remote server access: `root@47.98.112.193` (password: `RayCham123@`)
- Alternative server: `root@112.124.32.106` (password: `RayCham123@`)
- `render.sh` and config YAMLs in `k8s-deploy/` directory

## Workflow

### 1. Middleware Deployment (first-time or update)

```bash
cd /Users/mac/testspace/moyu-project/k8s-deploy

# Render templates
bash render.sh 2>&1 | tail -5

# Upload and apply each middleware YAML in order
for f in .rendered/middleware-standalone/0{0,1,2,3,4,5,6}*.yaml; do
  echo "Applying: $(basename $f)"
  sshpass -p 'RayCham123@' scp -o StrictHostKeyChecking=no "$f" root@47.98.112.193:/tmp/
  sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@47.98.112.193 \
    "kubectl apply -f /tmp/$(basename $f)"
done
```

Order matters: 00-namespace → 01-mysql → 02-redis → 03-nacos → 04-rocketmq → 05-emqx → 06-grafana

### 2. Application Deployment via Jenkins

```bash
# Trigger Jenkins build with parameters
sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@112.124.32.106 \
  'CRUMB=$(curl -s -c /tmp/j -u admin:RayCham123@ http://localhost:30088/crumbIssuer/api/json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d[\"crumb\"])") && \
   curl -s -u admin:RayCham123@ -b /tmp/j -X POST "http://localhost:30088/job/moyu-platform/buildWithParameters" \
   -H "Jenkins-Crumb:$CRUMB" -d "BRANCH=main"'
```

### 3. Verify Deployment

```bash
# Wait for build (3 min), then check result
sleep 180 && sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@112.124.32.106 \
  'curl -s -u admin:RayCham123@ http://localhost:30088/job/moyu-platform/lastBuild/api/json | \
   python3 -c "import sys,json; d=json.load(sys.stdin); print(d[\"number\"], d[\"building\"], d.get(\"result\",\"in progress\"))"'

# Check pod status
sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@47.98.112.193 \
  "kubectl get pods -n middleware && echo '---' && kubectl get pods -n moyu"
```

### 4. Troubleshooting

```bash
# Check pod logs
sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@47.98.112.193 \
  "kubectl logs -n <namespace> <pod-name> --tail=30"

# Check events
sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@47.98.112.193 \
  "kubectl -n <namespace> get events --sort-by='.lastTimestamp' | tail -15"

# Restart a deployment
sshpass -p 'RayCham123@' ssh -o StrictHostKeyChecking=no root@47.98.112.193 \
  "kubectl rollout restart deployment/<name> -n <namespace>"
```

## Key Paths

- K8s deploy configs: `/Users/mac/testspace/moyu-project/k8s-deploy/`
- Rendered YAMLs: `k8s-deploy/.rendered/`
- Jenkins URL: `http://112.124.32.106:30088`
- Jenkins creds: `admin` / `RayCham123@` (crumb API required for POST)
- Jenkins initial password (K8s pod): `df002304dbd84b3f8ff0c4f5c25e2663`

## Lessons Learned (from session history)

- Always render before apply — `render.sh` generates `.rendered/` from templates + `config.yaml`
- Middleware deploy order matters (MySQL before Nacos, Redis before RocketMQ)
- Jenkins build takes ~3 min; poll `lastBuild/api/json` for result
- Jenkins requires crumb token for any POST request (CSRF protection)
- Ceph/Rook operator logs are the first place to check for storage issues
- `kubectl rollout status` with `--timeout` prevents hanging on failed rollouts
