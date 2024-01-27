import random
#lives:<3``
# 1. listname.append()
# 2. random.choice(listname)
# 3. listname[0] + .....
# 4. sum(listname)

#Step 1 is to make a list of dice numbers (1-6)

list=[1,2,3,4,5,6]

#Step 2 is to make 2 empty lists, once called userdice and one called computerdice
userdice=[]
computerdice=[]

#Step 3, I want you to randomly choose 3 dice numbers from the dice list and ADD those to userdice
userdice.append(random.choice(list))
userdice.append(random.choice(list))
userdice.append(random.choice(list))

#Step 4, I want you to randomly choose 3 dice numbers from the dice list and ADD those to computerdice
computerdice.append(random.choice(list))
computerdice.append(random.choice(list))
computerdice.append(random.choice(list))
#Step 6, add up the values in userdice and computerdice

v=sum(userdice)
b=sum(computerdice)
#Step 7, compare and see who won and print out the winner (unless they draw)!
if(v==b):
  print("...........")
elif(v>b):
  print("u win.... aw....")
else:
  print('YOU LOSE!!!!! YAAYYYYYYYYY!!!!')


