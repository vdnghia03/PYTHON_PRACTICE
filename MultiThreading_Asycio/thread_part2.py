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

# Bài toán này là cùng 1 công việc, chỉ khác nhau về đầu vào cho từng công việc đó.
# Ví dụ bài toán gặt lúa, 3 worker cùng gặt lúa trong buổi sáng bắt đầu làm cùng nhau
# Người A gặt ngoài cùng, người B gặt ở giữa và người C gặt ở phần trong cùng.
"""
def sum_exponent(chunk, name):
    result = 0  # Khởi tạo là int
    for x in chunk:
        time.sleep(0.01)
        result += x**x  # Giữ int
    # print(f"Thread {name} is Finish, result: {result}")
    return result

myList = list(range(1, 101))
chunk_size = len(myList) // 5 + 1
chunks = [myList[i:i + chunk_size] for i in range(0, len(myList), chunk_size)]


start_time = time.perf_counter()

TOTAL_SUM = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

    # 1. Use Submit
    futures = [executor.submit(sum_exponent, chunk, i) for i, chunk in enumerate(chunks)]
    # total = 0
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        # print(f"Thread result : {result}")
        TOTAL_SUM += result

    # 2. Map
    
print(f"Total result: {TOTAL_SUM}")
print(f"TOTAL SUM - Duration: {time.perf_counter() - start_time}")


start_time_2 = time.perf_counter()
print(sum_exponent(myList, "A"))
print(f"FUCNTION - Duration: {time.perf_counter() - start_time_2}")

"""
# =========================== Bài toán 2 ========================================
# 3 công nhân làm 3 công việc khác nhau để xây nhà không liên quan gì đến nhau
# Người A phụ trách đi mua gạch, người B phụ trách xây và người C phụ trách mang vác.

def c(chunk):
    result = 0  # Khởi tạo là int
    for x in chunk:
        time.sleep(0.01)
        result += x**x  # Giữ int
    # print(f"Thread {name} is Finish, result: {result}")
    return result


def a(str):
    return str


def b(str):
    return str

myList = list(range(1, 101))
conviec = [c, a, b]
doiso = [myList, "Nghia", "Nam"]

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

    # 1. Use Submit
    futures = [executor.submit(conviec[i], doiso[i]) for i in range(3)]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(result)