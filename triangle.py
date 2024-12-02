def area(a, h): 
    ''' Функция возвращает площадь треугольника. Пример вызова функции:
    a = 10, h = 5
    10 * 5 / 2 = 25
    return 25 
    Также производится проверка на корректность значений (любые измерения не могут быть меньше или равно  0)
    '''
    if a <= 0 or h <= 0:
        raise ValueError()
    return a * h / 2 

def perimeter(a, b, c): 
    ''' Функция возвращает периметр треугольника. Пример вызова функции:
    a = 10, b = 7, c = 8
    10 + 8 + 7 = 25
    return 25 
    Также производится проверка на корректность значений (любые измерения не могут быть меньше или равно 0)
    ''' 

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError()

    return a + b + c 