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
    - Loi khuyen: Nen co them dong my_thread.join() de cap nhat duoc cac gia tri thay doi vao Main thread.

- Các thread chạy concurent và không bị giới hạn, có bao nhiêu thread củng được miễn là đủ bộ nhớ.

- Hiểu về process: Các thread được virtual enviroment biên dịch tạo ra một môi trường chung hoạt động, miễn là đủ bộ nhớ. Với process nó lại phụ thuộc vào số core CPU máy, mỗi core sử lí 1 process, có 1 gui hoạt xử lí riêng. Từ python 3.7 trở đi có thể trao đổi thông tin dữ liệu qua giữa các process. CPU 16 core tạo tối đa 16 process, với mỗi process tạo bao nhiêu thread đều được vì nó phụ thuộc bộ nhớ. Với nhiều process, nó sẽ phân chia bộ nhớ hợp lí cho từng process, bộ nhớ trong mỗi process lại chia ra cho các thread trên từng process.

- Một số ứng dụng của thread: Download sử dụng thread, chia nhiều màn hình camera,....

## 2. Một số vấn đề cần giải quyết

- Vấn đề Race condition: Việc sử dụng các thread chạy đồng thời để thay đổi giá trị cho biến toàn cục, vì các thread chạy đồng thời nên ta sẽ không thể kiểm soát được nó sẽ được cập nhật ở thread nào
    + Giải quyết: Sử dụng Lock()


