a=int(input("Enter The Number : "))   #Input
n1 = int( "%s" % a )                  #First number in equation
n2 = int( "%s%s" % (a,a) )            #Second number in equation
n3 = int( "%s%s%s" % (a,a,a) )        #Third number in equation
sum=n1+n2+n3                          #The quation
print("sum = " ,n1 ,"+",n2,"+",n3,"=" ,sum)     #Print