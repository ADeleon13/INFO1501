import rectangle
import rug
import carpet
import random
def main():
   rectangleList = []
   #for loop that creates 3 carpets and add them to a list
   for carpetNum in range(3):
      length = random.randrange(1, 10)
      width = random.randrange(1, 10)
      PPS = random.randrange(1, 10)
      myCarpet = carpet.Carpet(length, width, PPS)
      rectangleList.append(myCarpet)

      # for loop that creates 2 rugs and adds them to a list
   for rugNum in range(2):
      length = random.randrange(1, 10)
      width = random.randrange(1, 10)
      price = random.randrange(1, 10)
      myRug = rug.Rug(length, width, price)
      rectangleList.append(myRug)


   #for loop that iterates through the list and prints out their str representations
   for rectangle in rectangleList:
      print(rectangle.__str__())

if __name__== '__main__':
    main()



