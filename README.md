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
