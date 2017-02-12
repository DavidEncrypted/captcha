import captcha

from captcha import captcha, CapDisplay

disp = CapDisplay.CapDisplay(1200, 800)

letter = "sS"
leng = 4
while True:
    cap = captcha.Captcha(1, 1, letter, leng)
    while cap.failure == 1:
        cap = captcha.Captcha(1, 1, letter, leng)

    disp.update_segs(cap.get_segments())
    disp.display_cap()
    disp.display_seg()

