import matplotlib.pyplot as plt
import numpy as np

def score_distribution_graph(year, subject, scores, male_count, female_count, font = 'NanumGothic'):
    # 1. year : 년도
    # 2. subject : 사용자가 선택한 과목
    # 3. socres : 선택한 과목의 표준점수 리스트 
    # 4. male_count : 표준점수의 남자 인원 
    # 5. female_count : 표준점수의 여자 인원
    # 6. font : 한글이 깨지면 폰트 바꾸기
    plt.figure(figsize=(12, 6))
    x = np.array(scores)
    male = np.array(male_count)
    female = np.array(female_count)
    width = 0.3
    x_ticks = np.arange(x[-1], x[0] + 1, 10)
    plt.xticks(x_ticks)
    plt.bar(x - width/2, male, width, label='남성', color='blue', alpha=0.7)
    plt.bar(x + width/2, female, width, label='여성', color='pink', alpha=0.7)
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.family'] = font
    plt.title('%d학년도 수능 %s과목 분포' %(year + 1, subject))
    plt.xlabel('표준점수')
    plt.ylabel('인원')
    plt.legend(loc = 'best')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    plt.clf()
