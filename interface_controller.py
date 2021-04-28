from interface import Menu
import PySimpleGUI as sg 

class Menu_Controller:
    def __init__(self,lista:[]):
        self.__tela_inicial = Menu()
        #telas
        #dificuldade
        #ver pontuacao
        self.__bot = None
        self.__lista = lista


    def inicia(self):
        self.__tela_inicial.tela_consulta()
        rodando = True

        while rodando:
            event, values = self.__tela_inicial.le_eventos()

            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == 'INICIAR JOGO':
                #abrir jogo
                rodando = False

            elif event == 'DIFICULDADE':
                #abrir interface de dificuldades
                rodando = False

            elif event == 'VER PONTUACAO':
                #abrir interface de pontuação
                rodando = False

            elif event == 'SAIR':
                rodando = False

        self.__tela_inicial.fim()
