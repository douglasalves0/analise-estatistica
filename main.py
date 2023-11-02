import matplotlib.pyplot as plt

x = []
y = []

n = int(input())

for i in range(n): y.append(float(input()))
for i in range(n): x.append(float(input()))

plt.scatter(x, y)

plt.xlabel('Altura de queda')
plt.ylabel('Dano do fruto')

plt.title('Análise - banco de dados I')
plt.show()