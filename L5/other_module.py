from module import CAT, DOG as _DOG, _FISH

APPLE = 'apple'
MEAT = 'meat'
_CARROT = 'carrot'

# _all_   список переменных доступных для публичного пользования
# иного можно указыать системные неизменяемые переменные в качесте публчиных
__all__ = ('APPLE', '_CARROT')

print(_DOG)