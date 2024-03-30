import pygame
from tkinter import *

musica1 = 'Empire-state'
musica2 = 'Tarzan'
musica3 = 'PassandoPelaProva'

def tocar_musica():
    pygame.init()
    pygame.mixer.music.load(f'{musica1}.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


def pause_musica():
    pygame.mixer.music.pause()
    
def retomar_musica():
    pygame.mixer.music.unpause()   



janela = Tk()
janela.title('Tocador de Música')
janela.geometry('100x200')
texto = Label(janela, text=musica1)
texto.grid(column=0, row=0, padx=25, pady=10)

botao = Button(janela, text='Play', command=tocar_musica)
botao.grid(column=0, row=1, padx=20, pady=10)
botao2 = Button(janela, text='Pausar', command=pause_musica)
botao2.grid(column=0, row=2, padx=20, pady=10)
botao3 = Button(janela, text='Retomar', command=retomar_musica)
botao3.grid(column=0, row=3, padx=20, pady=10)

janela.mainloop()