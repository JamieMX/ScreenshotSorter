Basic python script I wrote to sort a very disorganised FFXIV screenshot folder using a standard naming format.
Creates directories for 2020, 2021 and 2022, as well as subfolders in all 3 for each month.
Loops through every file in the folder and copies it to an appropriate directory based on the file name, then deletes the original.
Creates a text file with a count of how many files were copied and a timestamp in the original directory.
-------------------------------------------------------------------------------------------------------------------
Instructions:
1) Change the dir variable in ScreenshotSorter.py to the filepath of your screenshot folder 
2) Run the script
-------------------------------------------------------------------------------------------------------------------
Notes:
-It will NOT function if you already have subdirectories based on year (to be fixed)
-There is a test folder with example files to prove functionality. To test, ensure the dir variable in ScreenshotSorter corresponds to the location of the testfiles.
-Double slashes (\\) are used throughout to avoid windows related unicode errors
-I just made this to practice coding in python
-------------------------------------------------------------------------------------------------------------------
Plans/Things to be implement:
-An actual user interface
-A "safe mode" that doesn't remove files from the original directories
-Automating the year directory creation and allow user input to control this
-Generally more user control: "what years/dates do you want to sort for"
-Sorting without directory setup: i.e., allowing user to sort multiple times as they repopulate root directory.
-Details from sort ("X files copied to folder 2021, Y to 2022" etc.)
