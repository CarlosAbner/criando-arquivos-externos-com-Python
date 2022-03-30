# PRIMEIRO COMECAMOS COM A FUNCAO PARA ABRIR E FECHAR ARQUIVOS

def criarArquivo():
    arquivo = open('dados.txt', 'w') # W - abertura do arquivo
    arquivo.close()

# APOS A FUNCAO DE ABRIR E FECHAR CONCLUIDA, CRIAREMOS A FUNCAO DE ESCREVER NO ARQUIVO

def escreveArquivo():
    nome = input('Digite seu Nome: ')

    arquivo = open('dados.txt', 'a')
    arquivo.write(nome)
    arquivo.write('\n(00) 0000-000\n')
    arquivo.close()

# DEPOIS DE CRIARMOS A FUNCAO QUE ABRE ESCREVE O NOME DE ALGUEM VIA INPUT, ESCREVE UM NUMERO FICTÍCIO E FECHA,
# CRIAREMOS A FUNCAO DE LEITURA DO ARQUIVO EXTERNO

def lerArquivo():
    arquivo = open('dados.txt', 'r') # R = leitura 
    line = arquivo.readline ()

    while line != '':
        print(line)
        line = arquivo.realine()
    
    arquivo.close()

# TERMINADO A ABERTURA DO ARQUIVO, A LEITURA DELE, CHAMAMOS AS VARIAVEIS PARA EXIBICAO DO ARQUIVO

escreveArquivo() # essa variavel permite q o bloco de codigos de escrita no arquivo seja permitida

lerArquivo() # após terminado da escrita no arquivo, chamamos a variavel para nos mostrar o que tem nele