import pandas
# đọc và hiển thị bảng giá vàng từ bài 1
print("Bảng Giá Vàng")
dfGiaVang = pandas.read_csv('lab1\giavang.csv', index_col=0)
print(dfGiaVang)

# đọc và hiển thị bảng điểm danh từ bài 2
print("\n\nBảng điểm danh")
dfDiemDanh = pandas.read_excel('lab1\diemdanh.xlsx', index_col=0)
print(dfDiemDanh)

# Lọc những sinh viên không nộp bài
print("\n\nSinh viên không nộp bài")
filterNoSubmit = dfDiemDanh[(dfDiemDanh['Khong nop bai'] > 0)]
print(filterNoSubmit)

# Lọc những sinh viên vắng cả lý thuyết và thực hành
print("\n\nSinh viên vắng cả lý thuyết và thực hành")
filterMissTheoryAndPractice = dfDiemDanh[(dfDiemDanh['Vang ly thuyet'] > 0) & (dfDiemDanh['Vang thuc hanh'] > 0)]
print(filterMissTheoryAndPractice)