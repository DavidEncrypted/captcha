import random
from PIL import Image

class Dataset(object):
    def __init__(self, filename):
        try:
            self.file = open(filename, 'r+')
        except:
            open(filename, 'w').close()
            self.file = open(filename, 'r+')
        self.seg = 0
        self.location = 0
        self.filename = filename
        self.allLetters = "abcdefghklmnprstuvwyzABDEFGHIJKLMNRTUXY23456789"      #Geen:  C, I, J, O, P, Q, S, Z, i, j, o, q, x, 0, 1, V, W
        self.header = [0, 900, len(self.allLetters)]  # amount_data input_neurons output_neurons

    def get_letters(self):
        return self.allLetters


    def get_header(self):
        self.file.seek(0, 0)
        lines = self.file.readline()
        if len(lines.split()) == 3:
            self.header[0], self.header[1], self.header[2] = (int(x) for x in lines.split())
            print "Amount Data: {}  Input Neurons {}   Output Neurons {}".format(self.header[0], self.header[1], self.header[2])
            self.check_data()

        else:
            print "Non-Compatible file\n Creating new File and Header"
            self.file.seek(0, 0)
            if self.file.read(1) != 0:
                self.file.close()
                open(self.filename,'w').close()
                self.file = open(self.filename, 'r+')
            self.file.write("0 {} {}\n\n".format(self.header[1], self.header[2]))

    def check_data(self):
        self.file.seek(0,0)
        lines = 0
        fix = []
        for i, line in enumerate(self.file):
            #print line
            if line != "\n":
                if i != 0:
                    data = [[float(n) for n in line.split()]]
                    if len(data[0]) != 47 and len(data[0]) != 900:
                        print "IEEK" + str(len(data[0]))
                        fix.append(line)


                    lines += 1
        if len(fix) > 0:
            self.fix_lines(fix)

        dataamount = lines / 2
        print lines / 2, self.header[0]

        if dataamount != self.header[0]:
            self.header[0] = dataamount
            self.update_header()
            print "Updating header to: Amount Data: {}  Input Neurons {}   Output Neurons {}".format(self.header[0], self.header[1], self.header[2])

    def fix_lines(self, fix):
        self.file.seek(0,0)
        d = self.file.readlines()
        self.file.seek(0,0)
        nope = 0
        for i in d:

            for f in fix:
                if i == f:
                    nope = 4
            if nope == 0:
                self.file.write(i)
            else:
                nope -= 1
        self.file.truncate()

    def update_header(self):
        self.file.seek(0, 0)
        self.file.write(str(self.header[0]) + " " + str(self.header[1]) + " " + str(self.header[2]) + "\n\n")
        self.file.seek(0, 2)

    def save(self):
        self.update_header()
        self.file.close()
        self.file = open(self.filename,'r+')

    def get_test(self):
        self.file.seek(0,0)
        test = random.randint(1, self.header[0] - 1)
        im = Image.new('L', (30,30), 255)
        curl = 0
        for i, line in enumerate(self.file):
            if line != "\n":
                if i != 0:
                    if len(line) > 51 * 3:
                        if curl == test:
                            #print line
                            data = [[float(n) for n in line.split()]]
                            #print data
                            for x in range(im.size[0]):
                                for y in range(im.size[1]):
                                    pass
                                    precol = data[0][((x*30) + y)]
                                    col = int(round(((precol * -1) + 1) * (255 / 2)))
                                    im.putpixel((x, y), col)
                        curl += 1





                    #data = []
                    #data = [[int(n) for n in line.split(' ')]]
                    #print len(data), data[0]


        return im

    def segs_to_data(self, segs, letter):
        if isinstance(segs, list):
            for seg in segs:
                self.seg_to_data(seg, letter)
        else:
            self.seg_to_data(segs, letter)

    def seg_to_data(self, seg, letter):
        self.header[0] += 1
        self.file.seek(0, 2)
        for x in range(seg.size[0]):
            for y in range(seg.size[1]):
                p = (x, y)
                col = seg.getpixel(p)

                norm = (((col / 255.00) * 2.00) - 1.00) * -1.00

                self.file.write("{} ".format(norm))
        self.file.write("\n\n")
        for l in self.allLetters:
            if l == letter:
                self.file.write("1 ")
            else:
                self.file.write("-1 ")
        self.file.write("\n\n")
