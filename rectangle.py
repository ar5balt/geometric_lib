def area(a, b): 
    ''' Функция возвращает площадь прямоугольника. Пример вызова функции: 
    a = 10, b = 8 
    10 * 8 = 80
    return 80 
    Также производится проверка на корректность значений (любые измерения не могут быть меньше или равно 0)
    ''' 
    if a <= 0 or b <= 0:
        raise ValueError() 
    return a * b 

def perimeter(a, b): 
    ''' Функция возвращает периметр прямоугольника. Пример вызова функции:
    a = 10, b = 8
    2 * (10 + 8) = 36
    return 36
    Также производится проверка на корректность значений (любые измерения не могут быть меньше или равно 0)
    ''' 
    if a <= 0 or b <= 0:
        raise ValueError() 
    return 2 * (a + b)