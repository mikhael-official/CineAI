from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from ai_engine import gerar_historia
from video_generator import gerar_video

class CineAI(BoxLayout):

    def gerar_filme(self):
        tema = self.ids.tema.text
        historia = gerar_historia(tema)
        video = gerar_video(historia)
        self.ids.resultado.text = "Filme criado: " + video

class CineAIApp(App):
    def build(self):
        return CineAI()

if __name__ == "__main__":
    CineAIApp().run()
