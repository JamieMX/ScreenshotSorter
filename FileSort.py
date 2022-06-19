import os
import shutil
from datetime import date, datetime
from DirectorySetup import directory_setup

#filedir = "D:\\Users\\Jamie\\Pictures\\Games\\FFXIV"
#directory_setup(filedir)
month_dict = {
    "01" : "01 January",
    "02" : "02 February",
    "03" : "03 March",
    "04" : "04 April",
    "05" : "05 May",
    "06" : "06 June",
    "07" : "07 July",
    "08" : "08 August",
    "09" : "09 September",
    "10" : "10 October",
    "11" : "11 November",
    "12" : "12 December"
}

def file_sort(screenshot_directory):
    screenshots = os.listdir(screenshot_directory)
    files_copied = 0
    for file in screenshots:
            filepath = os.path.join(screenshot_directory, file)
            #print(filepath)
            if os.path.isfile(filepath) and "ffxiv" in file:
                year_slice = file[10:14]
                month_slice = file[8:10]
                month = str(month_dict.get(month_slice))
                destination_year = os.path.join(screenshot_directory, year_slice)
                destination_month = os.path.join(destination_year, month)
                destination_full = os.path.join(destination_month, file)
                #print(file)
                #print(destination_full)
                shutil.copyfile(filepath, destination_full)
                os.remove(filepath)
                files_copied += 1
    current_time = datetime.now()
    timestamp = current_time.strftime("%m/%d/%Y, %H:%M:%S")
    output_path = os.path.join(screenshot_directory, "sort_results.txt")
    with open(output_path, "w") as results:
        results.write("Total files copied: " + str(files_copied) + "\n"
                        "Files sorted on: " + timestamp)
