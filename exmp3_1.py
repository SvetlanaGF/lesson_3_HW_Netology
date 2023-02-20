def count_letter(list_languages, letter):
    count = 0
    for word in list_languages:
        if letter in word:
            count = count + 1
    return count

list_languages = ['python', 'c++', 'c', 'scala', 'java']

char = input("Введите символ для поиска: ")
print(char)
print('Слов, содеражщих - ', char, ' в списке содержится - ', count_letter(list_languages, char))