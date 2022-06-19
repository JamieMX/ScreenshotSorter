import os
import string
from datetime import date, datetime

#My FFXIV screenshot directory. Double slashes used to avoid unicode errors
dir = "C:\\Users\\Jamie\\Desktop\\PracticeFolder"

def directory_setup(screenshot_directory):
#Numbers mean the folders will be chronological when alphabetised in windows
    month_dict = {
        1 : "01 January",
        2 : "02 February",
        3 : "03 March",
        4: "04 April",
        5: "05 May",
        6: "06 June",
        7: "07 July",
        8: "08 August",
        9: "09 September",
        10: "10 October",
        11: "11 November",
        12: "12 December"
    }

    #Setup 3 subdirectories for 2020, 21 and 22
    current_time = datetime.now()
    #Obtain only the current year from current_time then conver to int
    current_year = int(current_time.strftime("%Y"))
    #Create folders for the current and past 2 years
    y = current_year - 2
    month = 1
    #Create a folder for the past 2 years and the current year
    while y < (current_year + 1):
        year_string = str(y)
        year_path = os.path.join(screenshot_directory, year_string)
        os.mkdir(year_path)
        while month < 13:
            year_folder = "\\"+str(y)
            month_dir = month_dict.get(month)
            path = os.path.join(year_path, month_dir)
            os.mkdir(path)
            month = month + 1
        y = y  +1
        month = 1