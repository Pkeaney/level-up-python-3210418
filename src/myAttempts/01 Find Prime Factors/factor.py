##Challenge - Write a Python Function to find all Prime factors of a given number
##Input - Integer value e.g. 630
##Output - List of prime factors e.g. [2,3,3,5,7]

def findPrimeFactors(input):
  list = []
  divisor = 2
  num = input
  while divisor <= num:
    if num % divisor == 0:
      list.append(divisor)
      num = num / divisor
    else:
      divisor += 1
  return list


print(findPrimeFactors(630))