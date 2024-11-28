import matplotlib.pyplot as plt

def score_distribution_graph(subject, scores, male_count, female_count, font = 'NanumGothic'):
    # 1. subject : 사용자가 선택한 과목
    # 2. socres : 선택한 과목의 표준점수 리스트 
    # 3. male_count : 표준점수의 남자 인원 
    # 4. female_count : 표준점수의 여자 인원
    # 2, 3, 4  socres에 있는 표준 점수의 인덱스가 male_count, female_count에 있는 인원의 인덱스와 같아야함, socres 리스트가 내림차순 또는 오름차순으로 정렬되어야함
    # 5. font : 한글이 깨지면 폰트 바꾸기
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.family'] = font
    plt.title('2024학년도 수능 %s과목 분포' %subject)
    plt.plot(scores, male_count, label='남')
    plt.plot(scores, female_count, label='여')
    plt.xlabel('표준점수')
    plt.ylabel('인원')
    plt.legend(loc = 'best')
    plt.show()
