import math  # Importa a biblioteca para funções matemáticas, como raiz quadrada

# Entrada de dados: coordenadas da origem (ponto de referência)
x0 = int(input('Digite a origem do eixo x: '))
y0 = int(input('Digite a origem do eixo y: '))

# Entrada de dados: quantidade de pontos a serem analisados
p = int(input('Digite o número de pontos: '))

# Inicializa variáveis para armazenar o ponto mais próximo e mais distante
pdmin = None
pdmax = None
dmin = float('inf')  # Começa com infinito positivo para encontrar o mínimo
dmax = 0  # Começa com 0 para encontrar o máximo

# Lista para contagem de pontos em cada quadrante (1º a 4º)
qcount = [0, 0, 0, 0]
countNum = 0  # Contador de iterações

# Loop principal para entrada e análise dos pontos
while countNum < p:
    x = float(input('Digite o x do ponto: '))
    y = float(input('Digite o y do ponto: '))

    # Calcula a distância euclidiana do ponto até a origem (x0, y0)
    d = math.sqrt((x - x0)**2 + (y - y0)**2)

    # Verifica e atualiza o ponto de menor distância
    if d < dmin:
        dmin = d
        pdmin = (x, y)

    # Verifica e atualiza o ponto de maior distância
    if d > dmax:
        dmax = d
        pdmax = (x, y)

    # Determina o quadrante do ponto (ignora pontos exatamente sobre os eixos)
    if x != x0 or y != y0:
        if x > x0:
            if y > y0:
                qcount[0] += 1  # 1º quadrante
            else:
                qcount[3] += 1  # 4º quadrante
        else:
            if y > y0:
                qcount[1] += 1  # 2º quadrante
            else:
                qcount[2] += 1  # 3º quadrante

    # Classifica a posição do ponto e exibe mensagem correspondente
    if x == 0 and y == 0:
        print(f'O ponto {x, y} está na origem')
    elif x == x0 or y == y0:
        print(f'O ponto {x, y} está sobre o eixo das coordenadas')
    else:
        if x > x0:
            q = '1' if y > y0 else '4'
        else:
            q = '2' if y > y0 else '3'
        print(f'O ponto {x, y} está no {q}° quadrante')

    countNum += 1  # Incrementa o contador

# Exibe os resultados finais
print(f'O ponto de menor distância em relação à origem é {pdmin} com uma distância de {dmin:.2f}.')
print(f'O ponto de maior distância em relação à origem é {pdmax} com uma distância de {dmax:.2f}.')
print(f'Existem {qcount[0]} ponto(s) no 1° quadrante;
        Existem {qcount[1]} ponto(s) no 2° quadrante;
        Existem {qcount[2]} ponto(s) no 3° quadrante;
        Existem {qcount[3]} ponto(s) no 4° quadrante;
