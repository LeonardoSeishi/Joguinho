
import PySimpleGUI as sg 

class Menu():
    def __init__(self):
        self.__interface = []
        self.__window = sg.Window('dinos',self.__interface ,font=("Helvetica", 37))
        sg.theme('DarkAmber')

    def tela_consulta(self):   
        self.__interface = [
            [sg.Text('',size = (5,1)),sg.Text('JOGUINHO',size=(14,1) )],
            [sg.Text('')],  
            [sg.Text('',size = (2,1)),sg.Button('INICIAR JOGO')],
            [sg.Text('',size = (2,1)),sg.Button('DIFICULDADE')],
            [sg.Text('',size = (2,1)),sg.Button('VER PONTUACAO')],
            [sg.Text('')],
            [sg.Text('',size = (6,1)),sg.Button('SAIR')]
         ]

        self.__window = sg.Window("Sistema Chat Bot", self.__interface ,font=("Helvetica", 14))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
