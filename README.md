# captcha


Structuur:

captcha Package:
    Ann.py  #class die het neurale netwerk implementeerd
    CapDisplay.py   #class die een manier van displayen van de captcha faciliteerd
    captcha.py      #class die het captcha object implementeerd, het belangrijkste object om uiteindelijk captcha's op te lossen
    Dataset.py      #class die de dataset verwerkt en bruikbaar maakt
    graphics.py     #class die het script gebruikt om captcha's te displayen (niet zelf gemaakt)
    segImage.py     #class die het segmenteren van captcha's faciliteerd
    Solver.py       #class die uiteindelijk moet worden gemaakt in een toepassing van de package

p_vs_c Folder:
    game.py         #alle code die het spel op de informatiemarkt heeft laten werken


scripts Folder:
    #alle scripts die ik heb gebruikt om mijn package toe te passen en zo captcha's op te lossen

setup.py    #voor het handig installeren van alle benuttigde libraries



Libraries:

BeautifulSoup 4         https://www.crummy.com/software/BeautifulSoup/
PILLOW                  https://python-pillow.org/
Numpy                   http://www.numpy.org/
Fast Artificial Neural Network      http://leenissen.dk/fann/wp/
graphics.py             http://mcsp.wartburg.edu/zelle/python/graphics.py



Installeren:

Installatie is erg lastig, de software gebruikt de externe lib fann, deze lib is erg moeilijk om te installeren omdat hij in C geschreven is en dit in python.
Voor al het andere installeren naast fann zijn dit de stappen:

als 'git' geinstalleerd op systeem:
    git clone https://github.com/DavidEncrypted/captcha.git
anders:
    ga naar https://github.com/DavidEncrypted/captcha/
    klik op 'clone or download'
        'Download ZIP'
    pak zip uit