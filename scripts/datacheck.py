from captcha import captcha, Dataset, CapDisplay
import random, time, sys

dis = CapDisplay.CapDisplay(1200, 800)
ds = Dataset.Dataset(sys.argv[1])
ds.get_header()
segs = []
for i in range(5):
    segs.append(ds.get_test())
dis.update_segs(segs)
dis.display_seg(0)
dis.wait_click()
