id=input("Enter your id: ")

while (len(id)>9):
    print("Sorry - your id is too long")
    id=input("Enter your id again: ")
id="0"*(9-len(id))+id
sum=0
for i in range(0,len(id)):
    temp = int(id[i]) * (1+(i%2))
    sum+=temp%10 + temp//10
if sum%10==0:
    print("Your id is valid ",id)
else:
    print("Your id is not valid ",id)