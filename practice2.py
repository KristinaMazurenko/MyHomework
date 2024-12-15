# Тема: Основные методы строк
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Преобразуйте строку "hOw aRe yOu?" в верхний регистр.
# Ожидаемый результат: "HOW ARE YOU?"

str = 'hOw aRe yOu?'
print(str.upper())

# 2. Посчитайте количество символов "a" в строке "Bananas are amazing!".

str1 = 'Bananas are amazing!'
print(str1.count('a'))

# 3. Преобразуйте строку "PYTHON PROGRAMMING" в нижний регистр.
# Ожидаемый результат: "python programming"

str2 = 'PYTHON PROGRAMMING'
print(str2.lower()) 

# 4. Удалите начальные пробелы из строки "   Discover new worlds   ".
# Ожидаемый результат: "Discover new worlds   "

str3 = '   Discover new worlds   '
print(str3.lstrip())

# 5. Замените "rainy" на "sunny" в строке "It was a rainy day.".
# Ожидаемый результат: "It was a sunny day."

str4 = 'It was a rainy day.'
print(str4.replace('rainy', 'sunny'))

# 6. Найдите индекс подстроки "innovation" в строке "Innovation drives progress.".

str5 = 'Innovation drives progress.'
print(str5.find('innovation')) 

# 7. Удалите конечные пробелы из строки "   Explore the universe   ".
# Ожидаемый результат: "   Explore the universe"

str6 = '   Explore the universe   '
print(str6.rstrip())

# 8. Найдите индекс подстроки "galaxy" в строке "The Milky Way galaxy is vast.".

str7 = 'The Milky Way galaxy is vast.'
print(str7.find('galaxy')) 

# 9. Разделите строку "Apple;Banana;Cherry;Date" по точке с запятой.
# Ожидаемый результат: ["Apple", "Banana", "Cherry", "Date"]

str8 = 'Apple;Banana;Cherry;Date'
print(str8.split(';'))

# 10. Замените "robots" на "humans" в строке "In the future, robots will rule the world.".
# Ожидаемый результат: "In the future, humans will rule the world."

str9 = 'In the future, robots will rule the world.'
print(str9.replace('robots', 'humans'))

# 11. Преобразуйте строку "artificial intelligence" в заглавный регистр.
# Ожидаемый результат: "Artificial Intelligence"

str10 = 'artificial intelligence'
print(str10.title())

# 12. Разделите строку "Python is a versatile language" по пробелам.
# Ожидаемый результат: ["Python", "is", "a", "versatile", "language"]

str11 = 'Python is a versatile language'
print(str11.split(' '))

# 13. Удалите начальные и конечные пробелы из строки "   Learn Python   ".
# Ожидаемый результат: "Learn Python"

str12 = '   Learn Python   '
print(str12.strip())

