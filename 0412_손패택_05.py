'''
202195057 손패택
컴퓨터학부
'''
fac=1
input_num=int(input("점수 입력 :"))#初始值
while input_num >= 1:#条件式
    fac = fac * input_num
    input_num = input_num - 1 #증감식
print(f"{input_num}! = {fac}")
#5! = 120
