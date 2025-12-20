# Python-Assignment-3

# Assignment and practice

1. Task 1
   Problem statement : To find factorial of a number
   Solution:
   1. first take a number as an input form user 
   2. var factor hold curr val as 1 
   3. factorial is calculated as  : n*(n-1) until n reaches to 1
   4. So, we will take factor as 1 mutiply it with current value of n and 
      decrement the value of n by 1 until it reaches endpoint. 
   5. Iterate the process using while loop under condition.
   
  Using Recursion:
  1. We will use factorial function itself for process
  2. factor  = num * factorial(n-1)
  3. It will call itself again and again until n = 1 ,for n = 1 we wil return 1 and end the process.


2. Task 2
    Problem statement : to find following value of a user input number 
     Square root of the number
     Natural logarithm (log base e) of the number
     Sine of the number (in radians)

   Solution :
   1. we will import math module 
   2. than import the sqrt() function for square root , log() function for logarithm of num value and 
      sin(x,base) for sin value .Here, for sin x = num and base will be e by default i.e sin(num)
   3. By using above math module functions we will print above result for an user input.