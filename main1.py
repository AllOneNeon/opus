
import pandas as pd  
from opustools_wrapper.opus_filter import filter 

english_df = pd.read_csv("./dataset/WikiMatrix.en-ru.en")   
russian_df = pd.read_csv("./dataset/WikiMatrix.en-ru.ru")   

incorrect_en_df = pd.DataFrame(columns=english_df.columns)   
incorrect_ru_df = pd.DataFrame(columns=russian_df.columns)   

# Maximum edit distance 
dist = 2  
 
# Language to look for language errors in 
lang = "ru" 

for i, row in english_df.iterrows(): 
    filter_results = filter(row["text"], russian_df.iloc[i]["text"], dist, lang) 
     
    # Add row to incorrect translations if the filter fails 
    if not filter_results["passed"]: 
        incorrect_en_df = incorrect_en_df.append(row, ignore_index=True) 
        incorrect_ru_df = incorrect_ru_df.append(russian_df.iloc[i], ignore_index=True)  

updated_en_df = english_df[~english_df.index.isin(incorrect_en_df.index)] 
updated_ru_df = russian_df[~russian_df.index.isin(incorrect_ru_df.index)] 

updated_en_df.to_csv("filtered_english_data.csv")  
updated_ru_df.to_csv("filtered_russian_data.csv")