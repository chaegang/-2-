import csv 
import pandas as pd

#return [표준점수, 남자, 여자]

def extract_data(file_path, subject):
    #dataList - [score, 남자, 여자] 


    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    
    subject_data = df[df['유형'] == subject]
    subject_sorted = subject_data.sort_values(by='표준점수', ascending=False)
    data = subject_sorted[['표준점수','남자', '여자']]
    data_list = data.values.tolist()
    return data_list
