def find_max_min_numbers(numbers):
    max_number = numbers[0]
    min_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num

    return max_number, min_number

num_count = int(input("Kaç tane sayi kullanacaksiniz?"))
number_list = []

for i in range(num_count):
    number = float(input(f"{i+1}. sayiyi giriniz: "))
    number_list.append(number)

    max_num, min_num = find_max_min_numbers(number_list)

    print("En büyük sayi:", max_num)
    print("En küçük sayi:", min_num)