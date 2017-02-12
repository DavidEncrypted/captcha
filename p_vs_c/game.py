import pyglet
import os, random
import time, socket
class game(object):



    def __init__(self):

        platform = pyglet.window.get_platform()
        display = platform.get_default_display()
        pyglet.clock.schedule_interval(self.draw, 1 / 60.0)
        self.screens = display.get_screens()
        self.main = pyglet.window.Window()
        self.second = pyglet.window.Window()
        self.setupWindows()
        self.background = pyglet.image.load('./p_vs_c/backg3.jpg')
        self.gameState = 0
        self.fadein = 0
        self.frame = 0
        self.setup = 1
        self.solved = 0
        self.wrong = 0
        self.correct = 2
        self.countdown = 10
        self.stoptijd = 0
        self.starttimer = 1
        self.currentCode = ''
        self.correctCode = ''
        self.startCap = 10
        self.einde = 0
        self.currentCaptcha = pyglet.sprite.Sprite(pyglet.image.load('File1.jpg'))
        self.begintijd = 1.00
        self.captchacolcont = os.listdir('./captchacol/')
        print self.captchacolcont[len(self.captchacolcont) - 10: len(self.captchacolcont)]
        pyglet.app.run()




    def setupWindows(self):
        self.main.on_draw = self.on_draw_main
        self.main.on_mouse_press = self.on_mouse_pressed_main
        self.main.on_key_press = self.on_key_press_main
        self.main.set_fullscreen(screen=self.screens[1], width=1440, height=900)
        self.main.set_location(-1440, 0)
        #self.main.ge
        self.main.on_text = self.on_text_main
        self.second.on_text = self.on_text_main
        self.second.on_draw = self.on_draw_second
        self.second.on_mouse_press = self.on_mouse_pressed_second

        self.second.set_fullscreen(screen=self.screens[0])
        self.second.on_key_press = self.on_key_press_main

    def reset(self):
        self.gameState = 0
        self.fadein = 0
        self.frame = 0
        self.setup = 1
        self.solved = 0
        self.wrong = 0
        self.correct = 2
        self.countdown = 10
        self.stoptijd = 0
        self.starttimer = 1
        self.currentCode = ''
        self.correctCode = ''
        self.startCap = 10
        self.einde = 0

    def sendStart(self):
        self.startCap = random.randint(0,len(self.captchacolcont) - 1)

        server_address = ('192.168.43.219', 10001)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(server_address)
            s.sendall(str(self.startCap))
        except:
            print "NOOOO"

    def draw_text(self, text, x, y, color, size):
        label = pyglet.text.Label(text,
                                   font_name='Ariel',
                                   font_size=size,
                                   x=x, y=y,
                                   anchor_x='center', anchor_y='center')
        label._set_color(color)
        label.draw()



    def on_mouse_pressed_main(self, x, y, button, modifiers):
        pass
        #self.main.close()
        #self.second.close()

    def on_mouse_pressed_second(self, x, y, button, modifiers):
        pass
        #self.second.close()
        #self.main.close()


    def on_key_press_main(self, symbol, modifiers):
        #print pyglet.window.key.ESCAPE
        if symbol == pyglet.window.key.ESCAPE:
            self.main.close()
            self.second.close()
        elif symbol == pyglet.window.key.SLASH:
            self.reset()

        elif symbol == pyglet.window.key.ENTER:
            if self.gameState == 0:
                self.sendStart()
                self.gameState = 3
            elif self.gameState == 1:
                self.currentCode = ''
        elif symbol == pyglet.window.key.BACKSPACE:
            if self.gameState == 1:
                if len(self.currentCode) > 0:
                    self.currentCode = self.currentCode[0 : len(self.currentCode) - 1]

    def on_text_main(self, text):
        if self.gameState == 1:

            if text != ' ':
                self.currentCode += text

    def display_opening(self):
        self.background.blit(0,0)
        if self.fadein < 255:
            self.fadein += 8
            if self.fadein > 255:
                self.fadein = 255

        self.draw_text('Mens Vs. Computer', self.main.width // 2, self.main.height // 4 * 3, (140, 134, 163,self.fadein), 80)

        if self.fadein == 255:
            self.draw_text('Druk op enter om te beginnen', self.main.width // 2, self.main.height // 8 * 3, (140, 134, 163, 255), 40)


    def update_captcha(self):
        #print self.captchacolcont
        print self.startCap
        lengs = len(str(self.startCap))
        name = ''
        for cap in self.captchacolcont:
            if cap[:lengs] == str(self.startCap):
                name = cap
                print name, self.startCap



        temp = pyglet.image.load('./captchacol/{}'.format(name))
        captext = (name)
        self.correctCode =  captext[len(captext) - 10: len(captext) - 4].lower()
        print self.startCap, self.correctCode
        self.currentCaptcha = pyglet.sprite.Sprite(temp)
        self.currentCaptcha.scale = 4.0
        self.startCap += 1
    def display_captcha(self, win):
        self.currentCaptcha.set_position(win.width / 2 - (self.currentCaptcha.width / 2),win.height / 8 * 5 - (self.currentCaptcha.height / 2) )
        self.currentCaptcha.draw()

    def on_draw_main(self):
        pyglet.gl.glClearColor(112, 112, 112, 255)
        self.main.clear()

        if self.gameState == 0:
            self.display_opening()

        elif self.gameState == 3:
            if self.starttimer == 1:

                self.stoptijd = time.time() + 5
                self.starttimer = 0
            gettime = round(self.stoptijd - time.time(), 1)
            if gettime <= 1:
                self.begintijd = time.time()
                self.gameState = 1
            self.draw_text(str(gettime), self.main.width / 2, self.main.height / 2, (100,100,100,255),300)

        elif self.gameState == 1:

            if self.setup == 1:
                self.update_captcha()

                self.setup = 0
            self.display_captcha(self.main)

            self.draw_text(self.currentCode, self.main.width / 2, 100, (255,0,0,255), 150)
            if len(self.currentCode) >= 6:
                if self.currentCode.lower() == self.correctCode:
                    self.solved += 1
                    self.update_captcha()
                    self.correct = 1
                else:
                    self.correct = 0
                    self.update_captcha()
                self.currentCode = ''
            if self.correct == 0:
                self.draw_text('Fout!', self.main.width / 2, self.main.height - 100, (255, 0, 0, 255), 100)
            elif self.correct == 1:
                self.draw_text('Correct!', self.main.width / 2, self.main.height - 100, (0, 255, 0, 255), 100)

            if self.solved == 10:
                self.gameState = 2
            # self.gameSetup()
            # self.sendCap()
            # self.showCountdown()
            # while game_not_over:
            #    self.showCap()
            #    self.getKeys
            #    self.keys == 6
            #    if self.checkcap(keys):        #correct
            #       righttot += 1
            #    else:
            #       wrongtot += 1
            #    if righttot == 10:
            #       game_over


        elif self.gameState == 2:
            if self.einde == 0:
                self.eindtijd = time.time()
                self.einde = 1

            self.draw_text('Done!', self.main.width / 2, self.main.height / 2 + 50, (140,140,140,255),250)
            self.draw_text(str(round(self.eindtijd - self.begintijd, 3)), self.main.width / 2, self.main.height / 2 -300, (140, 140, 140, 255), 150)


    def on_draw_second(self):
        pyglet.gl.glClearColor(112, 128, 144, 255)
        self.second.clear()
        if self.gameState == 0 and self.fadein == 255:
            self.draw_text('Mens', self.second.width / 2, self.second.height / 2, (140, 140, 140, 255), 250)
        if self.gameState == 1:

            self.draw_text('Opgelost:', self.second.width // 2, self.second.height // 8 * 5, (140, 134, 163, 255), 200 )
            self.draw_text(str(self.solved) + '/10', self.second.width // 2, self.second.height // 8 * 3, (140, 134, 163, 255), 200)

        if self.gameState == 2:
            self.draw_text('Verliezer!', self.second.width / 2, self.second.height / 2, (140, 140, 140, 255), 250)


    def draw(self, time):
        self.frame = time
