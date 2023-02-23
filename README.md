This repo contains the code for my highschool graduation project. This was written in 2017 when I was 17.
The goal was to create a python library that is capable of breaking the [SecurImage CAPTCHA](https://www.phpcaptcha.org/).
The code in this repo is capable of generating the right answer to the captcha about 1 in 7 attempts. This is very usable as the securimage captcha instantly generates a new attempt. Also the code is very simple and thus very quick.

![Example Captcha](captcha.png)

## Example application of captcha lib:

https://github.com/DavidEncrypted/alphabreak


# Structure

captcha Package: 

```
Ann.py 
  Class that implements the neural network 
CapDisplay.py 
  Class facilitates displaying the captcha
captcha.py 
  Class that implements the captcha object, the main object to eventually solve captchas 
Dataset.py 
  Class that processes the dataset and makes it usable 
graphics.py 
  Class that uses the script to display captchas (not created by myself) 
segImage.py 
  Class that facilitates the segmentation of captchas 
Solver.py
  Class that must eventually be created in an application of the package
p_vs_c Folder:
 game.py
  All the code that made the game work on the information market
scripts Folder: 
  All the scripts I used to apply my package to solve captchas
setup.py 
  For convenient installation of all utilized libraries
```


Libraries:

  BeautifulSoup 4 https://www.crummy.com/software/BeautifulSoup/
   
  PILLOW https://python-pillow.org/ 

  Numpy http://www.numpy.org/

  Fast Artificial Neural Network http://leenissen.dk/fann/wp/

  graphics.py http://mcsp.wartburg.edu/zelle/python/graphics.py

# Install

Installation is very difficult for not tech people, the software uses the external lib fann, this lib could be very difficult to install because it is written in C and this in python.


For beginners(teachers):
```
# Install pip
https://bootstrap.pypa.io/get-pip.py
# download get-pip.py
python get-pip.py
#test pip with
pip version

# if 'git' is installed on systeem:
git clone https://github.com/DavidEncrypted/captcha.git 
# else: ga naar https://github.com/DavidEncrypted/captcha/ klik op 'clone or download' 'Download ZIP' pak zip uit
# cd to folder captcha
cd C:/path/to/folder/captcha/
```

For computer savvy people:
```
# clone repository
# use pip to install:
cd /path/to/clonedrepo/
pip install ./

# install libfann:
https://pypi.python.org/pypi/fann2
# install the C-version
http://leenissen.dk/fann/wp/help/installing-fann/
```
# Usage
```
import captcha, PIL

solver = Solver.Solver()

captchaim = Image.load("captcha.jpg")

answer = solver.solve(captchaim)

print answer
```


