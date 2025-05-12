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


import threading
import time


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

# import threading
# import time

# def sum_exponent(list, thread_name):
#     start_time = time.perf_counter()
#     sum = 0
#     for x in list:
#         time.sleep(0.001)
#         sum += x ** x

#     print(f'Thread "{thread_name}" says sum exponent is: {sum}')
#     print(f'Duration: {time.perf_counter() - start_time} - "{thread_name}"')



# myList = [x for x in range(1, 101)]

# # Start duration

# start_duration = time.perf_counter()

# my_thread = threading.Thread(target=sum_exponent, args=([x for x in range(10, 50)], 'Hoa'))
# your_thread = threading.Thread(target=sum_exponent, args=([x for x in range(2, 78)], 'Minh'))
# her_thread = threading.Thread(target=sum_exponent, args=(myList, 'Thuy'))

# my_thread.start()
# your_thread.start()
# her_thread.start()

# my_thread.join()
# your_thread.join()
# her_thread.join()

# print(f"Duration ALL:  {time.perf_counter() - start_duration}")

# import multiprocessing
# print(f"Number of CPU: {multiprocessing.cpu_count()}")
# print(f"Number of Threads: {threading.active_count()}")
# print(f"Xem id cua process: {threading.get_ident()}")


# ======================= Vi du su dung thread ===============================================

# import threading
# import requests
# import os

# # Hàm tải một phần của tệp
# def download_part(url, start_byte, end_byte, part_file_name):
#     headers = {'Range': f'bytes={start_byte}-{end_byte}'}
#     response = requests.get(url, headers=headers, stream=True)
#     with open(part_file_name, 'wb') as part_file:
#         part_file.write(response.content)
#     print(f"Downloaded part: {part_file_name}")

# # Hàm ghép các phần lại thành một tệp hoàn chỉnh
# def merge_parts(output_file, part_files):
#     with open(output_file, 'wb') as merged_file:
#         for part_file in part_files:
#             with open(part_file, 'rb') as pf:
#                 merged_file.write(pf.read())
#             os.remove(part_file)  # Xóa file tạm sau khi ghép
#     print(f"Merged file saved as: {output_file}")

# # Hàm chính
# def download_file_multithreaded(url, output_file, num_threads):
#     # Gửi yêu cầu HEAD để lấy kích thước tệp
#     response = requests.head(url)
#     file_size = int(response.headers['Content-Length'])
#     print(f"File size: {file_size} bytes")

#     # Chia tệp thành các phần
#     part_size = file_size // num_threads
#     threads = []
#     part_files = []

#     for i in range(num_threads):
#         start_byte = i * part_size
#         # Byte cuối cùng của phần cuối cùng là file_size - 1
#         end_byte = (start_byte + part_size - 1) if i < num_threads - 1 else file_size - 1
#         part_file_name = f"part_{i}.tmp"
#         part_files.append(part_file_name)

#         # Tạo thread để tải phần này
#         thread = threading.Thread(target=download_part, args=(url, start_byte, end_byte, part_file_name))
#         threads.append(thread)
#         thread.start()

#     # Chờ tất cả các thread hoàn thành
#     for thread in threads:
#         thread.join()

#     # Ghép các phần lại
#     merge_parts(output_file, part_files)

# # URL của tệp lớn (thay bằng URL thực tế)
# file_url = "https://th.bing.com/th/id/R.ab741be55190cee282d40387ed984983?rik=1GvIV4j2S2Ts9g&riu=http%3a%2f%2f4.bp.blogspot.com%2f-vtlRbdqkWT0%2fUYC7OHjSvpI%2fAAAAAAAAt18%2fBs8x07t6MKM%2fs1600%2fDogs%2bWallpapers%2b(1).jpeg&ehk=GD2tW1apASc0o8qYnNg6%2b4HCcOBRDmqeK9I7rXxEMmE%3d&risl=&pid=ImgRaw&r=0"  # URL của một file mẫu 100MB
# output_file_name = "largefile.jpg"

# # Tải tệp bằng 5 thread
# download_file_multithreaded(file_url, output_file_name, num_threads=5)


# ======================== Những vấn đề cần giải quyết =========================================

# Race Condition: Khi nhiều thread cùng truy cập và thay đổi một biến toàn cục mà không có sự đồng bộ hóa, có thể dẫn đến tình trạng không nhất quán trong dữ liệu.
# -> Dùng Lock để đồng bộ hóa truy cập vào biến toàn cục.

variable = 'Python'

def change_string(name, l : threading.Lock):
    global variable
    l.acquire()  # Đoạn này sẽ khóa biến toàn cục
    time.sleep(8)
    variable = "Threading"
    print(f"Thread  {name} change string")
    l.release()  # Giải phóng biến toàn cục

def change_string2(name, l: threading.Lock):
    global variable
    l.acquire()  # Đoạn này sẽ khóa biến toàn cục
    time.sleep(2)
    variable = "Asycio"
    print(f"Thread  {name} change string")
    l.release()  # Giải phóng biến toàn cục

# Dung lock để đồng bộ hóa truy cập vào biến toàn cục
lock = threading.Lock()

thread_1 = threading.Thread(target = change_string, args = ("Nghia", lock))
thread_2 = threading.Thread(target = change_string2, args = ("Nam", lock))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(f"variable :  {variable}")