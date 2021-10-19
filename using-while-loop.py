import time
start_time = time.time()
#------------------------- code area -----------------------------------------

i=0
while True:
    print(i)
    i += 1
    if i == 10:
        print('over')
        break

#------------------------- code area -----------------------------------------
end_time = time.time()
total_time = end_time - start_time
print("Execution time is :",total_time)
