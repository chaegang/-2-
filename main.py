import module_a
import module_b
import matplotlib as plt
from matplotlib import font_manager, rc

#파일 입력 받기
#과목 리스트 만들고 사용자 과목 입력 받기
#과목에 따른 표준점수, 남자, 여자 리스트 만들기
#module_b.score_distribution_graph -> 그래프 그리기

year_list=['2020','2021','2022','2023']
user_year = input("연도 선택(2020,2021,2022,2023) :")
while True:
    if user_year not in year_list:
        user_year = input("다시 연도 입력")
    else:
        break

subject_list = module_a.extract_subjecT(f'https://github.com/chaegang/computer_programming_II/raw/refs/heads/NEW/{user_year}1231.csv')

print("과목:"," ".join(subject_list))
user_subject = input("과목 입력")
        
while True:
    if user_subject not in subject_list:
        user_subject = input("다시 과목 입력")
    else:
        break

data_list = module_a.extract_data(f'https://github.com/chaegang/computer_programming_II/raw/refs/heads/NEW/{user_year}1231.csv',user_subject)

scores = []
males_list = []
females_list = []


for score, male, female in data_list:
    scores.append(score)
    males_list.append(male)
    females_list.append(female)

module_b.score_distribution_graph(int(user_year),user_subject, scores, males_list, females_list, font = 'Malgun Gothic')
