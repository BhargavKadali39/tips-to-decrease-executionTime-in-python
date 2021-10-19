import time
start_time = time.time()
#------------------------- code area -----------------------------------------

a = 10
b = 20
a, b = b, a
print(a,b)

#------------------------- code area -----------------------------------------
end_time = time.time()
total_time = end_time - start_time
print("Execution time is :",total_time)
