DECORATOR PYTHON BASIC
---

### Giai đoạn 1: Nền tảng cơ bản về hàm trong Python

#### 1. Python Functions (Hàm trong Python)
- **Mô tả:** Học cách định nghĩa và sử dụng hàm cơ bản.
- **Ví dụ:**
  ```python
  def greet(name):
      return f"Xin chào, {name}!"

  print(greet("Alice"))  # Output: Xin chào, Alice!
  print(greet("Bob"))    # Output: Xin chào, Bob!
  ```
- **Giải thích:** Hàm `greet` nhận tham số `name` và trả về một chuỗi. Đây là cách cơ bản để định nghĩa hàm.

#### 2. First-Class Objects (Hàm là đối tượng hạng nhất)
- **Mô tả:** Hiểu rằng hàm có thể được gán cho biến hoặc truyền như tham số.
- **Ví dụ:**
  ```python
  def say_hello():
      print("Hello!")

  # Gán hàm cho biến
  talk = say_hello
  talk()  # Output: Hello!

  # Truyền hàm làm tham số
  def execute(func):
      func()

  execute(say_hello)  # Output: Hello!
  ```
- **Giải thích:** Hàm `say_hello` được gán cho biến `talk` và truyền vào hàm `execute`, chứng minh hàm là "first-class object".

#### 3. Inner Functions (Hàm lồng nhau)
- **Mô tả:** Định nghĩa hàm bên trong một hàm khác.
- **Ví dụ:**
  ```python
  def outer_function():
      def inner_function():
          print("Tôi là hàm bên trong!")
      inner_function()

  outer_function()  # Output: Tôi là hàm bên trong!
  ```
- **Giải thích:** Hàm `inner_function` chỉ tồn tại trong phạm vi của `outer_function` và được gọi bên trong nó.

#### 4. Functions as Return Values (Hàm làm giá trị trả về)
- **Mô tả:** Một hàm có thể trả về một hàm khác.
- **Ví dụ:**
  ```python
  def get_multiplier(factor):
      def multiplier(number):
          return number * factor
      return multiplier

  double = get_multiplier(2)
  triple = get_multiplier(3)

  print(double(5))  # Output: 10
  print(triple(5))  # Output: 15
  ```
- **Giải thích:** `get_multiplier` trả về hàm `multiplier`, được gán cho `double` và `triple` để nhân số với các hệ số khác nhau.

---

### Giai đoạn 2: Nhập môn Decorators

#### 5. Simple Decorators in Python (Decorators đơn giản)
- **Mô tả:** Tạo một decorator cơ bản bọc quanh hàm.
- **Ví dụ:**
  ```python
  def my_decorator(func):
      def wrapper():
          print("Trước khi hàm chạy...")
          func()
          print("Sau khi hàm chạy...")
      return wrapper

  def say_hello():
      print("Xin chào!")

  say_hello = my_decorator(say_hello)
  say_hello()
  # Output:
  # Trước khi hàm chạy...
  # Xin chào!
  # Sau khi hàm chạy...
  ```
- **Giải thích:** `my_decorator` nhận hàm `say_hello`, bọc nó trong `wrapper` để thêm hành vi trước và sau khi gọi.

#### 6. Adding Syntactic Sugar (Cú pháp @)
- **Mô tả:** Sử dụng cú pháp `@` thay vì gán thủ công.
- **Ví dụ:**
  ```python
  def my_decorator(func):
      def wrapper():
          print("Trước khi hàm chạy...")
          func()
          print("Sau khi hàm chạy...")
      return wrapper

  @my_decorator
  def say_hello():
      print("Xin chào!")

  say_hello()
  # Output giống trên
  ```
- **Giải thích:** `@my_decorator` tự động áp dụng decorator lên `say_hello`, ngắn gọn và dễ đọc hơn.

---

### Giai đoạn 3: Mở rộng Decorators

