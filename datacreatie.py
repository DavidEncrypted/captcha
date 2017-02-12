from captcha import captcha, Dataset
import random, time, sys

uur = 3600
begintijd = time.time()
aantaluur = float(sys.argv[2])


ds = Dataset.Dataset(sys.argv[1])
ds.get_header()
totaal = 0
savetime = 50
leng = 1
letters = ds.get_letters()
while True:
    for j in range(savetime):
        letter = letters[random.randint(0,len(letters) - 1)]
        cap = captcha.Captcha(sys.argv[3],1, 1, letter, leng)
        while cap.failure == 1:
            cap = captcha.Captcha(sys.argv[3], 1, 1, letter, leng)
        ds.segs_to_data(cap.get_segments(), letter)
    ds.save()


    totaal += savetime
    tijdverstreken = time.time() - begintijd
    if tijdverstreken > aantaluur * uur:
        break
    tijdtegaan = aantaluur * uur - tijdverstreken
    print "Totaal: {}".format(totaal) + " Tijd te gaan(min): {}".format(tijdtegaan / 60)

print "DONE! TotaalKlaar: {}".format(totaal)