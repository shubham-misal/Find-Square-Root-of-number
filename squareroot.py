#find square-root of a number
while True:
  num=int(input("Enter a number:\n>>"))
  for i in range(2, num ):
    cond = (num % i == 0)
    if(cond == True):
      #print(i)
      k=(i*i==num)
      if(k==True):
        print("\n==>",i)
        break
  else:
    kd=(num**0.5)
    print("\n==>",kd)