from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class MySQLService:
    def __init__(self, config):
        """Khởi tạo kết nối tới MySQL với config cung cấp."""
        self.conn_info = (
            f"mysql+pymysql://{config['user']}:{config['password']}"
            f"@{config['host']}:{config.get('port', '3306')}/{config['database']}"
        )
        self.engine = None
        self.connect()

    def connect(self):
        """Tạo kết nối tới MySQL."""
        try:
            self.engine = create_engine(self.conn_info, pool_size=5, pool_recycle=3600)
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Connect Mysql Sucessfull!")
        except SQLAlchemyError as e:
            raise Exception(f"ERROR Connect MySQL: {str(e)}")

    def create_table(self, schema):
        """Tạo bảng trong MySQL với schema SQL đầy đủ."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text(schema))
            print("Create table Success!")
        except SQLAlchemyError as e:
            raise Exception(f"ERROR Create table: {str(e)}")

    def insert_data(self, table_name, columns_name, data):
        """Chèn nhiều bản ghi vào bảng từ list các tuple."""
        if not data:
            print("Không có dữ liệu để chèn.")
            return

        try:
            with self.engine.connect() as connection:
                # Tạo câu lệnh INSERT
                # Columns name được đưa vào 
                columns = columns_name
                placeholders = ", ".join([":%d" % i for i in range(len(data[0]))])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                # Chuẩn bị danh sách tham số
                params = [
                    {f"{i}": str(item) for i, item in enumerate(row)}
                    for row in data
                ]

                # Thực thi batch insert
                connection.execute(text(query), params)
                connection.commit()
            print(f"Chèn {len(data)} bản ghi vào bảng {table_name} thành công!")
        except SQLAlchemyError as e:
            raise Exception(f"Error when insert data to {table_name}: {str(e)}")

    def delete_data(self, table_name, condition):
        """Xóa dữ liệu trong bảng theo điều kiện."""
        try:
            with self.engine.connect() as connection:
                query = f"DELETE FROM {table_name} WHERE {condition}"
                connection.execute(text(query))
                connection.commit()
            print(f"Delete Success from  {table_name}!")
        except SQLAlchemyError as e:
            raise Exception(f"Error {table_name}: {str(e)}")

    def __enter__(self):
        """Hỗ trợ sử dụng với context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Đóng kết nối khi thoát context manager."""
        if self.engine:
            self.engine.dispose()
            print("Close Mysql Connection!")
            self.engine = None

if __name__ == "__main__":
    pass