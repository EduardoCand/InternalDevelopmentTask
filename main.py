import argparse
import os
import shutil
import hashlib
import time


# Compute the hash of a file.
def hash_file(file_path):
    with open(file_path, 'rb') as f:
        hasher = hashlib.md5()
        while True:
            buf = f.read(65536)
            if not buf:
                break
            hasher.update(buf)
        return hasher.hexdigest()


# Synchronize the source folder with the replica folder.
def sync_folders(source_dir, replica_dir, log_file):
    # Create the replica directory if it doesn't exist
    os.makedirs(replica_dir, exist_ok=True)

    # Synchronize files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_dir, os.path.relpath(source_file_path, source_dir))
            replica_file_dir = os.path.dirname(replica_file_path)

            # Create the directory in the replica folder if it doesn't exist
            os.makedirs(replica_file_dir, exist_ok=True)

            # If the file doesn't exist in the replica folder, copy it over
            if not os.path.exists(replica_file_path):
                shutil.copyfile(source_file_path, replica_file_path)
                log_file.write(f'Copied {source_file_path} to {replica_file_path}\n')
                print(f'Copied {source_file_path} to {replica_file_path}')
            else:
                # If the file exists in both folders, compare their hashes
                source_file_hash = hash_file(source_file_path)
                replica_file_hash = hash_file(replica_file_path)

                if source_file_hash != replica_file_hash:
                    # If the hashes don't match, copy the source file to the replica folder
                    shutil.copyfile(source_file_path, replica_file_path)
                    log_file.write(f'Updated {replica_file_path} to match {source_file_path}\n')
                    print(f'Updated {replica_file_path} to match {source_file_path}')

    # Remove files in the replica directory that don't exist in the source directory
    for root, dirs, files in os.walk(replica_dir):
        for file in files:
            replica_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_dir, os.path.relpath(replica_file_path, replica_dir))

            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                log_file.write(f'Removed {replica_file_path}\n')
                print(f'Removed {replica_file_path}')


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Synchronize two folders.')
    parser.add_argument('source_dir', help='path to the source folder')
    parser.add_argument('replica_dir', help='path to the replica folder')
    parser.add_argument('interval', type=int, help='synchronization interval in seconds')
    parser.add_argument('log_file', help='path to the log file')
    args = parser.parse_args()

    # Open the log file
    with open(args.log_file, 'a') as log_file:
        while True:
            sync_folders(args.source_dir, args.replica_dir, log_file)
            time.sleep(args.interval)
