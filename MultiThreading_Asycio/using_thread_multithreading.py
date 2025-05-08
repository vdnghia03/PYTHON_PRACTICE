import threading
import time


def inc_number(number):
    time.sleep(3)
    number += 1
    print(f'Number is {number}')

def dosomething(number):
    print(f'This is main thread')

# inc_number(99)

# Làm mới thread - Thread() có 3 parametter 
# gồm target-công việc muốn thực thi, 
# args-parametter của target dạng tuple, 
my_thread = threading.Thread(target = inc_number, args = (99,), daemon = True)
my_thread.start()

# my_thread.join()

dosomething(1000)

# Lấy ra current thread đang chạy
print(threading.current_thread().name)
