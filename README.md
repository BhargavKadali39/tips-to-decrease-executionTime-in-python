# tips-to-decrease-executionTime-in-python
Here are some amazingly useful tips to decrease execution time in python programs

As a beginner I admit that most of the tips given below are some of my deeds too, so this repo we will learn how to decrease the execution time.

The method I used here to calculate the time is previously explained in one of my repos which you can find by<br>[clicking here](https://github.com/BhargavKadali39/Execution_time)
  
## do not import the whole module
When we try to use certain module and we know it's sole purpose is only to serve a single function.
Then try importing only that single function instead of the whole thing.

syntax
> from module_name import function_name1, function_name2,etc,...

Example:

    from math import ceil, floor
    
    i = 9.67
    
    print(ceil(i))
    print(floor(i))
    
    output:
      10
      9
      
> Execution time: 0.008982419967651367

    import math
    
    i = 9.67
    
    print(ceil(i))
    print(floor(i))
    
> Execution time: 0.01605224609375
see the difference, amazing right


## no temp variables 
In one of my previous repos about different [swapping techniques](https://github.com/BhargavKadali39/Swapping_in_python) I stated to use <br>

    a = 10
    b = 20
    a, b = b, a
    print(a,b)
> Execution time is :  0.014656782150268555
 
Instead of the below code

    x = 10
    y = 20
    temp = x
    x = y
    y = temp
    print(x,y)
    
    Output: 20 10
> Execution time is : 0.014772176742553711
Might be closer but worthwhile when running in a loop.

## for loop for the win
This is the most common mistake made by most of us, that is using while-loop even tho the job could be done with a for-loop.
<h3>using for-loop</h3>

    
    for i in range(10):
    print(i)
    if i == 9:
        print('over')
        
    output:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    over
    > Execution time is : 0.05827617645263672
    
<h3>using while-loop</h3>
    
    i=0
    while True:
        print(i)
        i += 1
        if i == 10:
            print('over')
            break
            
    output:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    over
> Execution time is : 0.07421302795410156
    
