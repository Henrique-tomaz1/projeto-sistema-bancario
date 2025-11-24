# Faça um programa em python que faça e reproduza um arquivo em mp3

# from gtts import gTTS

# texto = input('Digite o seu nome')
# if texto.endswith('a'):
#     prefixo = ('a')
# else:
#     prefixo = ('o')

# apresentação = (f'{texto} Seja muito bem vind{prefixo} ao programa do Henrique')
# tts = gTTS(apresentação, lang="pt")
# tts.save("audio.mp3")

import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1)
pygame.mixer.music.load('zz2.mp3') #nome do arquivo .mp3 salvo no pc
pygame.mixer.music.play() #play na musica


while pygame.mixer.music.get_busy():
    pass
