# 1
n = 10
element_list = list(range(n))

for i in element_list:
    if i % 2 == 0 and i != 0:
        print(i)


# 2
capitals = dict()

capitals['Ukraine'] = 'Kiev'
capitals['Poland'] = 'Warshaw'
capitals['England'] = 'London'

countries = ['USA', 'France', 'Egypt', 'Ukraine', 'Poland', 'England']

for country in countries:
    if country in capitals:
        print(f'Столица страны {country}: {capitals[country]}')


# 3
for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# 4
def bank(deposit_sum, years, rate):
    amount_money = deposit_sum + deposit_sum * rate * years
    return amount_money


print(bank(1000, 2, 0.2))
