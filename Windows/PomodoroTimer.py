# -*- coding: utf-8 -*-
#coding: utf-8
from os import system, path
from time import sleep, ctime
from Pylipe import digGrande, textColor as tc, Arquivo as arq
from datetime import date

system('mode con: cols=37 lines=16')  # Abrir janela com tamanho fixo
system('@CHCP 65001 >nul')            # Permitir texto colorido  

nomeArq = 'status-' + str(date.today())

# Verifica se existe o arquivo que salva os ciclos
if (not path.isfile(nomeArq + '.txt')):
    arq.criar(nomeArq)
    arq.add(nomeArq, 'Pomodoro timer no dia: ' + str(date.today()) + '\nFechados: 0')
    fechados = 0
else: 
    arquivo = open(nomeArq + '.txt', 'r') 
    conteudo = arquivo.readlines()
    arquivo.close()
    l = len(conteudo)
    fechados = int(conteudo[l - 1][-1])


titulo = tc.red + 'Pomodoro timer!!!'.center(37)

avisos  = tc.yellow + '!! AVISOS !!'.center(37)
avisos += tc.green  + 'POSTURA' + '\n' 
avisos += tc.cyan   + 'ÁGUA' + '\n' 
avisos += tc.red    + 'M' + '\n' 
avisos += tc.yellow + '!!! LEGENDS NEVER DIE !!!'.center(37)

# Programa ativo
while(True):
    system('cls')
    
    # Tela inicial
    print(titulo)
    print((tc.cyan + 'Ciclos fechados: ' + str(fechados)).center(37))
    tempo = input(tc.purple + "Quantos minutos?? ")
    
    # Reconfigura os ciclos concluídos
    if tempo == 'set':
        fechados = int(input('Quantos ciclos já foram ?? '))
        arq.lastLineE(nomeArq)
        arq.add(nomeArq, 'Fechados: ' + str(fechados))
        continue # Pula um ciclo
    
    # Configura entrada
    tempo = float(tempo)
    segs = tempo * 60

    # Contador regressivo
    while(segs > 0):
        
        system('cls')

        segs -= 1
        minu = int(segs / 60)
        sega = int(segs % 60)
        
        # Cores para digGrande
        if minu >= tempo * 0.8:
            cor = tc.white
        elif minu >= tempo * 0.5:
            cor = tc.yellow
        elif minu >= tempo * 0.2:
            cor = tc.green
        else:
            cor = tc.cyan      

        # Configuração de entrada para digGrande para que os numeros < 10 apareçam corretamente
        digs = ''
        if minu < 10:
            digs += '0' + str(minu)
        else:
            digs += str(minu)
        
        if sega < 10:
            digs += '0' + str(sega)
        else:
            digs += str(sega)
        
        # Tela do timer
        print(titulo)
        print((tc.cyan + 'Ciclos fechados: ' + str(fechados)).center(37))
        print('Tempo restante: ')
        print(cor + digGrande(int(digs[0]), int(digs[1]), int(digs[2]), int(digs[3])))
        print(avisos)

        sleep(1)
    
    # Só conta se o tempo é maior que o intervalo de descanso 
    if tempo > 10:
        arq.lastLineE(nomeArq)
        fechados += 1
        arq.add(nomeArq, 'Encerrado as: ' + ctime().split()[3] + '\nFechados: ' + str(fechados))
    
    # Pega a hora atual
    system('cls')
    hrAtual = ctime().split()[3]
    print('Encerrado as: ' + hrAtual)
    
    # Abre uma alert box no final do ciclo
    system('mshta vbscript:Execute("msgbox ""ACABOOOOO!!!"",vbExclamation, ""Pomodoro"":close")')
