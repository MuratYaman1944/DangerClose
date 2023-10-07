import time as t



time = int(input("Enter the time in seconds : "))


for i in range(time,0,-1):

    print(f"{str(i)} seconds remaining \n")
    t.sleep(1)


print("Time's up !!!")