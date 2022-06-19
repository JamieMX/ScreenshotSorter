This is a basic program I've created to automatically sort my very disorganised
screenshot folder. All of the screenshots have a standard name incorporating the
date they were created. I want to use this standardised name to sort them into 
subfolders (year and month)

I'll use python's OS module and its os.walk() function which traverses a directory
I will have to extract the filename of each of the files looped through and perform
conditional operations based on the filename.

Example filename:
ffxiv_01012022_010807_986

The first part ffxiv_ is irrelevant
The second part 01012022 is the date (i.e. 01/01/2022)
Not sure what the third part is supposed to be

What makes them hard to sort manually is W10's default file sorting will put a
screenshot from for example the 4th of June next to one from the 4th of December
The formatting of files means the date string is always the same length which
should make things easier

Pseudocode:

Create directory 2020
Create directory 2021
Create directory 2022
n = 1
while n = <13:
    create directory(n) in 2020/2021/2022
    n++

