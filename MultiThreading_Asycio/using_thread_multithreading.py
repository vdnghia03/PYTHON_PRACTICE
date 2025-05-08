# ========================================
#  Hiểu về MultiThread và Asycio Await
# ========================================
#
# Các tác vụ trên Thread
#
# Chứng minh thread chạy concurrent
#
# ========================================


# ================= Thread ===================


# import threading
# import time


# # Dat gia tri

# gia_tri = 100

# def inc_number(number):
#     global gia_tri
#     time.sleep(3)
#     number += 1
#     gia_tri = number
#     print(f'Number is {number}')

# def dosomething(number):
#     print(f'This is main thread')

# # inc_number(99)

# # Làm mới thread - Thread() có 3 parametter 
# # gồm target-công việc muốn thực thi, 
# # args-parametter của target dạng tuple, 
# my_thread = threading.Thread(target = inc_number, args = (1,), daemon = True)
# my_thread.start()

# my_thread.join()

# dosomething(1000)

# # Lấy ra current thread đang chạy
# print(threading.current_thread().name)

# print(f"Gia tri cua bien gia tri la {gia_tri}")



# ====================== Chung minh thread concurrent =================

import threading
import time

def sum_exponent(list, thread_name):
    start_time = time.perf_counter()
    sum = 0
    for x in list:
        time.sleep(0.001)
        sum += x ** x

    print(f'Thread "{thread_name}" says sum exponent is: {sum}')
    print(f'Duration: {time.perf_counter() - start_time} - "{thread_name}"')

myList = [x for x in range(1, 101)]

# Start duration

start_duration = time.perf_counter()

my_thread = threading.Thread(target=sum_exponent, args=([x for x in range(10, 50)], 'Hoa'))
your_thread = threading.Thread(target=sum_exponent, args=([x for x in range(2, 78)], 'Minh'))
her_thread = threading.Thread(target=sum_exponent, args=(myList, 'Thuy'))

my_thread.start()
your_thread.start()
her_thread.start()

my_thread.join()
your_thread.join()
her_thread.join()

print(f"Duration ALL:  {time.perf_counter() - start_duration}")