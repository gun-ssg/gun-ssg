from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def load_public_key_from_pem(file_path):
    # Đọc file PEM chứa khóa công khai
    with open(file_path, 'rb') as pem_file:
        pem_data = pem_file.read()

    # Tải khóa công khai từ file PEM
    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())

    # Lấy các tham số n và e từ khóa công khai
    if hasattr(public_key, 'public_numbers'):
        public_numbers = public_key.public_numbers()
        n = public_numbers.n
        e = public_numbers.e
        return n, e
    else:
        raise ValueError("File không chứa khóa công khai hợp lệ.")

# Đường dẫn file PEM
pem_file_path = "public_key.pem"

# Chuyển đổi
try:
    n, e = load_public_key_from_pem(pem_file_path)
    print(f"Modulus (n): {n}")
    print(f"Exponent (e): {e}")
except Exception as ex:
    print(f"Lỗi: {ex}")
