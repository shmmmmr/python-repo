# TODO Найдите количество книг, которое можно разместить на дискете

a = 100
b = 50
c = 25
size_symb = 4
size = a*b*c*size_symb
disketa = int(1.44 * 1024 * 1024 // size)
print("Количество книг, помещающихся на дискету:", disketa)
