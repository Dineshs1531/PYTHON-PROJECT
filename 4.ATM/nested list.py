dict={"DINESH":[1234,2000],"RAMESH":[4567,1000]}
"""for i in dict:
  print(dict[i][1])"""
 
name=input("enter the name : ")
password=int(input("enter the password : "))
# CHECKING THE NAME AND PASSWORD
account=input("DO YOU HAVE ACCOUNT IN BANK PLEASE ENTER YES/NO : ")
if account=="YES":
  for i in dict:
    if name==i and dict[i][0]==password:
      print("correct")
else:
  noaccount=input("Do YOU WANT TO CREATE ACCOUNT FROM THIS BANK YES/NO : ")
  if noaccount=="YES":
    dict[input("enter the your name : ")]
#ADD THE NEW CUSTORMER
