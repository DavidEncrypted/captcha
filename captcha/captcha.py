#from PIL import Image, ImageDraw, ImageOps
from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup
from PIL import Image
from segImage import segImage, Image_to_segImage
import subprocess
from cStringIO import StringIO
import numpy
import time, math

#Global Captcha Object
class Captcha(object):

    def __init__(self, savefile="File1.jpg", do_seg=0, f_server=0,f_inter=0,  letter='', length=6):
        self.savefile = savefile
        if f_inter == 1:
            self.captchaf = self.retrieve_captcha()
            #print f_server
        elif f_server == 1:
            self.captchaf = self.get_from_server(letter, length)
        else:
            pass
            #self.captchaf = 0
        self.segments = []
        self.length = length
        self.letter = ''

        self.failure = 0


        if do_seg == 1:
            if self.segment() == 0:
                self.failure = 1

    def update_cap(self, cap):
        self.segments = []
        self.captchaf = Image_to_segImage(cap)
        #moet segImage zijn
    def retrieve_captcha(self):
        begin = time.time()
        html = urlopen("https://www.phpcaptcha.org/try-securimage/").read()
        soup = BeautifulSoup(html, "html.parser")
        images = [img for img in soup.findAll('img')]
        # print (str(len(images)) + " images found.")

        img = soup.select("#captcha_one")
        flink = img[0]["src"]

        ilink = "https://www.phpcaptcha.org"
        link = ilink + flink + ".jpg"
        # print (link)

        urlretrieve(link, self.savefile)
        im = Image.open(self.savefile).convert("L")
        seg_im = Image_to_segImage(im)
        end = time.time()
        #print "Retrieve time: {}".format(end - begin)
        return seg_im

    def get_from_server(self, letter, length):
        urlretrieve("http://localhost/securimage/securimage_show.php/?let={}&leng={}".format(letter, length), self.savefile)
        return Image_to_segImage(Image.open(self.savefile).convert("L"))
    def get_server2(self, letter, length):
        proc = subprocess.Popen("php /Applications/XAMPP/xamppfiles/htdocs/securimage/securimage_show2.php {} {}".format(letter, length), shell=True,
                                stdout=subprocess.PIPE)
        script_response = proc.stdout.read()
        print script_response
        buff = StringIO(script_response)
        return Image_to_segImage(Image.open(buff).convert('L'))

    def show_captcha(self):
        self.captchaf.show()

    def segment(self):
        #start = time.time()

        #self.captchaf.save('./stappen/pre_ruis.gif')
        self.captchaf.remove_groups_touching_white()
        #self.captchaf.save('./stappen/post_ruis.gif')
        self.captchaf.color_whitelist([140,112])
        self.captchaf.remove_small_groups(15)
        self.lineletterps = self.captchaf.get_line_letter_points()
        self.captchaf.grow_letter_into_line(10, self.lineletterps)

        self.captchaf.remove_small_groups(15)
        #self.captchaf.save('./stappen/post_lijn.gif')
        self.captchaf.color_whitelist([140])
        #self.captchaf.save('./stappen/post_lijn_list.gif')
        self.captchaf.to_black()
        self.captchaf = self.captchaf.blur()
        presegments =  self.captchaf.combine_groups(self.length)
        if presegments == 0:
            return 0
        self.finsegments(presegments)
        return 1

        #end = time.time()
        #print "Process time: {}".format(end - start)

    def finsegments(self, presegments):
        for i in range(len(presegments)):
            seg = presegments[i]
            minx = seg[0][0]
            maxx = seg[0][0]
            miny = seg[0][1]
            maxy = seg[0][1]

            for (x, y) in seg:
                if x > maxx:
                    maxx = x
                if x < minx:
                    minx = x
                if y > maxy:
                    maxy = y
                if y < miny:
                    miny = y
            xsize = 30
            dif = 0
            fdif = 0
            if maxx - minx + 1 > xsize:
                xsize = maxx - minx + 1
            else:
                dif = xsize - (maxx - minx + 1)
                fdif = int(math.floor(dif/2))
            image = Image.new("L", (xsize, maxy - miny + 1), 255)
            for (xsc, ysc) in seg:
                image.putpixel((xsc - minx + fdif, ysc - miny), self.captchaf.getpixel((xsc,ysc)))

            im = image.resize((30,30),Image.ANTIALIAS)
            self.segments.append(im)

    def show_segment(self, number):
        if number > len(self.segments):
            return
        self.segments[number].show()

    def get_segments(self):
        return self.segments
        #self.captchaf.

    def train_ann(self):
        pass

    def solve_with_ann(self):
        pass





