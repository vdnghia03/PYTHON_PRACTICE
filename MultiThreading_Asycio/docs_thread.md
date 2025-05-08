# MULTI THREADING

## 1. Thư viện Threading

- Trong một chương trình Python, luôn có MainThreading
- Sử dụng thư viện Threading tạo ra được các thread phụ khác
- Thread(target, args, daemon)
    - target: task cần thực thi
    - args: đối số của task
    - deamon: chạy ngầm, khi Main chạy xong thì main nó xóa đi các thread chạy ngầm
- Các thread trong chương trình thực thi đồng thời - concurrent, tùy vào task từng thread mà có thời gian thực thi khác nhau

- Hiểu về daemon:
    - Khi đặt daemon = True, thì rõ ràng khi Main thread chạy xong nó sẽ kill cái thread phụ. Ta không muốn điều này, vì vậy ta thêm lệnh sub_thread.join(). Tưởng tượng như anh MainThread tới trước cổng rồi, tuy nhiên ảnh không được vào nhà, ảnh phải đợi sub_thread đi vào trước và sau đó Main thread mới được đi vào :))
    - Ở đây sẽ có thắc mắc, là nếu vậy thì ngay từ đầu khỏi đặt daemon luôn, chương trình vẫn sẽ thực thi xong main thread và sau đó thực thi sub_thread mới đóng chương trình, khỏi mắc công khai báo deamon rồi sau đó lại phải dùng join củng bất tiện. Tuy nhiên cần phân biệt là với việc không đặt daemon = True, thì khác nhau ở chỗ ví dụ khi main_thread đến cánh cửa, nó đi qua luôn tuy nhiên nó không đóng lại và vẫn mở cho các anh khác vào. Còn nếu mà đặt deamon = True thì anh main thread ảnh chơi xấu, ảnh đóng lại luôn. Còn dùng join thì anh main thread đến cửa rồi thì bị trói lại, đợi khi nào các anh sau qua hết thì ảnh mới được qua và đóng chương trình.

- Về anh Main Thread
    - Với việc Main Thread qua cổng, đồng nghĩa với việc dù chương trình còn thực thi hay đóng lại, việc cập nhật Main thread sẽ không còn được nữa
