# fileloggerpython
File logger for Python


## file and folder description:

* **file_safe** : Folder with all reviewed files. Files will be stored here only when the changes reported are committed.
* **live_files** : Folder with all the files which are modified, created or deleted. This is where all the action takes place.
* **create_dat_files.py**: Python script to create random text files with lorem ipsum texts in it.
* **detect_changes.py**: Main script which will report all changes.

## Requirements

* Preferred OS: Linux/ Mac
* Python 3 (>=3.4)

## To execute the script

Files can be modified in live_files folder and the file_safe contains the safe repo of the files which will only be modified if the files are commited by the detect_changes.py script

```bash
python detect_changes.py
```
