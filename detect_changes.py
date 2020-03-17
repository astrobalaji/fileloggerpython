import filecmp
import os
from datetime import datetime
from shutil import copytree

## commit changes from live_files to file_safe
def file_actions(ans):
    if ans == 'y':
        os.system('cp live_files/* file_safe/')
    elif ans == 'n':
        ans1 = input('Would you like to revert these changes (y/n)').lower()
        revert_actions(ans1)
    else:
        ans2 = input('Wrong Input!!! Please enter only y or n').lower()
        file_actions(ans2)

## revert all the modifications on live_files and restore the files from file_safe
def revert_actions(ans):
    if ans == 'y':
        os.system('rm live_files/*')
        os.system('cp file_safe/* live_files/')
    elif ans == 'n':
        print('Live files are kept intact. The old changes will still be visible in the next run.')
    else:
        ans2 = input('Wrong Input!!! Please enter only y or n').lower()
        revert_actions(ans2)


live_files = os.listdir('live_files/')
safe_files = os.listdir('file_safe/')

## Detect newly created files
new_files = list(set(live_files).difference(safe_files))

## Detected deleted files
deleted_files = list(set(safe_files).difference(live_files))

if len(new_files) != 0:
    print('Files created:')

for f in new_files:
    ctime = datetime.fromtimestamp(os.path.getctime('live_files/'+f)).strftime('%d/%m/%Y %H:%M:%S')
    print(f+' created on: '+ctime)

if len(deleted_files) != 0:
    print('Files deleted:\n'+'\n'.join(deleted_files))

rest_files = list(set(live_files).intersection(safe_files))


### Checking for file modifications
print('File Modifications:')
files_modded = False

for f in rest_files:
    if not filecmp.cmp('live_files/'+f, 'file_safe/'+f):
        files_modded = True
        live_f = open('live_files/'+f, 'r')
        save_f = open('file_safe/'+f, 'r')
        live_content = live_f.readlines()
        save_content = save_f.readlines()
        new_lines = list(set(live_content).difference(save_content))
        old_lines = list(set(save_content).difference(live_content))
        ctime = datetime.fromtimestamp(os.path.getctime('file_safe/'+f)).strftime('%d/%m/%Y %H:%M:%S')
        mtime = datetime.fromtimestamp(os.path.getmtime('live_files/'+f)).strftime('%d/%m/%Y %H:%M:%S')
        print('filename: '+f, 'created on: '+ctime, 'modified on: '+mtime, '\n Modifications:')
        print('\n'.join(new_lines))
        print('Old Lines:')
        print('\n'.join(old_lines))

if not files_modded:
    print('No Changes detected')


## Asking user for commit or revert changes
if files_modded or (len(new_files) != 0) or (len(deleted_files) != 0):
    ans = input('Would you like to commit these changes (y/n)').lower()
    file_actions(ans)
