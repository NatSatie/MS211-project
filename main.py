import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import datetime as dt

time = []
time2020 = []
time2019 = []
date2019 = []
date2020 = []

with open('dados_rodoviaria_tiete_fev_2019.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tempDate = row['Date']
        tempTime = int(row['Daily Mean Travel Time (Seconds)'])
        time2019.append(tempTime)
        date2019.append(tempDate)
with open('dados_rodoviaria_tiete_mar_2019.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tempDate = row['Date']
        tempTime = int(row['Daily Mean Travel Time (Seconds)'])
        time2019.append(tempTime)
        date2019.append(tempDate)

with open('dados_rodoviaria_tiete_fev.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tempDate = row['Date']
        tempTime = int(row['Daily Mean Travel Time (Seconds)'])
        time.append(tempTime)
        time2020.append(tempTime)
        date2020.append(tempDate)
with open('dados_rodoviaria_tiete_mar.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tempDate = row['Date']
        tempTime = int(row['Daily Mean Travel Time (Seconds)'])
        time.append(tempTime)
        time2020.append(tempTime)
        date2020.append(tempDate)

def mmq5(x, y, dias):
    A = [
        [0 ,0, 0, 0, 0],
        [0 ,0 ,0, 0, 0],
        [0 ,0 ,0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    B = [
        [0],
        [0],
        [0],
        [0],
        [0]
    ]
    alpha = [
        [0],
        [0],
        [0],
        [0],
        [0]
    ]

    for i in  range(0,5):
        for j in range(0,5):
            aux = i + j + 3
            A[i][j] = pow(dias, aux)/aux

    #print(A)

    for i in range(0,dias):
        B[0][0] += (y[i]* x[i])
        B[1][0] += (y[i] * x[i]* x[i])
        B[2][0] += (y[i] * x[i] * x[i]* x[i])
        B[3][0] += (y[i] * x[i] * x[i] * x[i]* x[i])
        B[4][0] += (y[i] * x[i] * x[i] * x[i] * x[i] * x[i])

    #print(B)

    alpha = np.linalg.solve(A, B)

    return alpha

def mmq4(x, y, dias):
    A = [
        [0 ,0, 0, 0],
        [0 ,0 ,0, 0],
        [0 ,0 ,0, 0],
        [0, 0, 0, 0]
    ]
    B = [
        [0],
        [0],
        [0],
        [0]
    ]
    alpha = [
        [0],
        [0],
        [0],
        [0]
    ]

    for i in  range(0,4):
        for j in range(0,4):
            aux = i + j + 3
            A[i][j] = pow(dias, aux)/aux

    #print(A)

    for i in range(0,dias):
        B[0][0] += (y[i]* x[i])
        B[1][0] += (y[i] * x[i]* x[i])
        B[2][0] += (y[i] * x[i] * x[i]* x[i])
        B[3][0] += (y[i] * x[i] * x[i] * x[i]* x[i])

    #print(B)

    alpha = np.linalg.solve(A, B)

    return alpha

def mmq3(x, y, dias):
    A = [
        [0 ,0, 0],
        [0 ,0 ,0],
        [0 ,0 ,0]
    ]
    B = [
        [0],
        [0],
        [0]
    ]
    alpha = [
        [0],
        [0],
        [0]
    ]

    for i in  range(0,3):
        for j in range(0,3):
            aux = i + j + 3
            A[i][j] = pow(dias, aux)/aux

    #print(A)

    for i in range(0,dias):
        B[0][0] += (y[i]* x[i])
        B[1][0] += (y[i] * x[i]* x[i])
        B[2][0] += (y[i] * x[i] * x[i]* x[i])

    #print(B)

    alpha = np.linalg.solve(A, B)

    return alpha

def mmq2(x, y, dias):
    A = [
        [0 ,0],
        [0 ,0]
    ]
    B = [
        [0],
        [0]
    ]
    alpha = [
        [0],
        [0]
    ]

    for i in  range(0,2):
        for j in range(0,2):
            aux = i + j + 3
            A[i][j] = pow(dias, aux)/aux

    #print(A)

    for i in range(0,dias):
        B[0][0] += (y[i]* x[i])
        B[1][0] += (y[i] * x[i]* x[i])

    #print(B)

    alpha = np.linalg.solve(A, B)

    return alpha

def comparar_2020_2019():
    x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in date2019]
    y_2020 = time2020
    y_2019 = time2019

    xSubstitute = []
    size = int(np.size(x_values))
    for i in range(0, size):
        xSubstitute.append(int(i))

    alpha2019 = mmq5(xSubstitute, y_2019, 60)
    alpha2020 = mmq5(xSubstitute, y_2020, 60)

    x = np.array(range(size))
    y2019 = (alpha2019[0][0] * pow(x, 1)) + (alpha2019[1][0] * pow(x, 2)) + (alpha2019[2][0] * pow(x, 3)) + (
                alpha2019[3][0] * pow(x, 4)) + (alpha2019[4][0] * pow(x, 5))
    y2020 = (alpha2020[0][0] * pow(x, 1)) + (alpha2020[1][0] * pow(x, 2)) + (alpha2020[2][0] * pow(x, 3)) + (
            alpha2020[3][0] * pow(x, 4)) + (alpha2020[4][0] * pow(x, 5))

    line1, = plt.plot(x, y2019)
    line2, = plt.plot(x, y2020)
    plt.legend([line1, line2], ['02/2019 - 03/2019', '02/2020 - 03/2020'])
    plt.ylim(800, 4000)
    plt.xlim(int(0), 60)
    plt.xlabel('Número de dias ')
    plt.ylabel('Tempo em segundos do Percurso')
    plt.title(
        'Tabela do Tempo percorrido de um motorista do Uber sair do Terminal Tietê até o aeroporto de Guarulhos')
    plt.figure()

def equacao_2grau():
    x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in date2020]
    y_average = time
    dias = int(60)

    xSubstitute = []
    size = int(np.size(x_values))
    for i in range(0, size):
        xSubstitute.append(int(i))

    alphas = mmq2(xSubstitute, y_average, size)
    print(alphas)

    x = np.array(range(size))
    y2 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2))
    y = y2

    plt.plot(x, y)
    plt.plot(xSubstitute, y_average, 'ro')
    plt.ylim(1000, 3000)
    plt.xlim(int(0), 60)
    plt.xlabel('Número de dias ')
    plt.ylabel('Tempo em segundos do Percurso')
    plt.title(
        'Tabela do Tempo percorrido de um motorista do Uber sair do Terminal Tietê até o aeroporto de Guarulhos de fev/2019 até mar/2019')
    plt.figure()

def equacao_3grau():
    x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in date2020]
    y_average = time
    dias = int(60)

    xSubstitute = []
    size = int(np.size(x_values))
    for i in range(0, size):
        xSubstitute.append(int(i))

    alphas = mmq3(xSubstitute, y_average, size)
    print(alphas)

    x = np.array(range(size))
    y3 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3))
    # y3 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3))
    # y4 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3)) + (alphas[3][0] * pow(x, 4))
    # y5 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3)) + (alphas[3][0] * pow(x, 4)) + (alphas[4][0] * pow(x, 5))
    y = y3

    plt.plot(x, y)
    plt.plot(xSubstitute, y_average, 'ro')
    plt.ylim(1000, 3000)
    plt.xlim(int(0), 60)
    plt.xlabel('Número de dias ')
    plt.ylabel('Tempo em segundos do Percurso')
    plt.title(
        'Tabela do Tempo percorrido de um motorista do Uber sair do Terminal Tietê até o aeroporto de Guarulhos de fev/2019 até mar/2019')
    plt.figure()

