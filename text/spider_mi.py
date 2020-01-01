from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import xlwt

def spider(urls):
    ##开启一个excel输入流
    workbook = xlwt.Workbook(encoding='utf-8')

    ##添加一张工作表
    sheet = workbook.add_sheet("test")
    count = 0
    for url in urls:

        ##在自己的地址上开启Chrome驱动器，不同电脑位置不同
        chrome_driver = "D:\大数据2019\\text1\\venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

        ##打开浏览器，获取网页源代码
        browser = webdriver.Chrome(executable_path=chrome_driver)
        browser.get(url)
        js = "var q=document.documentElement.scrollTop=10000000"
        browser.execute_script(js)
        sleep(1)
        html = browser.page_source
        browser.close()

        ##截取<p></p>标签的pro-info类的内容
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        names = soup.find_all('p', class_='pro-info')

        ##输入excel
        for name in names:
            name_str = str(name.get_text())
            sheet.write(count, 0, name_str)
            count = count + 1

    ##保存excel
    workbook.save('./youpin_list.xls')