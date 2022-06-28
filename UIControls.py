from DirectorySetup import directory_setup
from FileSort import file_sort 
from FileSort import safe_sort

title_text = "Screenshot Sorter"
subtitle_text = "A basic program that sorts screenshots from FFXIV into folders\
based on year and date. "
instructions_text = "Enter the directory where your screenshots are stored \
using two backslashes to separate directories, then click submit.\nSafe sort \
does not delete files. Normal sort will remove files as it copies them to new \
folders. "
directory_default = "C:\\Users\\You\\Games\\FFXIV\\Screenshots"
def quit_program(event, window):
    """Close when button is clicked is pressed"""
    window.destroy()
def submit_directory(event, text_entry):
    """Runs the program using the address in the directory entry field"""
    directory_address = text_entry.get()
    #print(directory_address)
    directory_setup(directory_address)
    file_sort(directory_address)
def submit_safe(event, text_entry):
    """Runs the program using the address in the directory entry field"""
    directory_address = text_entry.get()
    directory_setup(directory_address)
    safe_sort(directory_address)