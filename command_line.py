import captcha

from captcha import captcha, CapDisplay

disp = CapDisplay.CapDisplay(1200, 800)

allLetter = 'ABCDEFGHKLMNPRSTUVWXYZabcdefghklmnprstuvwyz23456789'
print len(allLetter)
for i in range(len(allLetter)):
    leng = 4
    if allLetter[i] == 'A' or allLetter[i] == 'f' or allLetter[i] == 'W':
        leng = 1
    cap = captcha.Captcha(1, 1, allLetter[i], leng)
    while cap.failure == 1:
        cap = captcha.Captcha(1, 1, allLetter[i], leng)

    disp.update_segs(cap.get_segments())
    disp.display_cap()
    disp.display_seg()

