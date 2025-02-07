ab = int(input('Введите сумму продажи'))
if ab <= 5000:
    ab = ab - (ab * 50 / 100)
elif ab == 5000 and ab < 16000:
    ab = ab - (ab * 12 / 100)
else:
    ab > 15000
    ab = ab - (ab * 30 / 100)
print('Сумма продажи со скидкой равна:', ab)