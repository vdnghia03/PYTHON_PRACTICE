import concurrent.futures
import numpy as np
import time



# def sum_exponent(list, name):
#     """
#     Function to calculate the sum of the exponentials of a list of numbers.
#     """
#     result = 0
#     for x in list:
#         # time.sleep(0.1)  # Simulate a time-consuming operation
#         result = result + x**x
    
#     print(f"Thread {name} is Finish")
    
#     return result



# myList = [x for x in range(1,21)]


# with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#     # 1. Submit the function to the executor
#         # for i in range(5):
#         #     executor.submit(sum_exponent, myList)
#     futures = [executor.submit(sum_exponent, myList, i) for i in range(5)]

#     for future in concurrent.futures.as_completed(futures):
#         print(future.result())


#     # 2. Map the function to the list of numbers



# ========================== Ung Dung 1=======================================

def sum_exponent(chunk, name):
    result = 0  # Khởi tạo là int
    for x in chunk:
        time.sleep(0.1)
        result += x**x  # Giữ int
    print(f"Thread {name} is Finish, result: {result}")
    return result

myList = list(range(1, 21))
chunk_size = len(myList) // 5 + 1
chunks = [myList[i:i + chunk_size] for i in range(0, len(myList), chunk_size)]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(sum_exponent, chunk, i) for i, chunk in enumerate(chunks)]
    total = 0
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(f"Thread result: {result}")
        total += result
    print(f"Total result: {total}")