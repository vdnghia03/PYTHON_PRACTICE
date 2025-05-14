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
    

    data = [
        ("1", "brand1", "category1", "price1", "title1", "review1", "rating1", "image_link1", "product_link1", "from_page_link1"),
        ("2", "brand2", "category2", "price2", "title2", "review2", "rating2", "image_link2", "product_link2", "from_page_link2")
    ]

    try:
        with MySQLService(MYSQL_CONFIG) as db:
            # Tạo bảng products
            columns_name = "id, brand, category, price, title, review, rating, image_link, product_link, from_page_link"
            db.insert_data("products", columns_name, data)
            
    except Exception as e:
        print(f"ERROR: {e}")




