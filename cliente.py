from weakref import proxy
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')


print('Archivos')
print(proxy.list_contents('c:'))

print('')
print('Ingreso números para realizar la suma')
number1 = int(input("Número 1: "))
number2 = int(input("Número 2: "))
print('')

result = proxy.add(number1, number2)
print(f'Resultado de la suma {number1} + {number2} es: {result}')