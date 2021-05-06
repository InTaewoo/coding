import pyupbit
import numpy as np
#OHLCV(open, high,low,close,volume)로 당일시가, 고가,저가,종가,거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC",count=7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")
