from segImage import segImage
from PIL import Image
from graphics import *

class CapDisplay(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.nummerY = 0
        self.nummerX = 0
        self.segments = []
        self.win = GraphWin(width=self.w, height=self.h)
        self.win.setCoords(0,0,self.w,self.h)
        self.answers = []


    def update_segs(self, segments):
        self.segments = segments

    def clear_backg(self):
        self.win.close()
        self.win = GraphWin("Breaking Captcha's", self.w, self.h)
        self.win.setCoords(0, 0, self.w, self.h)

    def display_seg(self, answers,disX=250, disY = 40, w_input=0):


        cSegX = 30 + (disX*self.nummerX)


        cSegY = self.nummerY * disY
        for i in range(len(self.segments)):
            self.segments[i].save("temp.gif")

            seg = Img(Point(self.segments[i].size[0] / 2 + (cSegX),self.h - (50) - cSegY), "temp.gif")
            seg.draw(self.win)
            lin = Line(Point(self.segments[i].size[0] + (cSegX), self.h - (50) - cSegY),
                       Point(self.segments[i].size[0] + (cSegX), self.h - (50) - cSegY + 20))
            lin.draw(self.win)
            lin2 = Line(Point((cSegX), self.h - (50) - cSegY),
                       Point((cSegX), self.h - (50) - cSegY + 20))
            lin2.draw(self.win)

            if answers != 0 and i < 6:
                text = Text(Point(self.segments[i].size[0] / 2 + (cSegX), self.h - (50) - cSegY - 20), "")
                text.setText(answers[i][0])
                text.setSize(10)
                text.draw(self.win)
                text2 = Text(Point(self.segments[i].size[0] / 2 + (cSegX), self.h - (50) - cSegY - 35), "")
                text2.setText(round(answers[i][1], 3))
                text2.setSize(10)
                text2.draw(self.win)
            if w_input == 1:
                text = Text(Point(self.segments[i].size[0] / 2 + (cSegX),self.h - (50) - cSegY - 20), "")
                failtext = Text(Point(self.w - 120, self.h - 50), "")
                failtext.setSize(15)
                shift = 0
                while True:
                    let = self.win.getKey()
                    if let == "??":
                        if shift == 0:
                            shift = 1
                            failtext.setText("SHIFT")
                            failtext.draw(self.win)

                        else:
                            shift = 0
                            failtext.undraw()
                    else:
                        break
                failtext.undraw()
                if shift == 1:
                    for l in "abcdefghijklmnopqrstuvwxyz":
                        if let == l:
                            let = let.upper()


                self.answers.append(let)
                text.setText(let)
                text.setSize(10)
                text.draw(self.win)

            cSegX += self.segments[i].size[0] + 10
        if w_input == 1:
            suretext = Text(Point((cSegX) + 150,self.h - (50) - cSegY - 50), "Zeker over deze letters?\n\"c\"(lear) bij een foutje\n\"enter\" wanneer alles correct is")
            suretext.setSize(15)
            suretext.draw(self.win)

            while True:
                let = self.win.getKey()
                if let == "c":
                    self.display_seg()
                    suretext.undraw()
                elif let == "Return":
                    suretext.undraw()
                    break

        self.nummerY += 1
        if self.nummerY > 12:
            self.nummerY = 0
            self.nummerX += 1
            if self.nummerX >= 5:
                self.win.getMouse()
    def display_cap(self):


        Image.open("File1.jpg").save("tempcap.gif")

        captcha = Img(Point(self.w / 2, 50), "tempcap.gif")
        captcha.draw(self.win)

    def cap_seg(self, answers, segs):

        ims = Image.open("File1.jpg")
        ims.save("tempcap.gif")

        captcha = Img(Point(ims.size[0] / 2 + 10 + (self.nummerX * 500), self.h - (50) - (self.nummerY * 100)),
                      "tempcap.gif")
        captcha.draw(self.win)
        for i in range(len(answers)):
            text = Text(Point((ims.size[0]) + 130 + (self.nummerX * 500) - 100 + (i * 35), self.h - (75) - (self.nummerY * 100)), "")
            text.setText((answers[i][0]).lower())
            text.setSize(15)
            text.draw(self.win)


            segs[i].save("temp.gif")

            seg = Img(Point((ims.size[0]) + 130 + (self.nummerX * 500) - 100 + (i * 35), self.h - (50) - (self.nummerY * 100)), "temp.gif")
            seg.draw(self.win)

        key = self.win.getKey()
        #self.nummerX += 1
        self.nummerY += 1
        if self.nummerY > 6:
            self.nummerY = 0
            self.nummerX += 1
        if self.nummerX >= 2:
            self.nummerX = 0
            self.nummerY = 0
            self.clear_backg()

        if key == "Return":
            return 1
        else:
            return 0

    def only_cap(self, answers):
        ims = Image.open("File1.jpg")
        ims.save("tempcap.gif")

        captcha = Img(Point(ims.size[0] / 2 + 40 + (self.nummerX * 400), self.h - (50) - (self.nummerY * 100)),
                      "tempcap.gif")
        captcha.draw(self.win)
        for i in range(len(answers)):
            text = Text(Point(ims.size[0] / 2 + 40 + (self.nummerX * 300) - 100 + (i * 20),
                              self.h - (50) - (self.nummerY * 100) - (ims.size[1] / 2) - 10), "")
            text.setText((answers[i][0]).lower())
            text.setSize(15)
            text.draw(self.win)

        # self.nummerX += 1
        self.nummerY += 1
        if self.nummerY > 6:
            self.nummerY = 0
            self.nummerX += 1
        if self.nummerX > 2:
            self.nummerX = 0
            self.nummerY = 0
            self.clear_backg()
        key = self.win.getKey()
        if key == "Return":
            return 1
        else:
            return 0
    def wait_click(self):
        self.win.getMouse()

