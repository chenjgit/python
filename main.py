
# while
i=1
while i<10:
    print(i)
    if i==5:
     break
    i=i+1
# for
x=[1,2,12,2,3]
for i in x:
    print(i)
# if
a=20
b=30
if a>b:
    print(a)
else:
    print(b)

my_weight=int (input('请输入体重：'))
my_height=float(input("请输入身高"))
bmi=my_weight/my_height**2
if bmi<18.5:
   print('太轻了')
elif bmi>=18.5 and bmi<24:
    print('ok')
else:
    print('太重了')

