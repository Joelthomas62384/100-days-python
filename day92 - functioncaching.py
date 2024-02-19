import functools    
import time


@functools.lru_cache(maxsize=None)
def fn(n):
    time.sleep(5)
    return n*20


while (num:= input("Enter the number : ")) != "quit":
    print(fn(int(num)))
    print(f"Done for {num}")









# Memoization
# print(fn(20))
# print("Done for 20")
# print(fn(5))
# print("done for 5")
# print(fn(10))
# print("done for 10")


# print(fn(20))
# print("Done for 20")
# print(fn(5))
# print("done for 5")
# print(fn(10))
# print("done for 10")



