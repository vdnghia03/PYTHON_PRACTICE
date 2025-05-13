# Craw data tiki

## Xác định sơ đồ

- Sử dụng python để crawl - Xem xét việc sử dụng asyncio await hay multi threading
- Trang web: tiki.vn
- Cách crawl: Vào từng danh mục - menu page. Với mỗi menu page, cào dữ liệu có trong menu đó
- Database: Lưu dữ liệu vào mysql
- Tối ưu các tham số bằng một file yaml để điều chỉnh các tham số, các đường dẫn ....


## Các bước làm:

### Bước 1: Xác định nơi lưu trữ dữ liệu: Mysql pull từ docker

```markdown
  docker pull mysql
  docker run --name mysql_container -e MYSQL_ROOT_PASSWORD="RootAccount123" -d mysql
  docker ps
```

### Bước 2: Xác định Crawl
- Xác định được quy trình của việc crawl - từ menu đến từng page
- Xác định được các trường cần cào:
    + id
    + brand: Đây là thương hiệu của sản phẩm
    + category: Danh mục mà sản phẩm thuộc về, hiện trên trang tiki
    + price: Giá cả của sản phẩm
    + title: Là dòng mô tả sản phẩm ngắn gọn
    + review: Số lượng review cho sản phẩm
    + rating: Mức độ đánh giá 
    + image_link: Link đường dẫn của hình ảnh
    + product_link: Link dẫn đến sản phẩm
    + from_page_link: Đường dẫn của menu mà sản phẩm đó thuộc về


## Bước 3: Xây dựng git - cây thư mục

- Xây dựng một hàm main.py và các bổ trợ xung quanh nó - /parsing và /utils
- Thư mục parsing: Chứa các logic liên quan đến viec crawl trong menu( là các đề mục ví dụ như sách, hàng gia dụng,....) và logic crawl trong các phần tử trong menu(ví dụ menu sách chứa rất nhiều page mà mỗi page chứa nhiều card để ta craw)
- Thư mục utils: Bổ sung các logic và các phương thức tích hợp, thêm vào đó là xây dựng các đối tượng tham số cho dễ thống nhất việc crawl

##  Bước 4: Triển khai

---

## Các mục tiêu:

- Mục tiêu 1: Phải tạo được mysql docker và dùng dbeaver kết nối vào được

- Mục tiêu 2: Phải xây dựng được các phương thức sử dụng thao tác với mysql bằng python
    + Connect - .db_config.ini
    + CRUD - Tạo bảng init_db, insert dữ liệu vào mysql

- Mục tiêu 3: 
