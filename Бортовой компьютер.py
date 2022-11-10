#Путевой компьютер
program = "Путевой компьютер версии 1"
#Переменные
stars = 80 #Количество звездочек
tabs = 5 #Кол-во отступов

dist = 0 #Расстояние, которое нужно проехать
speed = 0 #Средняя скорость
time_hours = 0 #Время в движении часы
time_min = 0 #Время в движении минуты
total_time_hours = 0 #Общее время часы
total_time_min = 0 #Общее время минуты

tank = 0 #Объем бака
consum = 0 #Средний расход л/100 км
refuel = 0 #Кол-во дозаправок
refuel_time = 20 #Время дозаправки
fuel = 0 # Общий объем топлива
price = 0 #Ценя за литр

breaks = 0 #Кол-во остановок
breaks_time = 0 #Время остановки

# Заголовок
print("\t" * tabs, program)
print("*" * stars)

#Ввод данных от пользователя
dist = int(input("Введите расстояние, км: "))
speed = int(input("Введите среднюю скорость, км/ч: "))
consum = float(input("Введите средний расход, л/100 км: "))
tank = int(input("Введите объем бака, литры: "))
price = float(input("Введите стоимость топлива, руб/литр: "))
breaks = int(input("Введите кол-во остановок: "))
breaks_time = int(input("Введите время остановок: "))

#Расчеты
time = dist * 60 / speed
fuel = consum * dist / 100
time_hours = time // 60
time_min = time - time_hours * 60


refuel = fuel // tank
total_time = time + refuel * refuel_time + breaks * breaks_time
total_time_hours = total_time // 60
total_time_min = total_time - total_time_hours * 60

print("*" * stars)
print("\t" * tabs, "Результаты")

print("Время за рулем: ", int(time_hours), "ч.", int(time_min), "мин.")
print("Общее время за рулем: ", int(total_time_hours),"ч.", int(total_time_min), "мин.")
print("Количество дозаправок: ", int(refuel))
print("Потраченое время на дозаправку: ", int(refuel) * int(refuel_time), "минут")
print("Израсходавано топлива, л: ", fuel)
print("Стоимость топлива: ", fuel * price)
