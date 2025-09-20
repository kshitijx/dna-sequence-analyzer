import random
target = random.randint(1, 100)
while True :
 userchoice= int(input("guess the number: "))
 if userchoice==target :
  print ("success...")
 if userchoice > target :
  print("your target valur is to big...")
 elif userchoice < target :
  print ("your target val is to small..")
  print ("....game over...")