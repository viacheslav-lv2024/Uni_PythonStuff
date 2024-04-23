import os

def chunks(path: str, size: int, **kwargs):
    if not os.path.isfile(path) or size < 1:
        raise ValueError
    for arg in kwargs:
        with open(path, **kwargs) as f:
            while True:
                chunk = f.read(size)
                if not chunk:
                    break
                yield chunk
