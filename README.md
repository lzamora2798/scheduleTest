# scheduleTest

This code does not import any library, for running you just need python 3.x and upper versions.

For this code we use three functions that will help the good process of the schedules files.

1.  processOverlap, recive as input two time ranges in seconds and the output will be true if they overlap or false if their not.

2. convertToSeconds, recive as input a string with hours and minutes, and return as output a convertion of them to a list of their equivalent in seconds.

3.  ProcessFile, recive as input a file and the output is a dict with keys of  a tuple of the two collaborators names which overlaps in their time, and the value of those keys will be  the count of how many have they overlaped. The core of the function has two parts, first one the one who proccess the file and build a dictionary with the informations of each day of the week and how many workers have been working on them. 
Second part and last, is the one who process the dictionary with the olverlap funcion and give the result of the output. 


# Run Tests

My test script has four type of test. three first of them tried different files and the last one tries a file with any kind of bad format that will be intercepted by a try except block

For running test just run `python -m unittest test.py`

