# General
This project contains the code of a solution for a coding challenge I received.  
The code was written in Python 3 on the 23/08/2019.  
It is important to note that the code may generate significant CPU load at times (relative to a regular home PC).  
  
  
# The Terms and Content of the Challenge
Background information:  
You can choose the programming language you feel the most comfortable with.  
We expect that you can solve this within 1 hour.  



Task:  
For any positive integer n we define two rules:  
if even: divide by two  
if odd: multiply by three, then add one, and repeat until the result is the number 1  



This will generate sequences of numbers like below, converging to 1:  



3, 10, 5, 16, 8, 4, 2, 1  



7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1  



For each number n we can now count the number of steps in this sequence until we reach 1.  



So the sequence above, starting with 3, has a length of 8 (including the starting point and the final one).  
The second sequence has a length of 17.  



Challenge:  
Find the second-longest sequence of all the integers smaller or equal than 10 Million.  



Some calibration help:  
The longest sequence for input <= 1000 has a length of 179  
The longest sequence for input <= 10000 has a length of 262  



Calculate the sum of all the elements of the above mentioned second-longest sequence and share your result. Also, please include your source code.  
  
  
# Solution Workflow
* Import the module "time" and save the start time of the program to later calculate the run time.  
* Create two lists - one containing the length of each sequence per integer, the other containing the sum of each sequence per integer.  
* Run a for loop on the range of integers between 1 and 10,000,001.  
* Create a while loop under which the calculations for each integer will be made and break out of it once the sequence reaches 1.  
* 