def equacao_4grau():
    x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in date2020]
    y_average = time
    dias = int(60)

    xSubstitute = []
    size = int(np.size(x_values))
    for i in range(0, size):
        xSubstitute.append(int(i))

    alphas = mmq4(xSubstitute, y_average, size)
    print(alphas)

    x = np.array(range(size))
    y4 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3)) + (alphas[3][0] * pow(x, 4))
    # y5 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3)) + (alphas[3][0] * pow(x, 4)) + (alphas[4][0] * pow(x, 5))
    y = y4

    plt.plot(x, y)
    plt.plot(xSubstitute, y_average, 'ro')
    plt.ylim(1000, 3000)
    plt.xlim(int(0), 60)
    plt.xlabel('Número de dias ')
    plt.ylabel('Tempo em segundos do Percurso')
    plt.title(
        'Tabela do Tempo percorrido de um motorista do Uber sair do Terminal Tietê até o aeroporto de Guarulhos de fev/2019 até mar/2019')
    plt.figure()

def equacao_5grau():
    x_values = [dt.datetime.strptime(d, "%m/%d/%Y").date() for d in date2020]
    y_average = time
    dias = int(60)

    xSubstitute = []
    size = int(np.size(x_values))
    for i in range(0, size):
        xSubstitute.append(int(i))

    alphas = mmq5(xSubstitute, y_average, size)
    print(alphas)

    x = np.array(range(size))
    y5 = (alphas[0][0] * pow(x, 1)) + (alphas[1][0] * pow(x, 2)) + (alphas[2][0] * pow(x, 3)) + (alphas[3][0] * pow(x, 4)) + (alphas[4][0] * pow(x, 5))
    y = y5

    plt.plot(x, y)
    plt.plot(xSubstitute, y_average, 'ro')
    plt.ylim(1000, 3000)
    plt.xlim(int(0), 60)
    plt.xlabel('Número de dias ')
    plt.ylabel('Tempo em segundos do Percurso')
    plt.title(
         'Tabela do Tempo percorrido de um motorista do Uber sair do Terminal Tietê até o aeroporto de Guarulhos de fev/2019 até mar/2019')

    plt.figure()

def main():
    comparar_2020_2019()
    equacao_2grau()
    equacao_3grau()
    equacao_4grau()
    equacao_5grau()
    plt.show()

main()