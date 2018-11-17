import xlrd

w=xlrd.open_workbook('ss2.xlsx')

ad=w.sheet_by_index(0)
p11=[];p12=[];p13=[];p14=[];p15=[]
p21=[];p22=[];p23=[];p24=[];p25=[]
p31=[];p32=[];p33=[];p34=[];p35=[]
p41=[];p42=[];p43=[];p44=[];p45=[]
p51=[];p52=[];p53=[];p54=[];p55=[]
for i in range(2,163,8):
    p11.append(ad.cell_value(i,2))
    p12.append(ad.cell_value(i,3))
    p13.append(ad.cell_value(i,4))
    p14.append(ad.cell_value(i,5))
    p15.append(ad.cell_value(i,6))

if any(p11):print('p1本地');print(sorted(p11,reverse=True))
if any(p12):print('p1区域');print(sorted(p12,reverse=True))
if any(p13):print('p1国内');print(sorted(p13,reverse=True))
if any(p14):print('p1亚洲');print(sorted(p14,reverse=True))
if any(p15):print('p1国际');print(sorted(p15,reverse=True))
print()


for i in range(3,164,8):
    p21.append(ad.cell_value(i,2))
    p22.append(ad.cell_value(i,3))
    p23.append(ad.cell_value(i,4))
    p24.append(ad.cell_value(i,5))
    p25.append(ad.cell_value(i,6))

if any(p21):print('p2本地');print(sorted(p21,reverse=True))
if any(p22):print('p2区域');print(sorted(p22,reverse=True))
if any(p23):print('p2国内');print(sorted(p23,reverse=True))
if any(p24):print('p2亚洲');print(sorted(p24,reverse=True))
if any(p25):print('p2国际');print(sorted(p25,reverse=True))
print()


for i in range(4,165,8):
    p31.append(ad.cell_value(i,2))
    p32.append(ad.cell_value(i,3))
    p33.append(ad.cell_value(i,4))
    p34.append(ad.cell_value(i,5))
    p35.append(ad.cell_value(i,6))

if any(p31):print('p3本地');print(sorted(p31,reverse=True))
if any(p32):print('p3区域');print(sorted(p32,reverse=True))
if any(p33):print('p3国内');print(sorted(p33,reverse=True))
if any(p34):print('p3亚洲');print(sorted(p34,reverse=True))
if any(p35):print('p3国际');print(sorted(p35,reverse=True))
print()


for i in range(5,166,8):
    p41.append(ad.cell_value(i,2))
    p42.append(ad.cell_value(i,3))
    p43.append(ad.cell_value(i,4))
    p44.append(ad.cell_value(i,5))
    p45.append(ad.cell_value(i,6))

if any(p41):print('p4本地');print(sorted(p41,reverse=True))
if any(p42):print('p4区域');print(sorted(p42,reverse=True))
if any(p43):print('p4国内');print(sorted(p43,reverse=True))
if any(p44):print('p4亚洲');print(sorted(p44,reverse=True))
if any(p45):print('p4国际');print(sorted(p45,reverse=True))
print()


for i in range(6,167,8):
    p51.append(ad.cell_value(i,2))
    p52.append(ad.cell_value(i,3))
    p53.append(ad.cell_value(i,4))
    p54.append(ad.cell_value(i,5))
    p55.append(ad.cell_value(i,6))

if any(p51):print('p5本地');print(sorted(p51,reverse=True))
if any(p52):print('p5区域');print(sorted(p52,reverse=True))
if any(p53):print('p5国内');print(sorted(p53,reverse=True))
if any(p54):print('p5亚洲');print(sorted(p54,reverse=True))
if any(p55):print('p5国际');print(sorted(p55,reverse=True))