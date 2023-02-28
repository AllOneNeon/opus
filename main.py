import opus_filters as of 
import re 
 
# Input your datasets here: 
eng_data = './dataset/WikiMatrix.en-ru.en' 
rus_data = './dataset/WikiMatrix.en-ru.ru' 
 
# Create an instance of the Opus Filter object: 
opf = of.OpusFilter() 
 
# Initialize variables for the filtered data: 
eng_filtered = [] 
rus_filtered = [] 
 
# Loop through each line of both datasets:  
for eng_dlt, rus_dlt in zip(eng_data, rus_data): 
    # Check if English data matches the regex criteria: 
    eng_match = re.search(r'<Regex Criteria for English Data>', eng_dlt) 
     
    if eng_match: 
        check_eng = True   
    else: 
        check_eng = False    
     
    # Check if Russian data matches the regex criteria: 
    rus_match = re.search(r'<Regex Criteria for Russian Data>', rus_dlt) 
     
    if rus_match: 
        check_rus = True      
    else: 
        check_rus = False 
     
    # Use the Opus Filter to check for any errors in translation:  
    error_check = opf.opus_filter(eng_dlt, rus_dlt) 
     
    # If no issues are found, append line to filtered datasets: 
    if check_eng is True and check_rus is True and int(error_check) == 0: 
        eng_filtered.append(eng_dlt) 
        rus_filtered.append(rus_dlt) 
    #else: 
    #    continue 
             
# The resulting filtered datasets can then be used as needed:  
print(eng_filtered) 
print(rus_filtered)


# import regex as re 
# import opusfilter 
 
# HEIRARCHICAL_FILTER = [ 
#     opusfilter.OpusFilter( 
#         name='english-russian-errortype',  
#         filter_type=opusfilter.FilterType.Remove, 
#         category['grammar', 'lexical'], 
#         direction='English-Russian', 
#     ) 
# ] 
     
# def filter_data(data): 
#     for item in data: 
#         err, unk = opusfilter.filter(item, HEIRARCHICAL_FILTER, require_all=False) 
#         if err or unk: 
#             data.remove(item) 
#     return data 