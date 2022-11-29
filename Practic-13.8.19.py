ticket_count = 0
ticket = int(input("Введите количество билетов: "))
x = [i for i in range(ticket)]
age = {}
for a in x:
    age[a] = int(input("Введите возраст: "))
for a, age_count in age.items():
    if age_count < 18:
        ticket_count += 0
    elif 18 >= age_count < 25:
        ticket_count += 990
    elif age_count >= 25:
        ticket_count += 1390
if ticket > 3:
    ticket_count *= 0.9
print(f'Сумма к оплате: {ticket_count} руб.')