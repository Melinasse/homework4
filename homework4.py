my_string=input('Enter your text: ')
print('your text: ', my_string, ',Количество символов: ', len(my_string));
print('Строка в верхнем регистре: ',my_string.upper());
print('Строка в нижнем регистре: ',my_string.lower());
print('Замена символа пробел ,на решетку: ', my_string.replace(' ', '#'));
print(my_string[0]);
print(my_string[-1]);