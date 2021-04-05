import matplotlib.pyplot as plt
from math import *



#모터의 입력 값
theta_1=0
theta_2=0
#로봇팔의 길이
D=1
#원점과 로봇팔 끝점과의 길이
L=0
#로봇팔 끝점과 원점을 이은 직선과 수평선 사이의 각도
theta_3=0

print("단순 ㄱ자 모형 로봇팔입니다")
theta_1=input("첫번째 모터 각도를 입력하세요")#이때는 60분법으로 입력받음
theta_2=input("두번째 모터 각도를 입력하세요")#이때는 60분법으로 입력받음
print("첫번째 모터 각:{0}  두번째 모터 각:{1}".format(theta_1,theta_2))
theta_1=radians(int(theta_1))
theta_2=radians(int(theta_2))
L=sqrt(2*(D**2)*(1-cos(theta_2)))#cos(pi-theta_2)=cos(theta_2)이니까!!
theta_3=theta_1+(float(theta_2)-float(pi))/2
print(L)
plt.axis([-2, 2, -2, 2])
plt.plot([0,D*cos(theta_1)],[0,D*sin(theta_1)],"g-",marker='*')
# plt.plot([0,D*cos(theta_1+1.57)],[0,D*sin(theta_1+1.57)])
plt.plot([D*cos(theta_1),L*cos(theta_3)],[D*sin(theta_1),L*sin(theta_3)],marker='*')
plt.plot([0],[0],"yo")#로봇팔이 최종적으로 가르키는 위치
plt.plot([L*cos(theta_3)],[L*sin(theta_3)],"ro")#로봇팔이 최종적으로 가르키는 위치
plt.title('final_robot_position:\nx:{0} y:{1}'.format(L*cos(theta_3),L*sin(theta_3)), loc='left', pad=20)

plt.show()