import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.switch import Switch
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.clipboard import Clipboard
import os
import random
from googletrans import Translator
from gtts import gTTS
import time

Window.size = (480, 620)
Window.clearcolor = (153/255, 161/255, 1, 1)



class StartScreen(Screen):
    pass


class MainScreen(Screen):
    def wait(self):
        self.state1.text = "Wait.."
    def btn(self):
        self.state1.text = "Click to convert"
        global x                                  # x will hold the text converted from english
        englishEntered = self.english.text
        frenchT = self.french.text
        translator = Translator()
        x = self.french.text = (translator.translate(self.english.text, dest='fr')).text
        self.copybtn.disabled = False

    def switch_callback(self, switchObject, switchValue):
        print("switch 1 is pressed")

    def wait2(self):
        self.state2.text = "Wait.."
    def btn1(self):
        self.state2.text = "Save and play audio"
        fSwitch = self.firstSwitch.active
        if (fSwitch is False):
            tts = gTTS(x, lang='fr', slow=False)
        else:
            tts = gTTS(x, lang='fr', slow=True)
        tts.save('french.mp3')
        os.startfile('french.mp3')
        self.english.text = ""

    def copy(self):
        Clipboard.copy(self.french.text)


class AnotherScreen(Screen):
    def switch_callback2(self, switchObject, switchValue):
        print("Switch 2 is pressed")

    def wait(self):
        self.state3.text = "Wait.."

    def btn2(self):
        self.state3.text = "Save and play audio"
        fi = self.frenchInput2.text
        sSwitch = self.secondSwitch.active
        if (sSwitch is False):
            tts = gTTS(fi, lang='fr', slow=False)
        else:
            tts = gTTS(fi, lang='fr', slow=True)
        tts.save('french.mp3')
        os.startfile('french.mp3')


class FinalScreen(Screen):
    def wait(self):
        self.info1.text = "Please Wait.."

    def generator(self):
        array = []
        global phoneNo
        for i in range(5):
            number = int(random.randrange(10, 99))
            array.append(number)

        phoneNo = "   ".join(str(x) for x in array)
        print(phoneNo)
        tts = gTTS(phoneNo, lang='fr', slow=True)
        tts.save("phoneNumber.mp3")
        self.disab1.disabled = False
        self.info1.text = "Numbers are generated"



    def playAudio(self):
        os.startfile("phoneNumber.mp3")

    def showNumbers(self):
        self.sho1.text = phoneNo


    def clear(self):
        self.disab1.disabled = True
        self.info1.text = "."
        self.sho1.text = "."



class ScreenManagement(ScreenManager):
    pass



presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        self.title = "FrenchAudioApp"
        self.icon = "images/france.png"
        return presentation

if __name__ == "__main__":
    MainApp().run()