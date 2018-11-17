power=[[0,2,2,2],
       [7,3,3,3],
       [0,0,0,0],
       [4,3,3,3],
       [0,0,0,0]]

def last():
    print('剩余产能:')
    for i in range(5):
        print('p'+str(i+1),end=':')
        print(power[i])

def dan1():
    p,num,time=input('产品，个数，交货期:').split()
    p=int(p);num=int(num);time=int(time)
    if num<power[p-1][time-1]:
        power[p-1][time-1]-=num
    elif num<power[p-1][time-1]+power[p-1][time-2]:
        power[p-1][time-2]-=(num-power[p-1][time-1])
        power[p-1][time-1]=0
    else:
        power[p-1][time-3]-=(num-power[p-1][time-1]-power[p-1][time-2])
        power[p-1][time-1]=0
        power[p-1][time-2]=0
    last()
    dan1()

print(power)
dan1()