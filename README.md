# InternalDevelopmentTask
Internal Development in QA task for Veeam company

This script synchronizes the contents of two folders by copying files from the source folder to the replica folder, and updating files in the replica folder that have changed in the source folder. It also removes files from the replica folder that no longer exist in the source folder.

# Installation
To use this script, you must have Python 3 installed on your system. You can download it from the official website: https://www.python.org/downloads/

The script also uses the following Python modules, which can be installed using pip:
<br>**argparse**: for parsing command line arguments
<br>**hashlib**: for computing file hashes
<br>**shutil**: for copying and deleting files
<br>**time**: for implementing synchronization intervals

To install these modules, run the following command in your terminal:
<br> **pip install argparse hashlib shutil time**

# Usage
To run the script, open a terminal and navigate to the directory containing the script file. Then, enter the following command:
<br> **python file_sync.py <source_dir> <replica_dir> <time_interval> <log_file>**
  
### Where:
**<source_dir>** is the path to the source folder
<br>**<replica_dir>** is the path to the replica folder
<br>**<time_interval>** is the synchronization interval in seconds (e.g. 60 for one minute)
<br>**<log_file>** is the path to the log file

The script will run continuously, synchronizing the two folders at the specified interval. The log file will contain a record of all file operations performed by the script.
