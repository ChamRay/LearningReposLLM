from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent 

RAW_DATA_PATH = ROOT_DIR / 'data' / 'raw'
PROCESSED_DIR_PATH = ROOT_DIR / 'data' / 'processed'

LOGS_DRI = ROOT_DIR / 'logs'
MODELS_DIR = ROOT_DIR / 'models' 

SEQ_LEN = 5