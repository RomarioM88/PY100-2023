BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100  # TODO ввести количество страниц
lines = 50  # TODO ввести количество строк
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars  # TODO общее количество символов в книге
total_bytes = total_chars  # TODO размер одной книги в байтах

disk_size = 1440000  # TODO размер дискеты в байтах
d=round(1024*1.44*1024)
#d=d*1024
a=round(d/total_bytes)  # TODO найти количество книг, которое поместится на дискете
#print(total_bytes)

print(float(a))