# from sqlalchemy import create_engine



# def connect_db(config):
#     conn_info = (
#         f"mysql+pymysql://{config['user']}:{config['password']}" + f"@{config['host']}:{config['port']}" + f"/{config['database']}"
#     )

#     db_conn = create_engine

#     try:
#         yield db_conn
#     except Exception:
#         raise


# class mysql_service():
#     def __init__(self, config):
#         connect 


from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

class MySQLService:
    def __init__(self, config):
        """Khởi tạo kết nối tới MySQL với config cung cấp."""
        self.conn_info = (
            f"mysql+pymysql://{config['user']}:{config['password']}"
            f"@{config['host']}:{config['port']}/{config['database']}"
        )
        self.engine = None
        self.connect()

    def connect(self):
        """Tạo kết nối tới MySQL."""
        try:
            self.engine = create_engine(self.conn_info, pool_size=5, pool_recycle=3600)
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Kết nối MySQL thành công!")
        except SQLAlchemyError as e:
            raise Exception(f"Lỗi khi kết nối tới MySQL: {str(e)}")

    def create_table(self, table_name, schema):
        """Tạo bảng trong MySQL với schema cung cấp."""
        try:
            with self.engine.connect() as connection:
                connection.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
                connection.execute(text(f"CREATE TABLE {table_name} ({schema})"))
                connection.commit()
            print(f"Tạo bảng {table_name} thành công!")
        except SQLAlchemyError as e:
            raise Exception(f"Lỗi khi tạo bảng {table_name}: {str(e)}")

    def insert_data(self, table_name, data):
        """Chèn dữ liệu vào bảng."""
        try:
            with self.engine.connect() as connection:
                columns = ", ".join(data.keys())
                values = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in data.values()])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
                connection.execute(text(query))
                connection.commit()
            print(f"Chèn dữ liệu vào bảng {table_name} thành công!")
        except SQLAlchemyError as e:
            raise Exception(f"Lỗi khi chèn dữ liệu vào bảng {table_name}: {str(e)}")

    def __enter__(self):
        """Hỗ trợ sử dụng với context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Đóng kết nối khi thoát context manager."""
        if self.engine:
            self.engine.dispose()
            print("Đã đóng toàn bộ kết nối MySQL và giải phóng engine.")
            self.engine = None

# Ví dụ sử dụng
if __name__ == "__main__":
    config = {
        "user": "your_username",
        "password": "your_password",
        "host": "localhost",
        "port": "3306",
        "database": "your_database"
    }

    try:
        with MySQLService(config) as db:
            schema = """
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
            """
            db.create_table("users", schema)
            data = {"name": "Nguyen Van A", "age": 25}
            db.insert_data("users", data)
    except Exception as e:
        print(f"Lỗi: {str(e)}")