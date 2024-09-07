def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
#inner_function()   # Вызов функуии приводит к ошибке, потому, что
                    # она является локальной функцией внутни функции test_function()