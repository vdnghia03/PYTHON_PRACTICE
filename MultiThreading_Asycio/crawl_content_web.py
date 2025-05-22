import urllib.request
import os
# Using thread to download content from a URL


SAVING_DIR = "saving_file"

def download_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            
            return response.read()
    except:
        return None
    
# print(download_url("http://tiki.vn/"))

url = "https://tiki.vn/nha-sach-tiki/c8322?page=2"

def download_and_save(url, saving_dir):
    if not os.path.exists(saving_dir):
        os.makedirs(saving_dir)
    
    data = download_url(url)
    if data is None:
        print("Failed to download the URL")
        return
    
    filename = os.path.basename(url).replace("?", "_").replace("=", "_") 
    file_path = os.path.join(saving_dir, filename)
    with open(file_path, "wb") as f:
        f.write(data)

download_and_save(url, SAVING_DIR)