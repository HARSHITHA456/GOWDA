import random
count=0
while(count<=100):
     n=input("pressr to roll a die")
     if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random is",r)
        print( "your count is",count)
     if   count==8:
          count=37
          print("wow climbed up the ladder and count is",count)
     if   count==13:
          count=34
          print("wow climbed up the ladder and count is",count)
     if   count==40:
          count=68
          print("wow climbed up the ladder and count is",count)
     if   count==52:
          count=81
          print("wow climbed up the ladder and count is",count)
     if   count==76:
          count=87
          print("wow climbed up the ladder and count is",count)
     elif count==11:
          count=2
          print("ohh snake bit come down and count is",count)
     elif count==25:
          count=4
          print("ohh snake bit come down and count is",count)
     elif count==38:
          count=9
          print("ohh snake bit come down and count is",count)
     elif count==65:
          count=46
          print("ohh snake bit come down and count is",count)
     elif count==89:
          count=70
          print("ohh snake bit come down and count is",count)
     elif count==93:
          count=64
          print("ohh snake bit come down and count is",count)
     elif count>=100:
          print("win")
     else:
         print("CONTINUE THE GAME")
