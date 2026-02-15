import time
[1, 2, 3, 4]

n = 1000
my_list = list(range(n))

def process_data(x):
    time.sleep(0.001)

def my_fun1(x):
    start_time = time.time()
    process_data(x)
    end_time = time.time()
    print(f"[my_fun1] Time taken: {end_time - start_time} seconds")

def my_fun2(x):
    start_time = time.time()
    for i in x:
        process_data(i)
    end_time = time.time()
    print(f"[my_fun2] Time taken: {end_time - start_time} seconds")

def my_fun3(x):
    start_time = time.time()
    for i in range(len(x)):
        for j in range(len(x)):
            process_data(x[i])
    end_time = time.time()
    print(f"[my_fun3] Time taken: {end_time - start_time} seconds")

# O(1)
my_fun1(my_list)

# # O(n)
my_fun2(my_list)

# O(n^2)
my_fun3(my_list)
