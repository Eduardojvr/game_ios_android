from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Game(App):
    def build(self):
        self.cl_jogador_1 = '0'
        self.cl_jogador_2 = '0'

        box = BoxLayout(orientation='horizontal')

        button1 = Button(text='Jogador 1', font_size=30, on_release=self.incrementa_1)
        button2 = Button(text='Jogador 2', font_size=30, on_release=self.incrementa_2)


        self.label1 = Label(text=self.cl_jogador_1, font_size=30)
        self.label2 = Label(text=self.cl_jogador_2, font_size=30)

        box.add_widget(button1)
        box.add_widget(self.label1)

        box.add_widget(self.label2)
        box.add_widget(button2)        

        return box
    
    def incrementa_1(self, button):
        self.label1.text =str(int(self.label1.text)+1)
    
    def incrementa_2(self, button):
        self.label2.text =str(int(self.label2.text)+1)


## Main
Game().run()