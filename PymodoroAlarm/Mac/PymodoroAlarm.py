# -*- coding: utf-8 -*-
#coding: utf-8
from os import system, path
from time import sleep, ctime
from Pylipe import digGrande, textColor as tc, Arquivo as arq
from datetime import datetime, date

system("printf '\e[8;16;37t'")
system("mkdir status")
system('@CHCP 65001 >nul')            # Permitir texto colorido  


nomeArq = 'status/status-' + str(date.today())

# Verifica se existe o arquivo que salva os ciclos
if (not path.isfile(nomeArq + '.txt')):
    arq.criar(nomeArq)
    arq.add(nomeArq, 'Pomodoro of day: ' + str(date.today()) + '\nDone: 0')
    fechados = 0
else: 
    arquivo = open(nomeArq + '.txt', 'r') 
    conteudo = arquivo.readlines()
    arquivo.close()
    l = len(conteudo)
    fechados = int(conteudo[l - 1][-1])


titulo = tc.red + 'Pomodoro timer!!!'.center(37)

avisos  = tc.yellow + '!! WARNINGS !!'.center(37) + '\n'
avisos += tc.green  + 'Check notes!'                 + '\n' 
avisos += tc.cyan   + 'Update schedule'                    + '\n' 
avisos += tc.red    + 'Review studied content'                       + '\n' 
avisos += tc.yellow + '!!! LEGENDS NEVER DIE !!!'.center(37)

# Programa ativo
while(True):
    system('clear')
    
    # Tela inicial
    print(titulo)
    print((tc.cyan + 'Sessions done: ' + str(fechados)).center(37))
    time = input(tc.purple + "At which minute should alarms play??? ")
    
    # Reconfigura os ciclos concluídos
    if time == 'set':
        fechados = int(input('How many sessions were done?? '))
        arq.lastLineE(nomeArq)
        arq.add(nomeArq, 'Done: ' + str(fechados))
        continue # Pula um ciclo

    if time == '':
        time = '50'
    
    # Configura entrada
    time = float(time) - datetime.now().minute - 1
    segs = time * 60

    # Contador regressivo
    while(segs > 0):
        
        system('clear')

        segs -= 1
        minu = int(segs / 60)
        sega = int(segs % 60)
        
        # Cores para digGrande
        if minu >= time * 0.8:
            cor = tc.white
        elif minu >= time * 0.5:
            cor = tc.yellow
        elif minu >= time * 0.2:
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
        print((tc.cyan + 'Sessions done: ' + str(fechados)).center(37))
        print('Remaining time: ')
        print(cor + digGrande(int(digs[0]), int(digs[1]), int(digs[2]), int(digs[3])))
        print(avisos)
        
        sleep(1)
    
    # Só conta se o time é maior que o intervalo de descanso 
    if time > 10:
        arq.lastLineE(nomeArq)
        fechados += 1
        arq.add(nomeArq, 'Finished at: ' + ctime().split()[3] + '\nDone: ' + str(fechados))
    
    # Pega a hora atual
    system('clear')
    hrAtual = ctime().split()[3]
    print('Finished at: ' + hrAtual)
    
    # Abre uma alert box no final do ciclo
    system('open "https://www.youtube.com/shorts/6ZN69be827c"')
