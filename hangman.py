import os
import random
import msvcrt


def run():
    with open('./files/data.txt', 'r', encoding='utf-8') as f:
        words_list = [i[0:-1] for i in f]
    

    with open('./files/ascii_draw.txt', 'r', encoding='utf-8') as f:
        draw = [i[0:-1] for i in f]
    

    def normalize(word):
        replacements = {
            'á': 'a',
            'é': 'e',
            'í': 'i',
            'ó': 'o',
            'ú': 'u'
            }

        for i, j in replacements.items():
            word = word.lower().replace(i, j)
        return word
    

    def word_generator():
        word = words_list[random.randint(0, len(words_list))]
        hidden_word = [{'position':k, 'letter':v, 'visible':False} for (k,v) in list(enumerate(word))]
        return hidden_word
    

    def comprobation(letter):
        find = False

        for i in hidden_word:
            if normalize(i.get('letter')) == normalize(letter) and i.get('visible') == False:
                i['visible'] = True
                find = True
        
        return find
    

    def word_show(dict):
        word_list = ['_' if not(i.get('visible')) else i.get('letter') for i in dict]
        return word_list
    

    def drawing(attemp):
        for i in range(attemp * 20, attemp * 20 + 19):
            print(draw[i])
    

    def info_screen(case):
        os.system('clear')
        print('Adivina la palabra', '', sep='\n')
        print('============== Nivel ', str(level), ' ==============')
        drawing(attemps)
        print('Palabra:  ', ' '.join(word_show(hidden_word)), '\n\n', 'Ingresa una letra')
        if case == 'type_error':
            print('Solo se permiten letras')
        elif case == 'next_level_option':
            print(
                '¿Listo para el siguiente nivel?',
                'Ingresa "y" para continuar o "n" para salir',
                sep='\n\n'
                )
        elif case == 'new_game':
            print('La palabra era: ', ''.join([i.get('letter') for i in hidden_word]))
            print(
                '',
                '============= Game Over =============', 
                '¿Quieres jugar de nuevo?',
                'Ingresa "y" para continuar o "n" para salir',
                sep='\n\n'
                )


    def next_game_comprobation(status):
        response = str(msvcrt.getch())[2:3]
        while response != 'y' and response != 'n':
            info_screen(status)
            response = str(msvcrt.getch())[2:3]
        
        if response == 'y':
            return 'y'
        elif response == 'n':
            return 'n'

    
    hidden_word = word_generator()
    attemps = 0
    level = 1
    status = 'actual_game'

    info_screen(0)
    
    while True:

        letter = str(msvcrt.getch())[2:3]
        if not(letter.isalpha()):
            info_screen('type_error')
        elif comprobation(letter):
            info_screen(0)
        else:
            attemps += 1
            info_screen(0)

        if len(list(filter(lambda x : x.get('visible') == False, hidden_word))) == 0:
            info_screen('next_level_option')

            response = next_game_comprobation('next_level_option')
            
            if response == 'y':
                status = 'won'
            elif response == 'n':
                break
    
        if attemps == 9:
            info_screen('new_game')

            response = next_game_comprobation('new_game')
            
            if response == 'y':
                status = 'lost'
            elif response == 'n':
                break
        
        if status != 'actual_game':
            hidden_word = word_generator()
            attemps = 0
            if status == 'lost':
                level = 1
            elif status == 'won':
                level +=1
            info_screen(0)
            status = 'actual_game'

            

    print('\n', '=========== Gracias por Jugar ===========')


if __name__ == '__main__':
    run()
