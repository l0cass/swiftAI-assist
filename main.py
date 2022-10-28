import os
from playsound import playsound
from gtts import gTTS
import requests
import webbrowser

colorGray = '\33[7m'
colorGreen = '\033[1m'
colorReset = "\033[m"

gTTS(text='Olá, me chamo Julia! Sua assistente virtual.', lang='pt').save('helloWorld.mp3')
playsound('helloWorld.mp3')
os.remove('helloWorld.mp3')

def Main():
    chooseOption = int(input(f'\n\n{colorGreen}1{colorReset} {colorGray}-{colorReset} Cotações\n{colorGreen}2{colorReset} {colorGray}-{colorReset} Gravar Audio\n{colorGreen}3{colorReset} {colorGray}-{colorReset} Abrir Spotify\n{colorGreen}4{colorReset} {colorGray}-{colorReset} Assistir no Youtube\n{colorGreen}5{colorReset} {colorGray}-{colorReset} Pesquisar no Google\n\nEscolha: '))

    def chooseQuote():
        gTTS(text='Qual moeda deseja ver a cotação?', lang='pt').save('chooseQuote.mp3')
        playsound('chooseQuote.mp3')
        os.remove('chooseQuote.mp3')
        chooseAQuote = int(input(f'\n\n{colorGreen}1{colorReset} {colorGray}-{colorReset} Dólar\n{colorGreen}2{colorReset} {colorGray}-{colorReset} Euro\n{colorGreen}3{colorReset} {colorGray}-{colorReset} Voltar ao início\n\nEscolha: '))

        if chooseAQuote == 1:
            url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
            requestUrl = requests.get(url)
            responseJson = requestUrl.json()
            answer = float(responseJson['USDBRL']['high'])
            answer = f'{answer:.2f}'
            str(answer)

            gTTS(text=f'Ok. 1 Dólar americano é equivalente a {answer} Reais brasileiros.', lang='pt').save('dolarToday.mp3')
            playsound('dolarToday.mp3')
            os.remove('dolarToday.mp3')
            
            chooseQuote()

        elif chooseAQuote == 2:
            url = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL'
            requestUrl = requests.get(url)
            responseJson = requestUrl.json()
            answer = float(responseJson['EURBRL']['high'])
            answer = f'{answer:.2f}'
            str(answer)

            gTTS(text=f'Ok. 1 Euro é equivalente a {answer} Reais brasileiros.', lang='pt').save('euroToday.mp3')
            playsound('euroToday.mp3')
            os.remove('euroToday.mp3')
        
            chooseQuote()

        elif chooseAQuote == 3:
            Main()

        else:
            gTTS(text='Ops! Comando não identificado! Tente novamente com um dos números: 1, 2 e 3.', lang='pt').save('error.mp3')
            playsound('error.mp3')
            os.remove('error.mp3')
            chooseQuote()


    def recordAudio():
        gTTS(text='Ok. O Audio será gravado em português ou inglês?', lang='pt').save('recordLanguage.mp3')
        playsound('recordLanguage.mp3')
        os.remove('recordLanguage.mp3')
        recordLanguage = input("Audio: ")

        if recordLanguage == "Português" or recordLanguage == "português" or recordLanguage == "Portugues" or recordLanguage == "portugues":
            gTTS(text='Escreva o texto que irá ser gravado.', lang='pt').save('writeText.mp3')
            playsound('writeText.mp3')
            os.remove('writeText.mp3')

            recordingAudio = input("Gravando audio... ")
            gTTS(text=recordingAudio, lang='pt').save('recordingAudio.mp3')

            gTTS(text='Deseja reproduzir o audio?.', lang='pt').save('playAudio.mp3')
            playsound('playAudio.mp3')
            os.remove('playAudio.mp3')

            playAudio = input("Se deseja, digite: 'Sim'. Caso contrario: 'Não'.\n\nEscolha: ")

            if playAudio == "Sim" or playAudio == "sim":
                playsound("recordingAudio.mp3")
                Main()
            else:
                Main()

            recordAudio()

        elif recordLanguage == "Inglês" or recordLanguage == 'inglês' or recordLanguage == 'Ingles' or recordLanguage == 'ingles':
            gTTS(text='Escreva o texto que irá ser gravado.', lang='pt').save('writeText.mp3')
            playsound('writeText.mp3')
            os.remove('writeText.mp3')

            recordingAudio = input("Gravando audio... ")
            gTTS(text=recordingAudio, lang='en').save('recordingAudio.mp3')
            playAudio = input("Se deseja, digite: 'Sim'. Caso contrario: 'Não'.\n\nEscolha: ")

            if playAudio == "Sim" or playAudio == "sim":
                playsound('recordingAudio.mp3')
                Main()
            else:
                Main()

            recordAudio()

        else:
            gTTS(text='Comando não identificado! Tente novamente.', lang='pt').save('error.mp3')
            playsound('error.mp3')
            os.remove('error.mp3')
            recordAudio()

    def openSpotify():
        gTTS(text='Digite a Música barra Banda que deseja ouvir.', lang='pt').save('chooseMusic.mp3')
        playsound('chooseMusic.mp3')
        os.remove('chooseMusic.mp3')

        chooseMusic = input("Música/Banda: ")
        print('\n')
        webbrowser.open(f'https://open.spotify.com/search/{chooseMusic}', new=0, autoraise=True)
        
        gTTS(text='Abrindo Spotify...', lang='pt').save('openingSpotify.mp3')
        playsound('openingSpotify.mp3')
        os.remove('openingSpotify.mp3')

        Main()

    def openYoutube():
        gTTS(text='Digite o vídeo barra shorts que deseja assistir.', lang='pt').save('chooseYoutube.mp3')
        playsound('chooseYoutube.mp3')
        os.remove('chooseYoutube.mp3')

        chooseYoutube = input("Vídeo/Shorts: ")
        print('\n')
        webbrowser.open(f'https://www.youtube.com/results?search_query={chooseYoutube}', new=0, autoraise=True)
        
        gTTS(text='Abrindo Youtube...', lang='pt').save('openingYoutube.mp3')
        playsound('openingYoutube.mp3')
        os.remove('openingYoutube.mp3')

        Main()

    def searchOnGoogle():
        gTTS(text='Digite a sobre o que deseja pesquisar.', lang='pt').save('chooseGoogle.mp3')
        playsound('chooseGoogle.mp3')
        os.remove('chooseGoogle.mp3')

        chooseGoogle = input("Pesquisar... ")
        print('\n')
        webbrowser.open(f'https://www.google.com/search?q={chooseGoogle}', new=0, autoraise=True)
        
        gTTS(text='Pesquisando no Google...', lang='pt').save('openingGoogle.mp3')
        playsound('openingGoogle.mp3')
        os.remove('openingGoogle.mp3')

        Main()

    def error():
        gTTS(text='Comando não identificado! Tente novamente com um dos números: 1, 2 e 3.', lang='pt').save('error.mp3')
        playsound('error.mp3')
        os.remove('error.mp3')

    if chooseOption == 1:
        chooseQuote()

    elif chooseOption == 2:
        recordAudio()

    elif chooseOption == 3:
        openSpotify()

    elif chooseOption == 4:
        openYoutube()

    elif chooseOption == 5:
        searchOnGoogle()

    else:
        error()

Main()