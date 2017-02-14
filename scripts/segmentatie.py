from captcha import CapDisplay, captcha


letters = "abcdefghklmnprstuvwyzABDEFGHIJKLMNRTUXY23456789"
cap = captcha.Captcha(do_seg=1, f_server=1, letter=letters, length=6)
while cap.failure == 1:
    cap = captcha.Captcha(do_seg=1, f_server=1, letter=letters, length=6)
    segs = cap.get_segments()
