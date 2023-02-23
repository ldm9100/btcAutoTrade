import pyupbit

access = "Ze6VOxXr0ldncCYxc0MdwNvvcuuvYGOAPwj8bFTX"          # 본인 값으로 변경
secret = "jYOOjSUhogmk7hYsCZtxTNwx3sj5qM5YYJ3rKc5F"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-FCT2"))     # KRW-XRP 조회
print(upbit.get_balance("KRW")) 