#### 7. Decorating Functions With Arguments (Decorators với hàm có tham số)
- **Mô tả:** Xử lý hàm có tham số bằng `*args` và `**kwargs`.
- **Ví dụ:**
  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print("Trước khi hàm chạy...")
          func(*args, **kwargs)
          print("Sau khi hàm chạy...")
      return wrapper

  @my_decorator
  def greet(name, greeting="Hello"):
      print(f"{greeting}, {name}!")

  greet("Alice")         # Output: Trước... Hello, Alice! Sau...
  greet("Bob", "Hi")     # Output: Trước... Hi, Bob! Sau...
  ```
- **Giải thích:** `wrapper` dùng `*args` và `**kwargs` để linh hoạt truyền tham số vào hàm gốc.

#### 8. Returning Values From Decorated Functions (Trả về giá trị từ hàm được decorate)
- **Mô tả:** Đảm bảo decorator giữ giá trị trả về của hàm.
- **Ví dụ:**
  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print("Trước...")
          result = func(*args, **kwargs)
          print("Sau...")
          return result
      return wrapper

  @my_decorator
  def add(a, b):
      return a + b

  result = add(3, 5)
  print(result)
  # Output:
  # Trước...
  # Sau...
  # 8
  ```
- **Giải thích:** `wrapper` lưu kết quả của `func` vào `result` và trả về nó.

---

### Giai đoạn 4: Ứng dụng thực tế

#### 9. Timing Functions (Đo thời gian thực thi)
- **Mô tả:** Dùng decorator để đo thời gian chạy của hàm.
- **Ví dụ:**
  ```python
  import time

  def timer(func):
      def wrapper(*args, **kwargs):
          start = time.time()
          result = func(*args, **kwargs)
          end = time.time()
          print(f"{func.__name__} chạy trong {end - start:.4f} giây")
          return result
      return wrapper

  @timer
  def waste_time():
      time.sleep(1.5)

  waste_time()
  # Output: waste_time chạy trong 1.5023 giây (thời gian thực tế có thể khác)
  ```
- **Giải thích:** `timer` đo thời gian trước và sau khi gọi hàm, rồi in ra.

#### 10. Debugging Code (Gỡ lỗi)
- **Mô tả:** In thông tin đầu vào và kết quả của hàm.
- **Ví dụ:**
  ```python
  def debug(func):
      def wrapper(*args, **kwargs):
          print(f"Gọi {func.__name__} với args={args}, kwargs={kwargs}")
          result = func(*args, **kwargs)
          print(f"Kết quả: {result}")
          return result
      return wrapper

  @debug
  def multiply(a, b=2):
      return a * b

  multiply(3)      # Output: Gọi multiply với args=(3,), kwargs={} / Kết quả: 6
  multiply(4, 5)   # Output: Gọi multiply với args=(4, 5), kwargs={} / Kết quả: 20
  ```
- **Giải thích:** `debug` giúp theo dõi tham số và kết quả, hữu ích khi gỡ lỗi.

#### 11. Slowing Down Code (Làm chậm mã)
- **Mô tả:** Thêm độ trễ để kiểm tra hoặc mô phỏng.
- **Ví dụ:**
  ```python
  import time

  def slow_down(func):
      def wrapper(*args, **kwargs):
          time.sleep(1)
          return func(*args, **kwargs)
      return wrapper

  @slow_down
  def countdown(n):
      print(f"Đếm ngược từ {n}")
      return n - 1

  print(countdown(5))  # Chậm 1 giây, Output: Đếm ngược từ 5 / 4
  ```
- **Giải thích:** `slow_down` thêm độ trễ 1 giây trước khi gọi hàm.

---

### Giai đoạn 5: Nâng cao Decorators

#### 12. Reusing Decorators (Tái sử dụng)
- **Mô tả:** Lưu decorator trong module để dùng lại.
- **Ví dụ:** Tạo file `decorators.py`:
  ```python
  # decorators.py
  def log(func):
      def wrapper(*args, **kwargs):
          print(f"Chạy {func.__name__}")
          return func(*args, **kwargs)
      return wrapper
  ```
  Rồi dùng trong file khác:
  ```python
  # main.py
  from decorators import log

  @log
  def say_hi():
      print("Hi!")

  say_hi()  # Output: Chạy say_hi / Hi!
  ```
