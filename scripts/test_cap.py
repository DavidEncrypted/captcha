from captcha import captcha
from fann2 import libfann
import os
from PIL import Image
ann = libfann.neural_net()
ann.create_from_file("./networks/network200.net")
letters = "abcdefghklmnprstuvwyzABDEFGHIJKLMNRTUXY23456789"

correct = 0
wrong = 0


def toInput(seg):
    input = []
    for x in range(seg.size[0]):
        for y in range(seg.size[1]):
            p = (x, y)
            col = seg.getpixel(p)

            norm = (((col / 255.00) * 2.00) - 1.00) * -1.00
            input.append(norm)
    return input

def use_ann(segs):

    #print len(segs)
    answer = ""
    #print answer
    for seg in segs:
        inputann = toInput(seg)
        outputann = ann.run(inputann)
        max = [-1, 0]
        for x in range(len(outputann)):
            if outputann[x] > max[0]:
                max = [outputann[x],x]
        #print max[0], max[1], letters[max[1]]
        #print letters[max[1]]
        answer += letters[max[1]]
        #print answer
    return answer


caps = os.listdir('./captchacol/')
capsolver = captcha.Captcha()
for f in caps:

    tempim = Image.open('./captchacol/{}'.format(f)).convert('L')
    capsolver.update_cap(tempim)
    capsolver.segment()
    answ = use_ann(capsolver.get_segments())
    correctAnswer = f[len(f) - 10: len(f) - 4].lower()
    if correctAnswer == answ.lower():
        #print 'correct!'
        correct += 1
    else:
        #print 'incorrect'
        wrong += 1
    if correct != 0:
        curpercent = float(correct) / float(correct + wrong) * 100.00
        print "Percentage right: {}".format(curpercent)