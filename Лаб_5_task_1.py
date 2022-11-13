from pprint import pprint as write
write([{'bin': bin(number), 'dec': number, 'oct': oct(number), 'hex': hex(number)} for number in range(16)])