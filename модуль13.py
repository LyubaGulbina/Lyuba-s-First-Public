price_1 = int(0) #стоимость билета для посетителей до 18 лет
price_2 = int(990) # стоимость билета для посетителей от 18 до 25 лет
price_3 = int(1390) # стоимость билета для остальных посетителей
ticket_sum= int() # общая стоимость билета
ticket_count=0 # общее число посетителей
n=int(input("введите число посетителей "))
ticket_count=int(n)

for n in range (1,n+1):
    visitor_age = int(input("введите возраст посетителя "))
    if visitor_age<18:
        print("Стоимость билета - ", price_1, "руб")
        ticket_count+=1
        ticket_sum=ticket_sum+price_1
    elif visitor_age==18 or visitor_age<25:
        print("Стоимость билета - ", price_2, "руб")
        ticket_count+=1
        ticket_sum=ticket_sum+price_2
    else:
        print("Стоимость билета - ", price_3, "руб")
        ticket_count+=1
        ticket_sum=ticket_sum+price_3
if n>3:
    ticket_sum=ticket_sum*0.9

while ticket_count<=n:
    break

print("Сумма к оплате - ", ticket_sum, "руб")