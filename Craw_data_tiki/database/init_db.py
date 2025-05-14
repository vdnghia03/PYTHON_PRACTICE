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
    

    # Schema cho bảng products
    schema = """
    CREATE TABLE IF NOT EXISTS products (
        id VARCHAR(255) PRIMARY KEY,
        brand VARCHAR(255),
        category TEXT(255),
        price VARCHAR(255),
        title VARCHAR(255),
        review VARCHAR(255),
        rating VARCHAR(255),
        image_link TEXT(255),
        product_link TEXT(255),
        from_page_link TEXT(255)
    )
    """

    try:
        with MySQLService(MYSQL_CONFIG) as db:
            # Tạo bảng products
            db.create_table(schema)

    except Exception as e:
        print(f"ERROR: {e}")




