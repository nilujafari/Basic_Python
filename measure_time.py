import time

cache = {}

def cache_result(x):
    if x in cache:
        return cache[x]
    else:
        result = my_sum(x)
        if len(cache) >100:
            # remove the lower value key
            cache.pop(min(cache.keys(), key=cache.get))
        cache[x] = result
        print(f"[cache] Cache size: {len(cache)}")
        return cache[x]

def my_sum(num):
    start = time.time()
    total = 0
    for i in num :
        total += i
    end = time.time()
    time_dif = end - start
    print(f"[my_sum] Time taken: {time_dif} seconds")
    return total
my_sum(range(1, 5000000))

while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    print(cache_result(range(1, n+1)))
    
    