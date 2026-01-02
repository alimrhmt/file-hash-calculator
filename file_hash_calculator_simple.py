import hashlib
import os

# Get file path from user
file_path = input("Enter full file path: ").strip()

# Check if file exists
if not os.path.isfile(file_path):
    print("❌ File not found. Please check the path.")
    exit()

try:
    with open(file_path, 'rb') as file:
        content = file.read()

    md5_hash = hashlib.md5(content).hexdigest()
    sha1_hash = hashlib.sha1(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    print("\n✅ File Hashes:")
    print("MD5    :", md5_hash)
    print("SHA1   :", sha1_hash)
    print("SHA256 :", sha256_hash)

except Exception as e:
    print("❌ Error reading file:", e)
