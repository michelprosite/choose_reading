from random import randint
import datetime

chapter = '/home/kalimss/Documentos/choose_reading/chapter.txt'
chapter_dc = 138 # Aqui é definida o total de capítulos do livro
data = '/home/kalimss/Documentos/choose_reading/data_control.txt'
data_atual_str = datetime.date.today().strftime('%Y-%m-%d')

with open(chapter, 'r') as arquivo:
    conteudo = arquivo.read()
    n_chapter = conteudo.split()
    if n_chapter != []:
        anterior = n_chapter[-1]
    else:
        anterior = str("Não há registro de leitura anterior!")

with open(data, 'r') as today:
    day = today.read().strip()  
    if day != data_atual_str:
        with open(data, 'w') as today:
            today.write(data_atual_str)    

        random_chapter = randint(1, chapter_dc)
        random_chapter_str = str(random_chapter) 

        if random_chapter_str not in n_chapter:
            n_chapter.append(random_chapter_str)

            with open(chapter, 'w') as arquivo:
                arquivo.write(' '.join(n_chapter))
        print(f'A leitura anterior foi Capítulo: {anterior}')
        print(f'A leitura de hoje é Capítulo: {random_chapter}')
    else:
        if len(n_chapter) >= 2:
            print(f'A leitura anterior foi Capítulo: {n_chapter[-2]}')
        else:
            print('Não há registro de leitura anterior!')
        
        print(f'A leitura de hoje é Capítulo: {n_chapter[-1]}')