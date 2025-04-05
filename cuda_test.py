# run with prime-run python cuda_test.py
import torch

def test_cuda():
    assert torch.cuda.is_available()
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Device count: {torch.cuda.device_count()}")
        print(f"Current device: {torch.cuda.current_device()}")
        print(f"Device name: {torch.cuda.get_device_name(0)}")
        # Create a tensor on GPU
        x = torch.zeros(3, 3, device='cuda')
        print(f"Tensor created on: {x.device}")

if __name__ == "__main__":
    test_cuda()
