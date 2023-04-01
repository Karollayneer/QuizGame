import time #Importar sleep para o usuário ler os resultados

#Definição de cores por variáveis
REDN   = "\033[1;31m"
RED  = "\033[0;31m"
GREEN = "\033[1;32m"
GREENBG = "\033[1;29;42m"
REVERSE = "\033[;;7m"
RESET = "\033[m"

#Cabeçalho do jogo
print(f''' 
{REDN}########################################################################################{RESET}
{REDN}#{RESET}                       Seja bem-vindo(a) ao Quizz Math 2022!                          {REDN}#{RESET}
{REDN}#{RESET}               Este jogo é composto por questões de múltipla escolha.                 {REDN}#{RESET}
{REDN}#{RESET}               Seu desempenho poderá desbloquear novas dificuldades.                  {REDN}#{RESET}
{REDN}#{RESET}       No fim, sua pontuação será registrada no Ranking dos Campeões. Boa sorte!      {REDN}#{RESET}
{REDN}########################################################################################{RESET}
''')
ranking = {}
i = 'S' #Condicional para repetição

while i == 'S': #Laço de repetição
    player = input('\nDigite o seu nome para começar a partida: ')
    nivel = 1 #Nível de dificuldade
    pontos = 0 # Contagem de pontos
    #Lista de perguntas nível 1
    #Leia os pares divididos por ':{}' como Chaves e Valores
    perguntas = {
        'Questão 1': {
            'pergunta': 'Quanto é 4x2? ',
            'respostas': {'a': '7', 'b': '9', 'c': '8', },
            'resposta_certa': 'c', },
        'Questão 2': {
            'pergunta': 'quanto é 9-3 ',
            'respostas': {'a': '1', 'b': '6', 'c': '4', },
            'resposta_certa': 'b',
        },
        'Questão 3': {
            'pergunta': 'quanto é 7+15 ',
            'respostas': {'a': '22', 'b': '19', 'c': '20', },
            'resposta_certa': 'a',
        },
        'Questão 4': {
            'pergunta': 'quanto é 19-14 ',
            'respostas': {'a': '9', 'b': '5', 'c': '10', },
            'resposta_certa': 'b',
        },
        'Questão 5': {
            'pergunta': 'quanto é 9*4 ',
            'respostas': {'a': '40', 'b': '34', 'c': '36', },
            'resposta_certa': 'c',
        },
    }

    print()
    respostas_certas = 0

    for p1, lista_p1 in perguntas.items():
        print(f'{GREEN}{p1}:{RESET} {lista_p1["pergunta"]}')

        print('RESPOSTAS:')
        for rchave , rvalor in lista_p1['respostas'].items():
            print(f'[{rchave}]: {rvalor}')

        resposta_usuario = input('Sua resposta:').lower()

        if resposta_usuario == lista_p1['resposta_certa']:
            print(f'{GREENBG}Parabéns!!! Você acertou!!!{RESET}\n')
            respostas_certas += 1
            pontos += 1
            time.sleep(1)

        elif resposta_usuario != 'a' and resposta_usuario != 'b' and resposta_usuario != 'c':
            print(f'{REVERSE}{REDN}Não foi digitado uma alternativa válida. RESPOSTA ERRADA!{RESET}')
            time.sleep(1)
        else:
            print(f'{REDN}RESPOSTA ERRADA!{RESET}\n')
            time.sleep(1.5)
            print()
        qtd_perguntas = len(perguntas)
        porcentagem_acerto = (respostas_certas / qtd_perguntas) * 100

    print(f'Você acertou {respostas_certas} respostas.')
    print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.\n')


    if porcentagem_acerto > 80:
        nivel = 2
        print(f'{GREEN}Parabéns, você liberou o próximo nível! {RESET}\n')
    else:
        print('Infelizmente você não habilitou a próxima etapa. Tente novamente!')

    time.sleep(2)

    if nivel == 2:
        print('█ QUESTIONÁRIO NÍVEL 2 █')
        respostas_certas2 = 0
        perguntas2 = {
            'Questão 1': {
                'pergunta': 'Quanto é √16? ',
                'respostas': {'a': '4', 'b': '6', 'c': '8', },
                'resposta_certa': 'a', },

            'Questão 2': {
                'pergunta': 'Quanto é 365*400*9*0? ',
                'respostas': {'a': '0', 'b': '674', 'c': '936', },
                'resposta_certa': 'a', },

            'Questão 3': {
                'pergunta': 'Quanto é 8²? ',
                'respostas': {'a': '16', 'b': '24', 'c': '64', },
                'resposta_certa': 'c', },

            'Questão 4': {
                'pergunta': 'Quanto é 0,5/2? ',
                'respostas': {'a': '0,20', 'b': '0,25', 'c': '0,30', },
                'resposta_certa': 'b', },

            'Questão 5': {
                'pergunta': 'Quanto é 2,5 metros em centímetros? ',
                'respostas': {'a': '250cm', 'b': '2500cm', 'c': '25000cm', },
                'resposta_certa': 'a', },


        }



        for p2, lista_p2 in perguntas2.items():
            print(f'{GREEN}{p2}:{RESET} {lista_p2["pergunta"]}')
            print('RESPOSTAS:')

            for rchave2, rvalor2 in lista_p2['respostas'].items():
                print(f'[{rchave2}]: {rvalor2}')

            resposta_usuario2 = input('Sua resposta:')

            if resposta_usuario2 == lista_p2['resposta_certa']:
                print(f'{GREENBG} Parabéns!!! Você acertou!!! {RESET}\n')
                respostas_certas2 += 1
                pontos += 2
                time.sleep(1.5)

            elif resposta_usuario2 != 'a' and resposta_usuario2 != 'b' and resposta_usuario2 != 'c':
                print(f'{REVERSE}{REDN}Não foi digitado uma alternativa válida. RESPOSTA ERRADA!{RESET}')
                time.sleep(1.5)

            else:
                print(f'{REDN} RESPOSTA ERRADA! {RESET}\n')
                time.sleep(1.5)

                print()
            qtd_perguntas2 = len(perguntas)
            porcentagem_acerto2 = (respostas_certas2 / qtd_perguntas2) * 100

        print(f'Você acertou {respostas_certas2} respostas.')
        print(f'Sua porcentagem de acerto foi de {porcentagem_acerto2}%.\n')


        if porcentagem_acerto2 > 80:
            nivel = 3
            print(f'{GREEN}Parabéns, você liberou o próximo nível! {RESET}\n')

        else:
            print('Infelizmente você não habilitou a próxima etapa. Tente novamente!')

        time.sleep(2)



    if nivel == 3:
        print('█ QUESTIONÁRIO NÍVEL 3 █')
        respostas_certas3 = 0
        perguntas3 = {
            'Questão 1': {
                'pergunta': """
    Márcia decidiu ofertar um lanche às pessoas em situação de rua na sua cidade. 
    Para isso, ela decidiu confeccionar sanduíches e foi até à padaria perto da sua casa, 
    onde o kg de pão francês custa R$ 12,00.
    
    Sabendo que Márcia possuía R$ 42,00 para comprar pães, quantos quilos ela conseguiu comprar? """,
                'respostas': {'a': '4,5 kg', 'b': '3,5 kg', 'c': '4 kg', },
                'resposta_certa': 'b', },

            'Questão 2': {
                'pergunta': '''
    Bruno gostaria de comprar um vídeo game, que a vista estava com 30% de desconto e, 
    por isso, diminuía R$ 60,00 do valor da compra. A outra forma de pagamento oferecida 
    pela loja era comprar no cartão em uma única parcela com 12% de desconto.
    
    Se Bruno escolheu pagar o vídeo game com o cartão, 
    qual o valor em reais do desconto concedido? ''',
                'respostas': {'a': 'R$ 24,00', 'b': 'R$ 18,00', 'c': 'R$ 22,00', },
                'resposta_certa': 'a', },

            'Questão 3': {
                'pergunta': '''
    Antônio possui uma hamburgueria com 5 entregadores. 
    Com a pandemia causada pelo coronavírus em 2020 e as medidas de confinamento na sua cidade 
    aumentaram o número de pedidos para entrega em casa e, por isso, ele contratou mais 8 entregadores.
    
    Sabendo que em média 5 entregadores no período de funcionamento 
    do estabelecimento entregavam 45 lanches, quantos pedidos a nova equipe 
    consegue atender fazendo o mesmo horário?''',
                'respostas': {'a': '166', 'b': '117', 'c': '130', },
                'resposta_certa': 'b', },

            'Questão 4': {
                'pergunta': '''
    Júlia é costureira e para confeccionar 8 saias do mesmo tamanho 
    utiliza de 16 metros de tecido. 
    
    Se ela recebeu uma encomenda de 22 saias para uma loja, 
    quantos metros de tecido ela precisa comprar?''',
                'respostas': {'a': '25', 'b': '44', 'c': '27', },
                'resposta_certa': 'b', },

            'Questão 5': {
                'pergunta': '''
    Maria deixará seu filho no cinema assistindo o novo filme 
    dos Super-Heróis Radicais enquanto compra algumas coisas no Shopping. 
    Ela já sabe que o filme tem 2h 17min, tempo suficiente para realizar as compras. 
    
    Transformando em segundos, o filme tem: ''',
                'respostas': {'a': '8220 s', 'b': '8100 s', 'c': '8150 s', },
                'resposta_certa': 'a', },


        }



        for p3, lista_p3 in perguntas3.items():
            print(f'{GREEN}{p3}:{RESET} {lista_p3["pergunta"]}')
            print('RESPOSTAS:')

            for rchave3, rvalor3 in lista_p3['respostas'].items():
                print(f'[{rchave3}]: {rvalor3}')

            resposta_usuario3 = input('Sua resposta:')

            if resposta_usuario3 == lista_p3['resposta_certa']:
                print(f'{GREENBG} Parabéns!!! Você acertou!!! {RESET}\n')
                respostas_certas3 += 1
                pontos += 3
                time.sleep(1.5)

            elif resposta_usuario3 != 'a' and resposta_usuario3 != 'b' and resposta_usuario3 != 'c':
                print(f'{REVERSE}{REDN}Não foi digitado uma alternativa válida. RESPOSTA ERRADA!{RESET}')
                time.sleep(1.5)

            else:
                print(f'{REDN} RESPOSTA ERRADA! {RESET}\n')
                time.sleep(1.5)

                print()
            qtd_perguntas3 = len(perguntas)
            porcentagem_acerto3 = (respostas_certas3 / qtd_perguntas3) * 100

        print(f'Você acertou {respostas_certas3} respostas.')
        print(f'Sua porcentagem de acerto foi de {porcentagem_acerto3}%.\n')
        time.sleep(1.5)

    ranking[player] = pontos  # Registro de pontos
    i = input('Deseja jogar novamente? [S/N]: ').upper()


nomes = sorted(ranking, key=ranking.get, reverse=True) #Organiza pontuação de forma decrescente
print(f'\n{REVERSE} {RESET}{REVERSE}{GREEN} Ranking Game {RESET}')
posicao = 1
for x in nomes:
    print(f'{posicao}º - {x} : {ranking[x]} pontos') #Mostra o Player e sua pontuação
    posicao +=1



