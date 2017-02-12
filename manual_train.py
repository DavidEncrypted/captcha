from captcha import CapDisplay, captcha

disp = CapDisplay.CapDisplay(1200, 800)
for i in range(2):
    cap = captcha.Captcha(do_seg=1)
    while cap.failure == 1:
        cap = captcha.Captcha(do_seg=1)

    disp.update_segs(cap.get_segments())
    disp.display_cap()
    disp.display_seg()







#cap.show_captcha()

