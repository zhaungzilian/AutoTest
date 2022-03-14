import xlrd
from datetime import date, datetime ,timedelta

# 1. 需要open到 数据表   filename
# 2. 读取数据表内容
# 3. 查询数据表
def read_xlsx(filename , index, ishead=False ): #ishead 是否有标题，默认false
    tagefile = xlrd.open_workbook(filename)
    sheet = tagefile.sheet_by_index(index)

    #把查出的数据放到数组并放回
    data = []
    for i in range(sheet.nrows):
        if i == 0:
            if ishead:
                continue

        data.append(sheet.row_values(i))

    return data


#日期数
def date_today(n):
    return str(date.today() + timedelta(days=int(n)))


if __name__ == '__main__':
    print(read_xlsx("../data/test.xlsx", 0, True))