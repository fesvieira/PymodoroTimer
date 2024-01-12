def digGrande(dig1, dig2, dig3, dig4):

    res = ''
    nums = [
        ' ______ \n|      |\n|      |\n|      |\n|      |\n|______|\n',
        '        \n       |\n       |\n       |\n       |\n       |\n',
        ' ______ \n       |\n       |\n ------ \n|       \n|______ \n',
        ' ______ \n       |\n       |\n ------|\n       |\n ______|\n',
        '        \n|      |\n|      |\n ------|\n       |\n       |\n',
        ' ______ \n|       \n|       \n ------ \n       |\n ______|\n',
        ' ______ \n|       \n|       \n|------ \n|      |\n|______|\n',
        ' ______ \n       |\n       |\n       |\n       |\n       |\n',
        ' ______ \n|      |\n|      |\n|------|\n|      |\n|______|\n',
        ' ______ \n|      |\n|      |\n ------|\n       |\n ______|\n',
    ]
    
    linha = 0
    while linha <= 5:
        i = linha*9
        
        while nums[dig1][i] != '\n':
            res += nums[dig1][i]
            i += 1
        
        res += ' '
        i -= 8
        
        while nums[dig2][i] != '\n':
            res += nums[dig2][i]
            i += 1
        
        res += ' '
        i -= 8
        if linha == 2 or linha == 4:
            res += "# "
        else:
            res += "  "

        while nums[dig3][i] != '\n':
            res += nums[dig3][i]
            i += 1
        
        res += ' '
        i -= 8

        while nums[dig4][i] != '\n':
            res += nums[dig4][i]
            i += 1

        res += '\n'
        linha += 1

    
    return res

class textColor:
    red    = '\033[31;1m'
    green  = '\033[32;1m'
    white  = '\033[m'
    cyan   = '\033[36;1m'
    yellow = '\033[33;1m'
    purple = '\033[35;1m'

class Arquivo:
    def criar(nome):
        nome += '.txt'
        arquivo = open(nome, 'w')
        arquivo.write('')
        arquivo.close()

    def add(nome, texto):
        nome += '.txt'
        arquivo = open(nome, 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        conteudo.append(texto)   # insira seu conteúdo

        arquivo = open(nome, 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
        arquivo.close()
    
    def lastLineE(nome):
        nome += '.txt'
        arquivo = open(nome, 'r') # Abra o arquivo (leitura)
        conteudo = arquivo.readlines()
        conteudo = conteudo[0:len(conteudo) - 1]

        arquivo = open(nome, 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
        arquivo.close()


