# MULTI THREADING

## 1. Thư viện Threading

- Trong một chương trình Python, luôn có MainThreading
- Sử dụng thư viện Threading tạo ra được các thread phụ khác
- Thread(target, args, daemon)
    - target: task cần thực thi
    - args: đối số của task
    - deamon: chạy ngầm, khi Main chạy xong thì main nó xóa đi các thread chạy ngầm
- Các thread trong chương trình thực thi đồng thời - concurrent, tùy vào task từng thread mà có thời gian thực thi khác nhau
- 
