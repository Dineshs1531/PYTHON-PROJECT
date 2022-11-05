
d={1:'Dosa',2:'portta',3:'chicken briyani',4:'mutton briyani',5:'pizza',6:'chicken rice'}
c={1:30,2:20,3:200,4:250,5:300,6:100}
for x,y in d.items():
        print(x," : ",y)
def choice():
    i=int(input("enter the choice : "))
    if i>=1 and i<=6:
        print("yes ,your is food avaiable")
    else:
        print("NO ,your food is not avaiable")
    q=int(input("enter the quantity: "))
    return i,q;

sum=0
q=1
co='yes'
order=True
while order:
    if co=='yes':
        x,q=choice()
        sum+=(c[x]*q)
        co=input("do you want to continue yes or no :")
    else:
        print("total amount : ",sum)
        break

