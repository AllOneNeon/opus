import nltk 
import opusfilters  
import re 

# Load the English dataset 
english_data = load_text('./dataset/WikiMatrix.en-ru.en') 
# Load the Russian dataset 
russian_data = load_text('./dataset/WikiMatrix.en-ru.ru') 

# Apply the Opus filter   
english_filtered_data = opusfilters.filter(english_data, 'grammar,typo,spelling') 
russian_filtered_data = opusfilters.filter(russian_data, 'grammar,typo,spelling') 

# Function that checks if an English word doesn't appear in the Russian versions 
def check_words(row): 
    # Split each row into a list of words 
    english_row = row[0].split(' ') 
    russian_row = row[1].split(' ') 
 
    # Get the intersection between them 
    same_words = set.intersection(set(english_row), set(russian_row)) 
     
    # Compare length of sets 
    if len(same_words) != len(english_row): 
        return False 
    else: 
        return True 
 
# Filtering out translations 
filtered_data = [row for row in zip(english_filtered_data, russian_filtered_data) if check_words(row)] 

# Print the filtered data 
for i in filtered_data: 
    print(i) 
 
# Export the filtered data 
with open("filtered_data.txt", "w") as output: 
    for line in filtered_data: 
        output.write("%s\n" % str(line))