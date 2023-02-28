import os  
import re 
import opus_filter 
 
#The directory of your datafiles  
directory = './dataset/' 
 
#Create a list of files of the directory  
files = os.listdir(dataset) 
 
#Declaring necessary variables 
filtered_data = [] 
sourceLang = "en" 
targetLang = "ru" 
 
#Iterating through the elements of the list  
for file in files: 
 
    #Using Opus filter to check consistency 
    if not opus_filter.check_translation_quality(file, sourceLang, targetLang):  
      
       #Read source english document 
        with open("{}/{}".format(directory,file)) as fh: 
            for line in fh: 
                match = re.search("n_sid:[0-9]+", line) 
             
                #Check for incorrect translation in line 
                if match: 
                 
                    # Filtering the lines with incorrect translations 
                    idtxt = match.group(0)[7:] 
                    delnumt = int(idtxt) 
                    if delnumt > 0: 
                        filtered_data.append(line) 
 
#Writing the new dataset with the filtered lines 
with open("filtered_data.txt","w") as fh: 
    for line in filtered_data: 
        fh.write("%s\n" % line)