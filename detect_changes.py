import filecmp
import os
from datetime import datetime


live_files = os.listdir('live_files/')
safe_files = os.listdir('file_safe/')

new_files = list(set(live_files).difference(safe_files))
deleted_files = list(set(safe_files).difference(live_files))

if len(new_files) != 0:
    print('Files created:')

for f in new_files:
    ctime = datetime.fromtimestamp(os.path.getctime('live_files/'+f)).strftime('%d/%m/%Y %H:%M:%S')
    print(f+' created on: '+ctime)

print('Files deleted:\n'+'\n'.join(deleted_files))

rest_files = list(set(live_files).intersection(safe_files))

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
