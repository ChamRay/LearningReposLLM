import torch
import torch_directml
from prompt_toolkit.utils import to_int


def get_device(device_index: int = 0):
    """
    Get the appropriate device (GPU or CPU) for PyTorch.
    
    Args:
        device_index (int): The index of the GPU device to use. Default is 0.
    
    Returns:
        torch.device: The device to use for PyTorch operations
    
    Raises:
        RuntimeError: If the specified device index is not available
    """
    # Check for CUDA (NVIDIA) GPU
    if torch.cuda.is_available():
        if device_index >= torch.cuda.device_count():
            raise RuntimeError(f"CUDA device index {device_index} is not available. Only {torch.cuda.device_count()} devices are available.")
        device = torch.device(f"cuda:{device_index}")
        print(f"Using NVIDIA GPU: {torch.cuda.get_device_name(device_index)}")
        return device
    
    # Check for MPS (Apple Silicon) GPU
    if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        if device_index > 0:
            print(f"Warning: MPS only supports device index 0, but {device_index} was requested. Using index 0 instead.")
        device = torch.device("mps")
        print("Using Apple M1/M2 GPU")
        return device
    
    # Check for ROCm (AMD) GPU
    if torch_directml.is_available():
        if device_index >= torch_directml.device_count():
            raise RuntimeError(f"ROCm device index {device_index} is not available. Only {torch.cuda.device_count()} devices are available.")
        device = torch_directml.device(device_index)
        print(f"Using AMD GPU: {torch_directml.device_name(device_index)}")
        return device



    # Fallback to CPU
    if device_index > 0:
        print(f"Warning: CPU only supports device index 0, but {device_index} was requested. Using index 0 instead.")
    device = torch.device("cpu")
    print("Using CPU")
    return device

if __name__ == "__main__":
    # Test the function
    try:
        device = get_device(1)
        print(f"Selected device: {device}")

        # Test with different device indices
        for idx in range(2):
            try:
                device = get_device(idx)
                print(f"Selected device with index {idx}: {device}")
            except RuntimeError as e:
                print(f"Error when trying to use device index {idx}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}") 