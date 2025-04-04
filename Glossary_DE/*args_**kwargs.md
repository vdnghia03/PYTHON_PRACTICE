# Tham số *args and **kwargs
---

### 1. `*args` - Tham số vị trí không xác định (Arbitrary Positional Arguments)
- **Ý nghĩa:** `*args` cho phép một hàm nhận một số lượng **tham số vị trí** bất kỳ (tức là các tham số được truyền vào theo thứ tự, không cần khai báo tên). Tên `args` chỉ là quy ước, bạn có thể đặt tên khác, nhưng dấu `*` là bắt buộc.
- **Cách hoạt động:** Khi bạn dùng `*args` trong định nghĩa hàm, Python sẽ thu thập tất cả các tham số vị trí dư thừa (không được khai báo cụ thể) vào một **tuple**.
- **Mục đích:** Dùng khi bạn không biết trước hàm sẽ nhận bao nhiêu tham số hoặc muốn hàm linh hoạt hơn.

#### Ví dụ cơ bản:
```python
def print_numbers(*args):
    print("args là:", args)
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)
# Output:
# args là: (1, 2, 3, 4)
# 1
# 2
# 3
# 4
```

- **Giải thích:** 
  - Hàm `print_numbers` không khai báo tham số cụ thể nào, nhưng nhờ `*args`, nó nhận được tất cả các giá trị `1, 2, 3, 4` dưới dạng một tuple `(1, 2, 3, 4)`.
  - Vòng lặp `for` duyệt qua tuple để in từng phần tử.

#### Ví dụ kết hợp với tham số cố định:
```python
def greet(greeting, *args):
    for name in args:
        print(f"{greeting}, {name}!")

greet("Xin chào", "Alice", "Bob", "Charlie")
# Output:
# Xin chào, Alice!
# Xin chào, Bob!
# Xin chào, Charlie!
```

- **Giải thích:** 
  - `greeting` là tham số cố định, nhận giá trị `"Xin chào"`.
  - `*args` thu thập các tham số còn lại (`"Alice", "Bob", "Charlie"`) thành tuple.

#### Ứng dụng trong Decorator:
```python
def my_decorator(func):
    def wrapper(*args):
        print("Trước khi gọi hàm...")
        func(*args)
        print("Sau khi gọi hàm...")
    return wrapper

@my_decorator
def say_hello(name, age):
    print(f"Xin chào {name}, bạn {age} tuổi!")

say_hello("Alice", 25)
# Output:
# Trước khi gọi hàm...
# Xin chào Alice, bạn 25 tuổi!
# Sau khi gọi hàm...
```

- **Giải thích:** 
  - `*args` trong `wrapper` cho phép decorator xử lý bất kỳ số lượng tham số nào mà hàm gốc (`say_hello`) nhận.
  - Khi gọi `say_hello("Alice", 25)`, `*args` trở thành `("Alice", 25)` và được truyền lại vào `func`.

---

### 2. `**kwargs` - Tham số từ khóa không xác định (Arbitrary Keyword Arguments)
- **Ý nghĩa:** `**kwargs` cho phép một hàm nhận một số lượng **tham số từ khóa** bất kỳ (tức là các tham số được truyền vào dưới dạng `tên=giá trị`). Tên `kwargs` là quy ước, nhưng dấu `**` là bắt buộc.
- **Cách hoạt động:** Khi dùng `**kwargs`, Python thu thập tất cả các tham số từ khóa dư thừa vào một **dictionary**.
- **Mục đích:** Dùng khi bạn muốn hàm linh hoạt với các tham số có tên mà không cần khai báo trước.

#### Ví dụ cơ bản:
```python
def print_info(**kwargs):
    print("kwargs là:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Hanoi")
# Output:
# kwargs là: {'name': 'Alice', 'age': 25, 'city': 'Hanoi'}
# name: Alice
# age: 25
# city: Hanoi
```

- **Giải thích:** 
  - Hàm `print_info` nhận các tham số từ khóa và lưu chúng vào `kwargs` dưới dạng dictionary.
  - Vòng lặp `for` duyệt qua dictionary để in từng cặp key-value.

#### Ví dụ kết hợp với tham số cố định:
```python
def introduce(greeting, **kwargs):
    print(f"{greeting}, tôi là {kwargs.get('name', 'không tên')}!")
    if "age" in kwargs:
        print(f"Tôi {kwargs['age']} tuổi.")

introduce("Xin chào", name="Bob", age=30)
# Output:
# Xin chào, tôi là Bob!
# Tôi 30 tuổi.
```

- **Giải thích:** 
  - `greeting` là tham số cố định.
  - `**kwargs` thu thập `name="Bob"` và `age=30` vào dictionary.

#### Ứng dụng trong Decorator:
```python
def my_decorator(func):
    def wrapper(**kwargs):
        print("Trước khi gọi hàm...")
        func(**kwargs)
        print("Sau khi gọi hàm...")
    return wrapper

@my_decorator
def describe_person(name, age):
    print(f"{name} là {age} tuổi.")

describe_person(name="Alice", age=25)
# Output:
# Trước khi gọi hàm...
# Alice là 25 tuổi.
# Sau khi gọi hàm...
```

- **Giải thích:** 
  - `**kwargs` trong `wrapper` thu thập các tham số từ khóa (`name="Alice", age=25`) thành dictionary.
  - `func(**kwargs)` giải nén dictionary để truyền lại vào hàm gốc.

---

### 3. Kết hợp `*args` và `**kwargs`
- **Ý nghĩa:** Khi dùng cả hai, bạn có thể xử lý cả tham số vị trí và từ khóa trong cùng một hàm.
- **Thứ tự:** `*args` phải đứng trước `**kwargs` trong định nghĩa hàm.

#### Ví dụ:
```python
def show_details(*args, **kwargs):
    print("Tham số vị trí:", args)
    print("Tham số từ khóa:", kwargs)

show_details(1, 2, 3, name="Alice", age=25)
# Output:
# Tham số vị trí: (1, 2, 3)
# Tham số từ khóa: {'name': 'Alice', 'age': 25}
```

- **Giải thích:** 
  - `args` nhận `(1, 2, 3)` dưới dạng tuple.
  - `kwargs` nhận `{'name': 'Alice', 'age': 25}` dưới dạng dictionary.

#### Ứng dụng trong Decorator:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Trước khi gọi hàm...")
        result = func(*args, **kwargs)
        print("Sau khi gọi hàm...")
        return result
    return wrapper

@my_decorator
def introduce(greeting, name, age=0):
    return f"{greeting}, tôi là {name}, {age} tuổi!"

print(introduce("Xin chào", "Bob", age=30))
# Output:
# Trước khi gọi hàm...
# Sau khi gọi hàm...
# Xin chào, tôi là Bob, 30 tuổi!
```

- **Giải thích:** 
  - `*args` nhận `"Xin chào", "Bob"`.
  - `**kwargs` nhận `age=30`.
  - `func(*args, **kwargs)` truyền cả hai loại tham số vào hàm gốc.

---

### 4. Khi nào dùng `*args` và `**kwargs`?
- **`*args`:** Khi bạn cần xử lý một danh sách tham số không xác định theo thứ tự (ví dụ: danh sách số, tên).
- **`**kwargs`:** Khi bạn cần xử lý các tham số có tên (ví dụ: thông tin cấu hình, thuộc tính).
- **Kết hợp:** Khi hàm cần linh hoạt tối đa, đặc biệt trong decorators, để tương thích với mọi loại hàm gốc.

---

### 5. Lưu ý quan trọng
- **Truyền lại tham số:** Khi dùng trong decorator, bạn phải truyền `*args` và `**kwargs` từ `wrapper` sang `func` để hàm gốc nhận đúng giá trị.
- **Tên không quan trọng:** Bạn có thể thay `args` bằng `numbers` hoặc `kwargs` bằng `options`, miễn là giữ `*` và `**`.
  ```python
  def example(*numbers, **options):
      print(numbers, options)
  ```

Hy vọng giải thích này giúp bạn hiểu rõ `*args` và `**kwargs`! Nếu bạn muốn thêm ví dụ hoặc ứng dụng cụ thể hơn, cứ nói nhé!
