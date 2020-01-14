import xlwt
from project import spider

if __name__ == "__main__":
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet("test")
    count = 0
    after = spider.youp(sheet, 0, 1000, count)
    spider.youp(sheet, 100000, 120000, after)

    workbook.save('./youp_list.xls')