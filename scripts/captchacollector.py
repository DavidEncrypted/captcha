from urllib import urlretrieve
import random
from captcha import captcha
import subprocess
from cStringIO import StringIO
from PIL import Image
# proc = subprocess.Popen("php /Applications/XAMPP/xamppfiles/htdocs/securimage2/securimage_show.php", shell=True, stdout=subprocess.PIPE)
# script_response = proc.stdout.read()
# buff = StringIO(script_response)
# im = Image.open(buff)
# im.show()





def save_captcha(code, filename):
    urlretrieve("http://localhost/securimage2/securimage_show.php/?code={}".format(code), filename)

def genCode():
    code = ''
    letters = "abcdefghklmnprstuvwyzABDEFGHJKLMNRTUXY23456789"
    for i in range(6):
        code += letters[random.randint(0,len(letters) - 1)]
    #print code
    return code
for i in range(10000):
    code = genCode()
    save_captcha(code, './captchacol/{}-{}.jpg'.format(i, code))
    if i % 200 == 0:
        print i
