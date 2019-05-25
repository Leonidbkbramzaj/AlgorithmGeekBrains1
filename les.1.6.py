
string_alphabet = input("Введите требуемый алфавит")

a = len(string_alphabet)

x = int(input())

if x > 0 and x <= a:
    letter = string_alphabet[x-1]
    print(letter)
else:
    print(f"введите число не более {a}")


    # c точки зрения более продвинутой программы можно предустановить несколько
    # алфавитов, если пользователя не устроит, то он может ввести свой