- **Giải thích:** Tách decorator ra module để tái sử dụng dễ dàng.

#### 13. Nesting Decorators (Xếp chồng decorators)
- **Mô tả:** Áp dụng nhiều decorator lên một hàm.
- **Ví dụ:**
  ```python
  def deco1(func):
      def wrapper():
          print("Decorator 1")
          func()
      return wrapper

  def deco2(func):
      def wrapper():
          print("Decorator 2")
          func()
      return wrapper

  @deco1
  @deco2
  def say():
      print("Xin chào!")

  say()
  # Output:
  # Decorator 1
  # Decorator 2
  # Xin chào!
  ```
- **Giải thích:** Decorator áp dụng từ dưới lên (`deco2` rồi `deco1`).

#### 14. Defining Decorators With Arguments (Decorators có tham số)
- **Mô tả:** Thêm tham số vào decorator bằng cách bọc thêm một lớp hàm.
- **Ví dụ:**
  ```python
  def repeat(n):
      def decorator(func):
          def wrapper(*args, **kwargs):
              for _ in range(n):
                  func(*args, **kwargs)
          return wrapper
      return decorator

  @repeat(3)
  def cheer(name):
      print(f"Hooray, {name}!")

  cheer("Alice")
  # Output:
  # Hooray, Alice!
  # Hooray, Alice!
  # Hooray, Alice!
  ```
- **Giải thích:** `repeat` nhận tham số `n` và lặp lại hàm `n` lần.

#### 15. Using Classes as Decorators (Dùng class làm decorator)
- **Mô tả:** Dùng class với phương thức `__call__` làm decorator.
- **Ví dụ:**
  ```python
  class MyDecorator:
      def __init__(self, func):
          self.func = func

      def __call__(self, *args, **kwargs):
          print("Trước khi gọi...")
          self.func(*args, **kwargs)
          print("Sau khi gọi...")

  @MyDecorator
  def greet(name):
      print(f"Xin chào, {name}!")

  greet("Bob")
  # Output:
  # Trước khi gọi...
  # Xin chào, Bob!
  # Sau khi gọi...
  ```
- **Giải thích:** Class `MyDecorator` lưu hàm và thực thi khi được gọi.

---

### Giai đoạn 6: Thực hành và khám phá thêm

#### 16. More Real-World Examples (Ví dụ thực tế nâng cao)
- **Caching Return Values (Lưu trữ kết quả):**
  ```python
  def memoize(func):
      cache = {}
      def wrapper(*args):
          if args not in cache:
              cache[args] = func(*args)
          return cache[args]
      return wrapper

  @memoize
  def fibonacci(n):
      if n < 2:
          return n
      return fibonacci(n-1) + fibonacci(n-2)

  print(fibonacci(10))  # Output: 55 (tính nhanh hơn nhờ cache)
  ```
- **Validating JSON (Kiểm tra JSON):**
  ```python
  def validate_json(required_keys):
      def decorator(func):
          def wrapper(data):
              if not all(key in data for key in required_keys):
                  raise ValueError("Thiếu key bắt buộc!")
              return func(data)
          return wrapper
      return decorator

  @validate_json(["name", "age"])
  def process_data(data):
      print(f"Xử lý: {data}")

  process_data({"name": "Alice", "age": 25})  # Output: Xử lý: {'name': 'Alice', 'age': 25}
  # process_data({"name": "Bob"})  # Lỗi: Thiếu key bắt buộc!
  ```

#### 17. Conclusion & Further Reading
- Ôn lại các khái niệm: hàm lồng nhau, `@`, tham số, ứng dụng thực tế.
- Tài liệu đề xuất: Python Docs (`functools`), bài "Decorators" trên Real Python.

---

### Gợi ý thực hành
- Thử thay đổi các ví dụ: thêm tham số, kết hợp nhiều decorator.
- Viết decorator riêng cho dự án của bạn (ví dụ: kiểm tra quyền truy cập, log lỗi).
