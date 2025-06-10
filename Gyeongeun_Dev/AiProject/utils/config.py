import os

def read_api_key(relative_path: str) -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, relative_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"API 키 파일이 존재하지 않습니다: {full_path}")
    
    with open(full_path, "r") as f:
        return f.read().strip()

def read_api_key_path(relative_path: str) -> str:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, relative_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"API 키 파일이 존재하지 않습니다: {full_path}")
    
    return full_path
