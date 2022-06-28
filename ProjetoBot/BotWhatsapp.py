from selenium import webdriver
import time
import pyautogui

class WhatsappBot:
    def __init__(self):
        self.mensagem = "teste do bot"
        self.grupos = ["Eu"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        self.driver.get('https://www.web.whatsappweb.com')
        time.sleep(30)
        # <span dir="auto" title="Eu" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Eu</span>
        # <div tabindex="-1" class="p3_M1">

        grupo = self.driver.find_element_by_path("//span[@title='Eu']")
        time.sleep(3)
        grupo.click()
        chat_box = self.driver.find_element_by_class_name('_13mgZ')
        time.sleep(3)
        chat_box.click()
        chat_box.send_keys(self.mensagem)
        time.sleep(3)
        pyautogui.press('Enter')

bot = WhatsappBot()
bot.EnviarMensagens()