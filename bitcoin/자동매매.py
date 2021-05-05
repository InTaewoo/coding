import pyupbit
access = "7VLx5uJ2OgdatLbarhvxPILlxltdh8P6x0nu6Rto"          # 본인 값으로 변경
secret = "FWJmaPGspnxSJmBxWy3yHnoZfkPOFzeUJLOU9O67"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
