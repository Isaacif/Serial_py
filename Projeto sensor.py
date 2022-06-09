import matplotlib.pyplot as plt
import  serial 
import keyboard               
k = 0

ser = serial.Serial('COM4', baudrate = 9600, timeout=1) #iniciando a comunicação serial
eixo_y = [] #lista que armazena o numero de dados
c_parada = 0 #saida do laço
pular_linha = "\n" #pular linha no arquivo
arquivo = open('dados.txt', 'w')
while (c_parada != 1):
    arduinomostrar = ser.readline() #ler a entrada serial
    try:
        dist = int(arduinomostrar)
        print(dist)
        eixo_y.append(dist)
        k = k+1
        arquivo.write(str(dist) + pular_linha)
    except ValueError: #Esse trecho para o erro 'b'
       continue
    if keyboard.is_pressed('q'): #saida do laço para a tecla pressionada 
        c_parada = 1
        

arquivo.close()
eixo_x = list(range(0,len(eixo_y)))
plt.ylim(0, 150) #limite de 5 metros no plot
plt.title('Gráfico de Varredura')
plt.xlabel('Tempo em Segundos')
plt.ylabel('Distância em cm')
Dist = plt.plot(eixo_x, eixo_y, 'r') 
plt.show()
print(k)
