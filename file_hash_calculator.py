import hashlib
import os

def calculate_hash(filepath, algorithm='sha256'):
    """
    Calculate hash of a file using specified algorithm
    
    Args:
        filepath: Path to the file
        algorithm: Hash algorithm (md5, sha1, sha256)
    
    Returns:
        Hex digest of the hash
    """
    
    # Select hash algorithm
    if algorithm == 'md5':
        hasher = hashlib.md5()
    elif algorithm == 'sha1':
        hasher = hashlib.sha1()
    elif algorithm == 'sha256':
        hasher = hashlib.sha256()
    else:
        return None
    
    # Open file in binary read mode
    try:
        with open(filepath, 'rb') as f:
            # Read file in chunks to handle large files efficiently
            while chunk := f.read(8192):
                hasher.update(chunk)
        
        return hasher.hexdigest()
    
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """Main function to run the hash calculator"""
    
    print("=" * 50)
    print("File Hash Calculator v1.0")
    print("=" * 50)
    print()
    
    # Get file path from user
    filepath = input("Enter file path: ").strip()
    
    # Remove quotes if user copied path with quotes
    filepath = filepath.strip('"').strip("'")
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return
    
    # Get file size
    file_size = os.path.getsize(filepath)
    print(f"\nFile: {os.path.basename(filepath)}")
    print(f"Size: {file_size:,} bytes")
    print()
    
    # Calculate hashes
    print("Calculating hashes...")
    print("-" * 50)
    
    algorithms = ['md5', 'sha1', 'sha256']
    
    for algo in algorithms:
        hash_value = calculate_hash(filepath, algo)
        if hash_value:
            print(f"{algo.upper():8} : {hash_value}")
        else:
            print(f"{algo.upper():8} : Error calculating hash")
    
    print("-" * 50)
    print("\nDone!")


if __name__ == "__main__":
    main()