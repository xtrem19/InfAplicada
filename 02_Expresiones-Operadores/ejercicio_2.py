# Expresiones y Operadores

## Expresiones.
'''
Las expresiones son combinaciones de constantes, variables, símbolos de operación, paréntesis y nombres de funciones especiales.

Una expresión consta de operandos y operadores. Según sea el tipo de objetos que manipulan, las expresiones se clasifican en: 

* aritméticas 
* relacionales
* lógicas
* carácter

El resultado de la expresión aritmética es de tipo numérico; el resultado de la expresión relacional y de una expresión lógica es de tipo lógico; el resultado de una expresión carácter es de tipo carácter.

Las expresiones aritméticas son análogas a las fórmulas matemáticas. Las variables y constantes son numéricas (real o entera) y las operaciones son las aritméticas.

* `+` - Este es el operador de suma y realiza la función de adicionar un operando al otro. 
* `-` - Este es el operador de resta y realiza la función de sustraer un operando de otro.
* `*` - Este es el operador de multiplicación y realiza la función de aumentar un operando en función de otro operando.
* `/` - Este es el operador de división y realiza la función de seccionar un operando en función de otro operando.
* `%` - Este es el operador de módulo y realiza la función de regresar el residuo de una división.
* `**` - Este es el operador de exponencial y permite obtener la potencia de un operando en función de otro operando.

A continuación se presentan algunos ejemplos de los operadores en código Python.
'''
### Operador +.

#python
a = 7 + 3
print(a)   #10 class
a = 5
b = 3
c = a + b
print(c)
print(3+4)
#


### Operador -.

#python
a = 6 - 2
print(a)
a = 5
b = 3
c = a - b
print(c)
print(2-6)
#


### Operador *.

#python
a = 3 * 4
print(a)
a = 6
b = 3
c = a * b
print(c)
print(5*7)
#


### Operador /.

#python
a = 6 / 2
print(a)
a = 5
b = 3
c = a / b
print(c)
print(10/3)
#

### Operador %.

#python
a = 8 % 4
print(a)
a = 9
b = 2
c = a % b
print(c)
print(6%3)
#

### Operador **.

#python
a = 3 ** 3
print(a)
a = 2
b = 4
c = a ** b
print(c)
print(4**3)
#


### Operador <.

#python
a = 3 < 3
print(a)
a = 2
b = 4
c = a < b
print(c)
print(4<3)
#

### Operador >.

#python
a = 4 > 2
print(a)
a = 5
b = 7
c = a > b
print(c)
print(9>2)
#

### Operador ==.

#python
a = 5 == 5
print(a)
a = 6
b = 9
c = a == b
print(c)
print(6==2)
#

### Operador !=.

#python
a = 4 != 2
print(a)
a = 5
b = 3
c = a != b
print(c)
print(8!=8)
#

### Operador <=.


#python
a = 5 <= 3
print(a)
x = 7
y = 5
z = x <= y
print(z)
print(9<=4)
#

### Operador >=.

#python
a = 2 >= 8
print(a)
a = 3
b = 4
c = a >= b
print(c)
print(7>=3)
#


## Expresiones lógicas.


### Operador and.

#python
print(4-1==3 and 5>6)
print(6+7 > 11 and 3==3)
#

### Operador or.

#python
print(4-1==3 or 5>6)
print(6+7 > 11 or 3==3)
#

### Operador not.

#python
print(not 5>6)
print(not 5>4)
#

## Expresiones de carácter

#Ejemplo:

#python
import re
frase = "Tengo 2 hijos que tienen 15 y 11 años"
patron = '[0-9]+' #Esta es una expresión regular
re.findall(patron, frase)
#



