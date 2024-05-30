# 现有2元、3元、5元共三种面额的货币，如果需要找零99元，一共有多少种找零的方式？
for i in range(50):
    for j in range(34):
        for q in range(20):
            if i*2 + j*3 + q*5 == 99:
                print(i, j, q)

