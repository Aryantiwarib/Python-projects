# with open("f.txt", "r") as f:
#     p=f.readlines()
    
# d={}
# for l in p:
#     parse=l.split("\t")
#     d[parse[0]]=float(parse[1])
#     # print(l)10
#     print(parse[0])
# n=int(input("Enter your amount\n"))
# m=input("Enter the country\n")
# print(f"{n} INR in {m} is {d[m]*n:0.2f}")

with open("f.txt","r")as f:
    p=f.readlines()
d={}
for i in p:
    r=i.split("\t")
    d[r[0]]=float(r[1])
    print(r[0])
n=int(input("Enter your amount\n"))
m=input("Enter the country\n")
print(f"{n} INR in {m} is {d[m]*n:0.2f}")  
    
    
