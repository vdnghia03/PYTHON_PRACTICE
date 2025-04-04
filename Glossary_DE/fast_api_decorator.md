
# FAST API DECORATOR

Trong **FastAPI**, decorators là một công cụ mạnh mẽ của Python được sử dụng để mở rộng hoặc thay đổi hành vi của các hàm hoặc phương thức mà không cần sửa đổi trực tiếp mã nguồn của chúng. FastAPI tận dụng decorators một cách tự nhiên để định nghĩa các tuyến đường (routes), xử lý logic bổ sung, và tích hợp các tính năng như xác thực, kiểm tra quyền, hoặc đo lường hiệu suất. Dưới đây là các ứng dụng chính của decorators trong FastAPI

---

### 1. **Định nghĩa các tuyến đường (Path Operation Decorators)**
FastAPI sử dụng các decorators như `@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()`, v.v. để định nghĩa các tuyến đường API và chỉ định phương thức HTTP tương ứng.

#### Ví dụ:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Xin chào FastAPI!"}

@app.post("/items/")
def create_item(name: str):
    return {"item_name": name}
```
- **Giải thích:** 
  - `@app.get("/")` chỉ định rằng hàm `read_root` xử lý yêu cầu GET tới đường dẫn `/`.
  - `@app.post("/items/")` chỉ định rằng hàm `create_item` xử lý yêu cầu POST tới `/items/`.

---

### 2. **Xác thực và phân quyền (Authentication & Authorization)**
Decorators có thể được dùng để kiểm tra quyền truy cập hoặc xác thực người dùng trước khi thực thi logic của tuyến đường.

#### Ví dụ:
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

def require_auth(func):
    async def wrapper(token: str, *args, **kwargs):
        if token != "secret-token":
            raise HTTPException(status_code=401, detail="Không được phép truy cập")
        return await func(*args, **kwargs)
    return wrapper

@app.get("/secure")
@require_auth
async def secure_route(token: str):
    return {"message": "Bạn đã truy cập vào tuyến đường bảo mật!"}
```
- **Giải thích:** 
  - Decorator `require_auth` kiểm tra `token` trước khi cho phép truy cập vào `secure_route`.
  - Nếu token không đúng, nó ném ra ngoại lệ HTTP 401.

---

### 3. **Đo lường hiệu suất (Timing/Performance Monitoring)**
Decorators có thể được dùng để đo thời gian thực thi của một tuyến đường, hữu ích cho việc tối ưu hóa hoặc gỡ lỗi.

#### Ví dụ:
```python
import time
from fastapi import FastAPI

app = FastAPI()

def timer(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} chạy trong {end - start:.4f} giây")
        return result
    return wrapper

@app.get("/slow")
@timer
async def slow_route():
    time.sleep(1)  # Giả lập tác vụ chậm
    return {"message": "Hoàn thành!"}
```
- **Giải thích:** 
  - Decorator `timer` đo thời gian thực thi của `slow_route` và in ra kết quả.

---

### 4. **Ghi log (Logging)**
Decorators có thể ghi lại thông tin về yêu cầu, chẳng hạn như phương thức HTTP, đường dẫn, hoặc thời gian xử lý.

#### Ví dụ:
```python
from fastapi import FastAPI, Request

app = FastAPI()

def log_request(func):
    async def wrapper(request: Request, *args, **kwargs):
        print(f"Yêu cầu: {request.method} {request.url}")
        result = await func(request, *args, **kwargs)
        print("Yêu cầu đã hoàn thành")
        return result
    return wrapper

@app.get("/log")
@log_request
async def log_route(request: Request):
    return {"message": "Đã ghi log!"}
```
- **Giải thích:** 
  - Decorator `log_request` ghi lại thông tin yêu cầu trước và sau khi thực thi `log_route`.

---

### 5. **Xử lý ngoại lệ (Exception Handling)**
Decorators có thể bọc logic xử lý ngoại lệ để trả về phản hồi tùy chỉnh khi có lỗi xảy ra.

#### Ví dụ:
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

def handle_errors(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Lỗi: {str(e)}")
    return wrapper

@app.get("/risky")
@handle_errors
async def risky_route():
    raise ValueError("Có lỗi xảy ra!")
```
- **Giải thích:** 
  - Decorator `handle_errors` bắt mọi ngoại lệ trong `risky_route` và trả về lỗi HTTP 500 với thông điệp tùy chỉnh.

---

### 6. **Giới hạn tốc độ (Rate Limiting)**
Decorators có thể được dùng để giới hạn số lượng yêu cầu từ một địa chỉ IP trong một khoảng thời gian.

#### Ví dụ:
```python
from fastapi import FastAPI, Request, HTTPException
from time import time

app = FastAPI()
rate_limit_store = {}

def rate_limit(max_calls: int, period: int):
    def decorator(func):
        async def wrapper(request: Request, *args, **kwargs):
            ip = request.client.host
            now = time()
            calls, last_reset = rate_limit_store.get(ip, (0, now))
            if now - last_reset > period:
                calls, last_reset = 0, now
            if calls >= max_calls:
                raise HTTPException(status_code=429, detail="Quá nhiều yêu cầu!")
            calls += 1
            rate_limit_store[ip] = (calls, last_reset)
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator

@app.get("/limited")
@rate_limit(max_calls=3, period=60)  # 3 yêu cầu mỗi phút
async def limited_route(request: Request):
    return {"message": "Yêu cầu thành công!"}
```
- **Giải thích:** 
  - Decorator `rate_limit` giới hạn số lượng yêu cầu từ một IP (tối đa 3 lần trong 60 giây).

---

### 7. **Tái sử dụng logic chung (Reusing Common Logic)**
Decorators giúp tránh lặp lại mã bằng cách đóng gói logic chung, chẳng hạn như kiểm tra đầu vào hoặc định dạng đầu ra.

#### Ví dụ:
```python
from fastapi import FastAPI

app = FastAPI()

def uppercase_output(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        return {k: v.upper() if isinstance(v, str) else v for k, v in result.items()}
    return wrapper

@app.get("/upper")
@uppercase_output
async def upper_route():
    return {"message": "xin chào", "status": "ok"}
```
- **Giải thích:** 
  - Decorator `uppercase_output` chuyển tất cả giá trị chuỗi trong phản hồi thành chữ in hoa.

---

### 8. **Tích hợp với Dependencies của FastAPI**
Decorators có thể kết hợp với hệ thống `Depends` của FastAPI để tận dụng các phụ thuộc (dependencies).

#### Ví dụ:
```python
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

async def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=403, detail="Không có quyền")
    return {"user_id": user_id}

def require_user(func):
    async def wrapper(current_user=Depends(get_user), *args, **kwargs):
        return await func(current_user, *args, **kwargs)
    return wrapper

@app.get("/user-only")
@require_user
async def user_route(current_user: dict):
    return {"message": f"Chào mừng user {current_user['user_id']}"}
```
- **Giải thích:** 
  - Decorator `require_user` sử dụng `Depends` để kiểm tra người dùng trước khi thực thi `user_route`.

---

### Lợi ích của việc dùng Decorators trong FastAPI
- **Tái sử dụng mã:** Giảm lặp lại logic chung.
- **Tách biệt logic:** Giữ mã tuyến đường sạch sẽ, dễ đọc.
- **Linh hoạt:** Dễ dàng thêm hoặc thay đổi hành vi mà không sửa đổi hàm gốc.
- **Tích hợp tốt:** Kết hợp với các tính năng của FastAPI như `Depends`, `Request`, v.v.
