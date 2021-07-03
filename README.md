# Medals-AutoCleanup
Saving this on git for me to have easy access to -- very hacky solution. 

Cleans up old clips from medals, with configurable max-time retention. Default is 7 days. You will have to create a windows task scheduler to run the .vbs script at a time interval you're comfortable with.

REQUIRES that medal be restarted for old clips to disappear from its database. I am not going to handle that, since that will inevitably cause issues if it auto-restarts when the script runs.

## Install
1. Copy the three files from this repository.
2. Extract them to a location. Any location is fine, so long as they all exist in the same folder.
3. Edit MedalsRM.bat according to the configuration section below. All three paths **have to be filled out**.
4. Also edit MedalsRM.vbs and change the file location to point to the batch file.
  - For example:
    - If my MedalsRM.bat file exists in "C:/ProgramFiles/CustomScript/MedalsRM.bat" , then use that full path in the first argument of the .Run command within the VBS file, **quotes included**.
6. Add a task in Task Scheduler that will run the **_VBS_** script (preferably once a day, or through any other event that fits your needs).
7. Complete.

## Configuration

There are four different variables to configure in MedalsRM.bat. It is required.


| Variable  | Description | Default  |  Required  |
| ------------- | ------------- | ------------- |------------- |
| pathtoclips  | Path to the clips saved by Medal. Will usually be in your Videos folder, unless configured differently  | None  | Yes  |
| pathtoscripts  | The path to the folder where your scripts are located  | None  | Yes  |
| pathtoJSON  | Path to the JSON database of the medals clips. This will usually be in: C:\Users\yourusername\AppData\Roaming\Medal\store\clips.json | None  | Yes  |
| timetodelete  | Delete files older than this number, in days | 7  |  No  |


There is one thing to configure in MedalsRM.bat. It is required.

CreateObject("Wscript.Shell").Run "**Replace everything between these quotes with the location to your bat file**", 0, False
