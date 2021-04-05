import matplotlib.pyplot as plt
from math import *



#모터의 입력 값:theta_1,theta_2
#로봇팔의 길이:D
class SCARA_BOT:
  def __init__(self,x_pos,y_pos,theta_1,theta_2,D):
    self.x_pos=x_pos
    self.y_pos=y_pos
    self.theta_1=theta_1
    self.theta_2=theta_2
    self.D=D

  def CHANGE_DEGREE(self):
    self.theta_1=radians(int(self.theta_1))
    self.theta_2=radians(int(self.theta_2))


class SCARA_BOT_HOM(SCARA_BOT):
  def __init__(self,theta_1,theta_2,D):
    SCARA_BOT.__init__(self,theta_1,theta_2,D)

  def draw_line(self):
    self.CHANGE_DEGREE()
    #원점과 로봇팔 끝점과의 길이
    L=0
    #로봇팔 끝점과 원점을 이은 직선과 수평선 사이의 각도
    theta_3=0
    theta_1=self.theta_1
    theta_2=self.theta_2
    D=self.D
    L=sqrt(2*(D**2)*(1-cos(theta_2)))#cos(pi-theta_2)=cos(theta_2)이니까!!
    theta_3=theta_1+(float(theta_2)-float(pi))/2
    plt.axis([-2, 2, -2, 2])
    plt.plot([0,D*cos(theta_1)],[0,D*sin(theta_1)],"g-",marker='*')
    # plt.plot([0,D*cos(theta_1+1.57)],[0,D*sin(theta_1+1.57)])
    plt.plot([D*cos(theta_1),L*cos(theta_3)],[D*sin(theta_1),L*sin(theta_3)],marker='*')
    plt.plot([0],[0],"yo")#로봇팔이 최종적으로 가르키는 위치
    plt.plot([L*cos(theta_3)],[L*sin(theta_3)],"ro")#로봇팔이 최종적으로 가르키는 위치
    plt.title('final_robot_position:\nx:{0} y:{1}'.format(L*cos(theta_3),L*sin(theta_3)), loc='left', pad=20)
    plt.show()

a=0
b=0
c=1
print("단순 ㄱ자 모형 로봇팔입니다.로봇팔 길이는 1")
a=input("첫번째 모터 각도를 입력하세요")#이때는 60분법으로 입력받음
b=input("두번째 모터 각도를 입력하세요")#이때는 60분법으로 입력받음
print("첫번째 모터 각:{0}  두번째 모터 각:{1}".format(a,b))

scr_bot_1=SCARA_BOT(1,1,a,b,c)
scr_bot_1.CHANGE_DEGREE()
print("첫번째 모터 각:{0}  두번째 모터 각:{1}".format(scr_bot_1.theta_1,scr_bot_1.theta_2))
# scr_bot_1.draw_line()
# scr_bot_1=SCARA_BOT_HOM(a,b,c)
# scr_bot_1.draw_line()
