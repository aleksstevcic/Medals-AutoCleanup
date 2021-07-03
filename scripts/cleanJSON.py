import sys
import json
from pathlib import Path

#if not running from the shell, then exit
if not __name__ == "__main__":
    print('invalid syntax/not running in shell. exiting')
    quit()

#set path to the first arg
path = sys.argv[1]
path = path.replace('\\', '/')

#open file as a string
medalClipsJSON = open(path, 'r')

#parse into json (as a dictionary)
JSONData = json.load(medalClipsJSON)

#close file
medalClipsJSON.close()

#list of entries to delete, will be populated with GUIDs of empty entries
listToDelete = []

#find entries that have no corresponding file
for clipname in JSONData:
    clip = JSONData[clipname]
    if (not Path(clip['FilePath']).is_file()) and (clip['Status'] == 'local'):
        listToDelete.append(clipname)

#go through queue of missing files and delete from list
for clipname in listToDelete:
    #print(clipname)
    del JSONData[clipname]

medalClipsJSON = open(path, 'w')

#clear file then write to file with dump
medalClipsJSON.truncate(0)
json.dump(JSONData, medalClipsJSON, indent = 2)

#close file
medalClipsJSON.close()

#done
#print('done')