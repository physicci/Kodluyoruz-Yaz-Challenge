def is_armstrong_number(number):
    original_number = number
    num_digits = len(str(number))
    sum_of_cubes = 0
    while number > 0:
        digit = number % 10
        sum_of_cubes += digit ** num_digits
        number //=10

        return sum_of_cubes == original_number
user_number = int(input("Sayi giriniz:"))
if is_armstrong_number(user_number):
    print(user_number, "Girilen sayi, bir Armstrong sayisidir.")
else:
    print(user_number, "Girilen sayi, bir Armstrong sayisi değildir.")