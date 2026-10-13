n=[]
hangshu=int(input("请输入杨辉三角的行数应大于等于1:"))
if hangshu<1:
    print("输入错误")
for i in range(0,hangshu):
    n.append(1)
for i in range(0,hangshu):
    for j in range(i-1,0,-1):
         n[j]=int(n[j])+int(n[j-1])
    for k in range(0,i+1):
        print(n[k],end=" ")
    print()