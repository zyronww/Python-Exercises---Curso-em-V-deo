from math import sin,cos,tan, radians
angle = float(input('Valor do ângulo: '))
radians = radians(angle)
sen = sin(radians)
cos = cos(radians)
tan = tan(radians)
print(f'''O triângulo com ângulo igual a {angle}° tem:
      Seno: {sen:.2f}
      Cosseno: {cos:.2f}
      Tangente: {tan:.2f} ''')