from captcha import CapDisplay, captcha
from fann2 import libfann
ann = libfann.neural_net()
ann.create_from_file("./networks/ann_fin.net")


def toInput(seg):
    input = []
    for x in range(seg.size[0]):
        for y in range(seg.size[1]):
            p = (x, y)
            col = seg.getpixel(p)

            norm = (((col / 255.00) * 2.00) - 1.00) * -1.00
            input.append(norm)
    return input

right = 0.00
wrong = 0.00
totaal = 1

disp = CapDisplay.CapDisplay(1200, 800)
letters = "abcdefghklmnprstuvwyzABDEFGHIJKLMNRTUXY23456789"

for i in range(totaal):
    cap = captcha.Captcha(do_seg=1, f_server=1, letter=letters, length=6)
    while cap.failure == 1:
        cap = captcha.Captcha(do_seg=1, f_server=1, letter=letters, length=6)
    segs = cap.get_segments()
    answers = []
    for seg in segs:
        inputann = toInput(seg)
        outputann = ann.run(inputann)
        max = [-1, 0]
        for x in range(len(outputann)):
            if outputann[x] > max[0]:
                max = [outputann[x],x]
        #print max[0], max[1], letters[max[1]]
        answers.append((letters[max[1]], max[0]))
    #print answers


    succes = disp.cap_seg(answers, segs)
    if succes == 1:
        right += 1.00
    else:
        wrong += 1.00
print "procent goed: " , right / totaal * 100

#disp.wait_click()




#cap.show_captcha()

