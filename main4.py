import pandas as pd 
from opus_filter import OpusFilter 
from re import compile as regex_compile 
 
# Load the data in pandas 
en_df = pd.read_csv('./dataset/WikiMatrix.en-ru.en', encoding='utf-8') 
ru_df = pd.read_csv('./dataset/WikiMatrix.en-ru.ru', encoding='utf-8') 
 
# Create an instance of the opus filter 
opal = OpusFilter('en-ru') 
 
# Compile the expression for errors detection 
regsx_expr = regex_compile(r'[^A-Za-z0-9_]|[^А-Яа-яёЁ0-9_]') 
 
# Combine the dataframes 
combined_df = pd.concat([en_df, ru_df], axis=1) 
 
# Filter the combined dataframe 
filtered_df = combined_df.drop( 
    combined_df.index[opal.filter(combined_df['en'], combined_df['ru'])] 
) 
 
# Find possible mistakes 
mistakes_df = filtered_df[ 
    filtered_df.applymap(lambda x: True if regsx_expr.search(x) else False).any(axis=1) 
] 
 
# Delete mistakes 
final_df = filtered_df.drop( 
     mistakes_df.index 
) 
 
# Save the filtered data 
final_df.to_csv('processed_data.csv', index=False, encoding='utf-8')