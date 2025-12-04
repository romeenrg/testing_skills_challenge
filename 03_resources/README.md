# CHALLENGE

### Overview
Overall, the program was easy to understand and use. With the use of single files, the functionality worked the way it was intended to with all the scenarios carrying out as expected.
However, with the addition of other valid files - problems arose.

### Feedback
- There was no output to let the user know that files had been created in finals folder
- Following on from above, there was no output for the user when NO files had been created in the finals folder

### Bugs 

Severity: 1 (high) - 5 (trivial)
Priority: 1 (high) - 3 (low)

#### 1. Removal of punctuation when moving to finals directory

*Description of bug*
When the user has a filename (surname) that contains punctuation such as dashes or apostrophes, when it gets added to the finals directory - the punctuation is removed. This happens whether the file is present in just originals, just updates or both and it can be updated into the finals folder.

*Observed*
The filename has the punctuation removed 

*Expected*
The filename should be kept the same and consitent throughout

*Steps to reproduce*
1. Create a valid file in originals folder with the filename "O'Neil-Smith"
2. Create an allowlist file with just the name "O'Neil-Smith" on line 1
3. (OPTIONAL) Create a valid file in updates folder with the filename "O'Neil-Smith"
4. Run the program
5. Observe the filename of the file in the finals folder

*Severity* - 2

*Priority* - 1

*Media*


#### 2. Hidden files in original or updates folder stop program running

*Description of bug*
When there is a hidden file (.___ files), the program still runs through them and causes an error code to occur.

*Observed*
Error code produced 
> Traceback (most recent call last):
>File "/Users/romeenrg/Projects/Testing_skills/challenge/03_resources/document_updater.py", ??line 59, in <module>
>    contents = f.readlines()
>               ^^^^^^^^^^^^^
>  File "<frozen codecs>", line 322, in decode
> UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 558: invalid start byte

*Expected*
A more userfriendly error message or for the program to ignore hidden files


*Steps to reproduce*
1. Create a valid file in originals 
2. Delete that file using "Finder" application (on Mac) - this creates the .DS file which causes the error
3. Create a new valid file in originals
4. Create a valid allow list with that filename present
4. Run the program

*Severity* - 1

*Priority* - 2

*Media*


#### 3. Original file merges with Update file for Finals file when not listed in droplist

*Description of bug*
When there is an original file version and an updated file version, they should not overwrite each other or effect each other. However, when the filename is NOT present in a droplist file, the original file (if it is longer on lines 4/5) will have its content added onto the updated file.


*Observed*
e.g
> droplist = hello

>original
>Shirley Smith
>>Studio 05
>Wright forks and Extra 
>Port Antony
>•N40 6GT

>updated
>Shirley Smith
>Studio 88A
>Campbell circle
>Waynehaven


>finals 
>Shirley Smith
>Studio 88A
>Campbell circled Extra (d extra is added)
>Waynehaveny
>N40 6GT (this line is added)

*Expected*

Should be just the updated file
>Shirley Smith
>Studio 88A
>Campbell circle
>Waynehaven


*Steps to reproduce*

*Severity* - 1

*Priority* - 1


*Media*


#### 4. Files in original & allowlist do not make it to the final folder (when an updated file is present in allowlist)

*Description of bug*
An original file that is also in the allow list (meaning it should be present in the finals folder when program runs) does not appear in the finals folder WHEN an updated file is present in both originals and allowlist. This means that files are not showing up in finals when they are supposed to.

*Observed*
To illustrate it easier, the folders can be shown section by section.

> originals folder - 5 
> Baker
> Hardy
> Jenkins
> Jones
> Riley

> allowlist - 
> Baker
> Hardy
> Jones


> updates folder - 2
> Jenkins
> Jones
> (Jenkins)
*note that Jones is present in both originals and allowlist (can interchange with Jenkins or even include both and observed results are the same)*

RESULTS IN FINALS 
> finals folder 
> Jenkins
> Jones

only the updates files are present


*Expected*

> originals folder - 5 
> Baker
> Hardy
> Jenkins
> Jones
> Riley

> allowlist - 
> Baker
> Hardy
> Jones


RESULTS IN FINALS 
> finals folder 
> Jenkins
> Jones
> Baker 
*Baker's original file should be present as it is in the allowlist*


*Steps to reproduce*
1. Create 5 valid files in Originals folder
2. Add 3 of those valid files into allow list
3. Create 2 updated files with same filename as 2 files from Original folder (make sure at least ONE of these files is in allow list)
4. Run program

*Severity* - 2

*Priority* - 2

*Media*