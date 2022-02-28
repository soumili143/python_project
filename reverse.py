n=int(input("enter a number"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
    print("reverse of num",rev)