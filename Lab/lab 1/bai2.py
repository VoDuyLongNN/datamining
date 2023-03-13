import pandas 
sName = pandas.Series(["Trung","Canh","Bao","Quoc","Tung"])
sMissTheory = pandas.Series([3,5,1,0,2])
sMissPractice = pandas.Series([2,1,0,0,1])
sNotSubmit = pandas.Series([0,3,0,2,1])

data = {"Ho ten":sName, "Vang ly thuyet":sMissTheory, "Vang thuc hanh":sMissPractice, "Khong nop bai":sNotSubmit}

df = pandas.DataFrame(data)

df.to_excel("lab1\diemdanh.xlsx")
