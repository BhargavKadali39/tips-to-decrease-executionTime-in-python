x = 10
y = 20
temp = x
x = y
y = temp
print(x,y)
import time
start_time = time.time()
#------------------------- code area -----------------------------------------

x = 10
y = 20
temp = x
x = y
y = temp
print(x,y)

#------------------------- code area -----------------------------------------
end_time = time.time()
total_time = end_time - start_time
print("Execution time is :",total_time)
