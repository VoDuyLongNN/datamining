import pandas as pd
sDay = pd.Series(["1/3","2/3","3/3","4/3","5/3","6/3","7/3"])
sGoldSellCoin = pd.Series([46,47,45,46,46,46,45])
sGoldBuyCoin = pd.Series([45,46,45.5,44.5,45,45.5,44.5])

data = {"Ngay":sDay, "Gia vang ban ra":sGoldSellCoin, "Gia vang mua vao":sGoldBuyCoin}
df = pd.DataFrame(data)
print(df)
df.to_csv("lab1\giavang.csv")
