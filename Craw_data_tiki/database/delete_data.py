from mysql_manager import MySQLService
import os
from dotenv import load_dotenv


# Load cấu hình từ file .env
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
# Load biến môi trường
load_dotenv(env_path)

MYSQL_CONFIG = {
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "host": "127.0.0.1", #os.getenv("MYSQL_HOST"),
    "port": os.getenv("MYSQL_PORT"),
    "database": os.getenv("MYSQL_DATABASE")
}


if __name__ == "__main__":
    

    try:
        with MySQLService(MYSQL_CONFIG) as db:
            # Xóa dữ liệu trong bảng products có id = 1 và id = 2
            condition = "id IN (1, 2)"
            db.delete_data("products", condition)
    except Exception as e:
        print(f"ERROR: {e}")




