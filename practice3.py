# Темы: Спецсимволы и экранирование символов, Форматирование строк и F-строки
# Результат по каждому заданию необходимо выводить в консоль через print().

# 1. Вставьте символ новой строки в строку "Hello World".
# Ожидаемый результат:
# Hello
# World

print('Hello \nworld!')

# 2. Вставьте символ обратного слэша в строку "This is a backslash: ".
# Ожидаемый результат: "This is a backslash: \"

print('This is a backslash: \\')

# 3. Экранируйте кавычки в строке "He said, "Hello!"".
# Ожидаемый результат: He said, "Hello!"

print("He said, \"Hello!\"")

# 4. Экранируйте одинарные кавычки в строке "It's a sunny day".
# Ожидаемый результат: It's a sunny day

print('It\'s a sunny day')

# 5. Вставьте символ новой строки в строку "Python Programming".
# Ожидаемый результат:
# Python
# Programming

print('Python \nProgramming')

# 6. Экранируйте кавычки в строке "She said, 'Hi!'".
# Ожидаемый результат: She said, 'Hi!'

print('She said, \'Hi!\'')

# 7. Экранируйте обратный слэш в строке "Path to file: C:\\".
# Ожидаемый результат: Path to file: C:\\

print('Path to file: C:\\\\')

# 8. Используйте метод `format()` для строки "This is a ... course for ... learners." с переменными course="Python"
# и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."

course = "Python"
level = "beginner"
str = 'This is a {} course for {} learners.'.format(course, level)
print(str)

# 9. Используйте F-строку для строки "This is a ... course for ... learners." с переменными
# course="Python" и level="beginner". Ожидаемый результат: "This is a Python course for beginner learners."

course1 = "Python"
level1 = "beginner"
print(f'This is a {course1} course for {level1} learners.')

# 10. Используйте метод `format()` для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."

topic = "Machine Learning"
str1 = 'Welcome to the {} workshop.'.format(topic)
print(str1)

# 11. Используйте F-строку для строки "Welcome to the ... workshop." с переменной topic="Machine Learning".
# Ожидаемый результат: "Welcome to the Machine Learning workshop."

topic = "Machine Learning"
print(f'Welcome to the {topic} workshop.')

# 12. Придумайте название переменной и поместите в нее строку "machine learning",
# затем преобразуйте первые буквы слов в заглавный регистр, чтобы получилось "Machine Learning".
# Затем создайте переменную со строкой "Course: ". Используйте метод `format()`, чтобы показать в консоли
# "Course: Machine Learning"

a = 'machine learning'
c = (a.title())
b = 'Course: {}'.format(c)
print(b)

# 13. Объедините строки "Data" и "Science" с пробелом между ними, дублируйте результат три раза, и используйте F-строку
# для строки "Field: ...". Ожидаемый результат: "Field: Data ScienceData ScienceData Science"

a1 = 'Data'
b1 = 'Science'
c1 = ' '.join([a1, b1])
d1 = c1 * 3
print(f'Field: {d1}')

# 14. Выведите третий символ строки "Information", затем используйте метод `format()` для строки "Third character: ...".
# Ожидаемый результат: "Third character: f"

a2 = 'Information'
b2 = a2[2]
c2 = 'Third character: {}'.format(b2)
print(c2)


# 15. Определите длину строки "Neural Networks", умножьте её на 2, и используйте F-строку для строки "Length: ".
# Ожидаемый результат: "Length: 28"

a3 = 'Neural Networks'
b3 = len(a3) * 2
print(f'Field: {b3}')

# 16. Преобразуйте строку "Deep Learning" в заглавный регистр, найдите индекс подстроки "LEARNING", и выведите символ
# на этом индексе. Ожидаемый результат: "L"

a4 = 'Deep Learning'
b4 = a4.upper()
print(b4.find('LEARNING'))
print(b4[5])

# 20. Определите длину строки "Starta", затем преобразуйте её в строку и добавьте к строке " has length of ",
# используя метод `format()`. Ожидаемый результат: "Starta has length of 6"

a5 = 'Starta'
b5 = len(a5)
c5 = '{} has length of {}'.format(a5, b5)
print(c5)
