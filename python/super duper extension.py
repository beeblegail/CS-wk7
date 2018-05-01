#!/usr/bin/env python
# Author : Abbey Pates
# Date : 23.04.18
# Version : 1

from functools import reduce

# ask user for a value and check their reply - if not a number the loop is restarted
# checks value is in parameters 
def askUser(question , lowerLimit, upperLimit):
   while True:
      try:
         answer = int(input(question))
      except ValueError:
         print("Not an integer value...")
         continue
      else:
         if (answer < lowerLimit) | (answer > upperLimit):
            print("Not within the range " + str(lowerLimit) + " and " + str(upperLimit))
         else:
            return (answer)
            break

def isEven(number):
   return number%2==0


def primeNumber(number):
   if number >= 2:
      for y in range(2,number):
         if not ( number % y ):
            return False
   else:
      return False
   return True


def factors(number):
   factorsStr = ""
   for value in  set(reduce(list.__add__, 
                ([i, number//i] for i in range(1, int(pow(number, 0.5) + 1)) if number % i == 0))):
       factorsStr += str(value) + ", "
   return factorsStr
   

if __name__ == '__main__':
   print("Properties Of a Numbers")
   print("=======================")

   number = askUser("Please select your number", 0, 5000000000)
   print("The number " + str(number) + ";")
   
   if isEven(number):
      print("is an even number")
   else:
      print("is an odd number")
      
   if primeNumber(number):
      print("is a prime number")
   else:
      print("is not a prime number")
      
   print("has the factors: " + factors(number))
   
      
