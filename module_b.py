import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.rcParams['font.family'] = '1' #1. 한글표시가 되는 폰트
plt.title('2024학년도 수능 %s과목 분포' %2) #2. 사용자가 선택한 과목
plt.plot(3, 4, label='남') #3. 선택한 과목의 표준점수 리스트, #4. 표준점수의 남자인원
plt.plot(3, 5, label='여') #3. 선택한 과목의 표준점수 리스트, #5. 표준점수의 여자인원
plt.xlabel('표준점수')
plt.ylabel('인원')
plt.legend()
plt.show()
