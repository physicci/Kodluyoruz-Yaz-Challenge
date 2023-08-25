def count_vowels(input_text):
    vowels = "aeıiouAEIİOU"
    vowel_count = sum(1 for char in input_text if char in vowels)
    return vowel_count

def count_words_letters_or_digits(input_data):
    if input_data.isdigit():
        number = int(input_data)
        digit_sum = sum(int(digit) for digit in str(number))
        return "Bu bir sayı.", digit_sum
    else:
        words = input_data.split()
        word_count = len(words)
        letter_count = sum(len(word) for word in words)
        vowel_count = sum(count_vowels(word) for word in words)
        return (
            f"Kelime sayisi: {word_count}",
            f"Harf sayisi: {letter_count}",
            f"Sesli harf sayisi: {vowel_count}"
        )

user_input = input("Analiz için bir girdi yazınız: ")
word_or_digit_info = count_words_letters_or_digits(user_input)
for info in word_or_digit_info:
    print(info)
