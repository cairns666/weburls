import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
import openpyxl
import concurrent.futures

def welcome_message():
    print("*****************************************")
    print("*          我要允许每个人都是上帝       *")
    print("*                                       *")
    print("*                  Cairns               *")
    print("*                                       *")
    print("* 友情链接:https://github.com/cairns666 *")
    print("*                                       *")
    print("*****************************************\n")

def extract_domain(url):
    parsed_url = urlparse(url)
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.netloc
    else:
        return "null"

def extract_second_level_domain(url):
    parsed_url = urlparse(url)
    
    # 如果 URL 包含协议和 netloc，则直接提取
    if parsed_url.scheme and parsed_url.netloc:
        return parsed_url.netloc

    # 如果 URL 不包含协议，但包含 netloc，则直接提取
    elif parsed_url.netloc:
        return parsed_url.netloc

    # 如果 URL 既没有协议也没有 netloc，则返回 "null"
    return "null"

def get_webpage_title(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()  # 对于错误的响应，引发HTTPError异常
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string.strip() if soup.title else "null"
    except requests.RequestException as e:
        print(f"访问 {url} 时发生错误：{e}")
        return "null"
    except requests.Timeout:
        print(f"访问 {url} 超时")
        return "null"

def process_url(idx, url, headers):
    full_url = urlparse(url).geturl()
    title = get_webpage_title(full_url, headers)
    second_level_domain = extract_second_level_domain(full_url)
    return [idx + 1, full_url, title, second_level_domain]

def main():
    # 1. 获取用户输入的URL
    user_input_url = input("请输入要访问的URL：")

    # 添加 Edge 浏览器的请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
    }
    
    try:
        # 2. 访问网页，提取所有URL
        response = requests.get(user_input_url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        all_urls = [a['href'] for a in soup.find_all('a', href=True)]

        # 3. 处理URL并获取标题，使用多线程
        data = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            future_to_url = {executor.submit(process_url, idx, url, headers): url for idx, url in enumerate(all_urls)}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data.append(future.result())
                    print(f"Success 成功获取标题 {url}")
                except Exception as e:
                    print(f"Error processing {url}: {e}")

        # 4. 导出到Excel文件
        export_to_excel(data)

        print("爬取成功！")
    
    except requests.RequestException as e:
        print(f"爬取失败：{e}")

def export_to_excel(data):
    # 生成文件名
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"Results{timestamp}.xlsx"

    # 创建一个Excel文件
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 写入表头
    sheet.append(["序号", "URL", "网页标题", "域名"])

    # 写入数据
    for row in data:
        sheet.append(row)

    # 保存文件
    workbook.save(filename)
    print(f"数据已保存到 {filename}")

if __name__ == "__main__":
    welcome_message() 
    main()
