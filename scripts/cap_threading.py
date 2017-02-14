from captcha import captcha, Dataset
import random, time, threading
from multiprocessing.pool import ThreadPool, ApplyResult

uur = 3600
begintijd = time.time()
aantaluur = 0.01


ds = Dataset.Dataset("prac_dataset.data")
ds.get_header()
totaal = 0
savetime = 5
leng = 1
letters = ds.get_letters()

prevseg = (0,0)
def getCaptchas():
    letter = letters[random.randint(0, len(letters) - 1)]
    cap = captcha.Captcha(1, 1, letter, leng)
    while cap.failure == 1:
        cap = captcha.Captcha(1, 1, letter, leng)

    segments = letter
    print "1"
    return letter


p = ThreadPool(processes=2)

result = p.apply_async(getCaptchas())



print result.get()
cyc = 0
while True:


    #ds.segs_to_data(segments[0], segments[1])



    ds.save()
    totaal += savetime
    tijdverstreken = time.time() - begintijd
    if tijdverstreken > aantaluur * uur:
        break
    tijdtegaan = aantaluur * uur - tijdverstreken
    #print "Totaal: {}".format(totaal) + " Tijd te gaan(min): {}".format(tijdtegaan / 60)

print "DONE! TotaalKlaar: {}".format(totaal)