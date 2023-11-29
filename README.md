# Web-urls 🕸️

![Spider](https://img.shields.io/badge/spider-web%20crawler-green)

Web-urls是一个Python脚本，允许你输入访问指定网页，提取其中的所有 URL，并将结果导出到 Excel 文件中。

## 功能特性

- 🕷️ 访问指定 URL，提取所有链接
- 🔄 使用多线程处理 URL，并获取网页标题
- 📊 将结果导出到 Excel 文件中，包含序号、URL、网页标题和域名

## 使用方法

1. 使用终端运行代码。
2. 输入要访问的目标 URL。
3. 脚本将使用 Edge 浏览器请求头访问网页（可自行修改）。
4. 所有提取到的 URL 将会在 Excel 文件中保存。

```
bashCopy code
python weburls.py
```

## 注意事项

- 请确保你有足够的网络访问权限。
- 请注意网站的使用政策和 robots.txt。
- 如果出现访问超时或其他异常，请检查网络连接并重试。
- 设置线程部分请根据运行情况调整，过高的线程无法正常获取标题。

## 意外情况

❓代码以及导出的Excel中提示字符含有中文，若您的计算机不支持简体中文，请自行修改代码中的字符。

❓导出的Excel中的序号不会自然排序，请自行调整，若您有解决办法，请反馈给我，谢谢。

## 作者

- [Cairns](https://github.com/cairns666)

🚀 感谢使用我的 Web 数据爬取工具！使用代码请遵守开源守则，欢迎提出建议和贡献代码。



*****



# Web-urls

Web-urls is a Python script that allows you to input a specified webpage, extract all URLs from it, and export the results to an Excel file.

## Features

- 🕷️ Visit a specified URL and extract all links
- 🔄 Process URLs using multiple threads and fetch webpage titles
- 📊 Export results to an Excel file, including index, URL, webpage title, and domain

## Usage

1. Run the code using the terminal.
2. Enter the target URL you want to visit.
3. The script will access the webpage using the Edge browser request header (modifiable).
4. All extracted URLs will be saved in an Excel file.

```
bash
python weburls.py
```



## Notes

- Ensure you have sufficient network access.
- Be mindful of the website's usage policies and robots.txt.
- In case of timeouts or other issues, check your network connection and retry.

## Caveats

❓ The code and exported Excel may contain Chinese characters. If your computer does not support Simplified Chinese, feel free to modify the characters in the code.

❓ The index in the exported Excel may not be naturally sorted. Adjust it manually, and if you have a solution, please provide feedback. Thank you!

## Author

- [Cairns](https://github.com/cairns666)

🚀 Thank you for using my Web data crawling tool! Adhere to open-source principles when using the code.Suggestions and code contributions are welcome.
