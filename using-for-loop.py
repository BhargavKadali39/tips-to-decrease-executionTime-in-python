import time
start_time = time.time()
#------------------------- code area -----------------------------------------

for i in range(10):
print(i)
if i == 9:
    print('over')

#------------------------- code area -----------------------------------------
end_time = time.time()
total_time = end_time - start_time
print("Execution time is :",total_time)
