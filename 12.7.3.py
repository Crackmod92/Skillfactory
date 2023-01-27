per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
deposit = []
deposit.append(money * per_cent['ТКБ'] / 100)
deposit.append(money * per_cent['СКБ'] / 100)
deposit.append(money * per_cent['ВТБ'] / 100)
deposit.append(money * per_cent['СБЕР'] / 100)
print(deposit)
print("Максимальная прибыль с вклада: =", max(deposit))
