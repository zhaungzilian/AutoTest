import xlrd
#通过索引顺序获取
xlrds = xlrd.open_workbook("test.xlsx")

#三种读取表内容
# sheet = xlrds.sheets()[0]  #通过索引顺序获取
# sheet3 = xlrds.sheet_by_name(u'Sheet1')  # 通过名称获取
sheet1 = xlrds.sheet_by_index(0)  #通过索引顺序获取


#行数
print(sheet1.nrows)
#列数
print(sheet1.ncols)

#写入
row = "广东"
col = "汕头"
ctype = 1
value = '单元格的值'
xf = 0 # 扩展的格式化

# sheet1.put_cell(row,col,ctype,value,xf)

#读取全部内容
for i in range(sheet1.nrows):
    print(sheet1.row_values(i))