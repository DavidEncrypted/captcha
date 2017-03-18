Structuur:

captcha Package: 

Ann.py 
  Class die het neurale netwerk implementeerd 
CapDisplay.py 
  Class die een manier van displayen van de captcha faciliteerd 
captcha.py 
  Class die het captcha object implementeerd, het belangrijkste object om uiteindelijk captcha's op te lossen 
Dataset.py 
  Class die de dataset verwerkt en bruikbaar maakt 
graphics.py 
  Class die het script gebruikt om captcha's te displayen (niet zelf gemaakt) 
segImage.py 
  Class die het segmenteren van captcha's faciliteerd 
Solver.py
  Class die uiteindelijk moet worden gemaakt in een toepassing van de package
p_vs_c Folder:
 game.py
  Alle code die het spel op de informatiemarkt heeft laten werken
scripts Folder: 
  Alle scripts die ik heb gebruikt om mijn package toe te passen en zo captcha's op te lossen
setup.py 
  Voor het handig installeren van alle benuttigde libraries



Libraries:

  BeautifulSoup 4 https://www.crummy.com/software/BeautifulSoup/
   
  PILLOW https://python-pillow.org/ 

  Numpy http://www.numpy.org/

  Fast Artificial Neural Network http://leenissen.dk/fann/wp/

  graphics.py http://mcsp.wartburg.edu/zelle/python/graphics.py

Installeren:

Installatie is erg lastig, de software gebruikt de externe lib fann, deze lib is erg moeilijk om te installeren omdat hij in C geschreven is en dit in python. Voor al het andere installeren naast fann zijn dit de stappen:


Voor beginners(leraren):
installeer pip
https://bootstrap.pypa.io/get-pip.py
download get-pip.py
'python get-pip.py'
test pip door:
'pip version'

als 'git' geinstalleerd op systeem:
git clone https://github.com/DavidEncrypted/captcha.git 
anders: ga naar https://github.com/DavidEncrypted/captcha/ klik op 'clone or download' 'Download ZIP' pak zip uit
ga naar folder captcha
'cd C:/path/to/folder/captcha/'

Voor computervaardigen:
clone repository
gebruik pip om te installeren:
cd /path/to/clonedrepo/
'pip install ./'
alle gebruikte libs installeren nu zichzelf
installeer libfann:
https://pypi.python.org/pypi/fann2
installeer ook de C-versie
http://leenissen.dk/fann/wp/help/installing-fann/
klaar.

Om de captcha lib te gebruiken:
import captcha, PIL
solver = Solver.Solver()
captchaim = Image.load("captcha.jpg")
answer = solver.solve(captchaim)
print answer



