import re
import opusfilter # import the Opus Filter package 
 
# open the two datasets in both English and Russian 
with open("./dataset/WikiMatrix.en-ru.en", "r") as english, open("./dataset/WikiMatrix.en-ru.ru", "r") as russian: 
    lines = english.readlines() + russian.readlines() # combine them into one list 
 
# initialize a filter to use with Opus 
filt = opusfilter.Filter() 
 
# loop through each line of the dataset 
for line in lines: 
    result = filt.run(line) # run the filter on the current line 
     
    if len(result["Terms"]) > 0: # if there were any errors found 
        lines = [l for l in lines if l != line] # remove the erroneous line 
 
# save the filtered dataset 
with open("filtered_dataset.txt", "w") as outfile:  
    outfile.writelines(lines) 
 
# regex pattern example to find incorrectly translated lines 
pattern = re.compile(r'[A-Z][a-z]+\s([A-Z0-9.,!?]+\s)+[а-я]+')  
 
# further refine the filter by using regex 
for line in lines: 
    res = re.search(pattern, line) 
     
    if res is not None: 
        lines = [l for l in lines if l != line] 
 
# save the filtered dataset again 
with open("filtered_dataset.txt", "w") as outfile:  
    outfile.writelines(lines)