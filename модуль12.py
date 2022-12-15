money=(input("Введите сумму депозита "))
money=float(money)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[money*roi/100 for roi in per_cent.values ()]
print("deposit =",(deposit))
print("Максимальная сумма, которую вы можете заработать — deposit",max(deposit))