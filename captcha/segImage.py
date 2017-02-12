from PIL import Image, ImageFilter
import numpy, collections, sys

class segImage(Image.Image):

    # def __init__(self):
    #     Image.Image.__init__(self)

    def __init__(self, im, mode, size, palette, info, category, readonly, pyaccess):
        #Image.Image.__init__(self)
        sys.setrecursionlimit(3000)
        self.im = im
        self.mode = mode
        self.size = size
        self.palette = palette
        self.info = info
        self.category = category
        self.readonly = readonly
        self.pyaccess = pyaccess

    def get_groups(self, grpsize=10000, ignore_col = 0):
        groups = []
        #finished = []
        copy = self.copy()
        def floodfill(x, y, color):
            # "hidden" stop clause - not reinvoking for "c" or "b", only for "a".
            if copy.getpixel((x, y)) != 255  and (copy.getpixel((x, y)) == color or ignore_col):
                curgroup.append((x, y))
                #finished.append((x, y))

                copy.putpixel((x,y), 255)
                # recursively invoke flood fill on all surrounding cells:
                if x > 0:
                    floodfill(x - 1, y, color)
                if x < copy.size[0] - 1:
                    floodfill(x + 1, y, color)
                if y > 0:
                    floodfill(x, y - 1, color)
                if y < copy.size[1] - 1:
                    floodfill(x, y + 1, color)
        for x in range(copy.size[0]):
            for y in range(copy.size[1]):
                #if (x,y) in finished:
                #    break
                temp = copy.getpixel((x,y))
                if temp != 255:
                    curgroup = []
                    floodfill(x,y, temp)
                    if len(curgroup) < grpsize and len(curgroup) > 0:
                        groups.append(curgroup)

        return groups



    def remove_groups_touching_white(self):
        groups = self.get_groups(20)
        for group in groups:

            totWhi = 0
            for (x, y) in group:
                for (s, t) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    if (s > 0 and s < (self.size[0]) and t > 0 and t < (self.size[1])):
                        if (self.getpixel((s, t)) == 255):
                            totWhi += 1
            if (totWhi > 1):
                for (x, y) in group:
                    self.putpixel((x, y), 255)
            else:
                for (x, y) in group:
                    self.putpixel((x, y), 140)

    def color_whitelist(self, colors):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.getpixel((x,y)) not in colors:
                    self.putpixel((x,y),255)

    def remove_small_groups(self, upto):
        groups = self.get_groups(upto)

        for group in groups:

            for p in group:
                self.putpixel(p, 255)

    def collect_pixels(self, colors):
        collected = []
        for i in range(len(colors)):
            collection = []
            for x in range(self.size[0]):
                for y in range(self.size[1]):
                    if self.getpixel((x,y)) == colors[i]:
                        collection.append((x,y))
            collected.append(collection)
        return collected

    def get_line_letter_background_points(self):
        llbpoints = []
        letpoints = self.collect_pixels([140])[0]

        for (s, t) in letpoints:
            whi = 0
            lin = 0
            for (v, w) in (
            (s + 1, t), (s - 1, t), (s, t + 1), (s, t - 1), (s - 1, t - 1), (s + 1, t - 1), (s - 1, t + 1),
            (s + 1, t + 1)):
                if (v > 0 and v < (self.size[0] - 1) and (w > 0) and w < (self.size[1] - 1)):
                    if (self.getpixel((v, w)) == 255):
                        whi += 1
                    elif (self.getpixel((v, w)) == 112):
                        lin += 1
            if (whi > 0 and lin > 0):
                llbpoints.append((s, t))
        return llbpoints

    def get_line_letter_points(self):

        llpoints = []
        linepoints = self.collect_pixels([112])[0]
        llbpoints = self.get_line_letter_background_points()
        for (s, t) in linepoints:
            whi = 0
            let = 0
            for (v, w) in (
            (s + 1, t), (s - 1, t), (s, t + 1), (s, t - 1), (s - 1, t - 1), (s + 1, t - 1), (s - 1, t + 1),
            (s + 1, t + 1)):

                if (v > 0 and v < (self.size[0] - 1) and (w > 0) and w < (self.size[1] - 1)):
                    if (self.getpixel((v, w)) == 255):
                        whi += 1
                    elif (self.getpixel((v, w)) == 140):
                        let += 1
            if (whi == 0 and let > 1):

                bdc = 10000
                for (xc, yc) in llbpoints:
                    dx = abs(s - xc)
                    dy = abs(t - yc)
                    dc = (dx * dx) + (dy * dy)
                    if (dc < bdc): bdc = dc
                if (bdc > 2):
                    llpoints.append((s, t))
        return llpoints

    def grow_letter_into_line(self, distance,llpoints):
        endpoints = []
        for (rx, ry) in llpoints:
            lineCoords = []
            runt = 0
            if (self.getpixel((rx, ry)) == 112):
                lineCoords.append((rx, ry))
                temp = 0
                while (len(lineCoords) > 0 and runt < 10):
                    runt += 1
                    (x, y) = lineCoords[0]
                    for (s, t) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if (s >= 0 and s < (self.size[0]) and t >= 0 and t < (self.size[1] - 1)):
                            if (self.getpixel((s, t)) == 112):
                                dx = abs(s - rx)
                                dy = abs(t - ry)
                                dc = (dx * dx) + (dy * dy)
                                if (dc < distance):
                                    lineCoords.append((s, t))
                                    if runt > 4:
                                        temp = ((s, t), (x, y))
                    self.putpixel((x, y), 140)
                    lineCoords.pop(0)
                if temp != 0:
                    endpoints.append(temp)
        return endpoints
    def combine_groups(self, amount):
        groups = self.get_groups(ignore_col=1)
        if len(groups) < amount:
            return 0
        groups.sort(key=len)
        #for group in groups:
        while (len(groups) > amount):
            mx = []
            my = []
            for (s, t) in groups[0]:
                mx.append(s)
                my.append(t)
            medx = numpy.median(numpy.array(mx))
            medy = numpy.median(numpy.array(my))

            cdist = (1000, 0)
            for n in range(1, len(groups)):
                for coords in groups[n]:
                    x1 = medx
                    y1 = medy
                    x2 = coords[0]
                    y2 = coords[1]
                    tempdist = (abs(x1 - x2) ** 3) + ((abs(y1 - y2) ** 2) / 2)
                    if tempdist < cdist[0]:
                        cdist = (tempdist, n)
            groups[cdist[1]] = groups[0] + groups[cdist[1]]
            groups.pop(0)
            groups.sort(key=len)
        groups.sort(key=lambda tup: tup[0])


        return groups

    def to_black(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.getpixel((x,y)) == 140:
                    self.putpixel((x,y),0)
    def blur(self):
        im = self.filter(ImageFilter.SMOOTH_MORE)
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if (im.getpixel((x,y)) > 100):
                    im.putpixel((x,y),255)
        return Image_to_segImage(im)

def Image_to_segImage(im):
    return segImage(im.im,im.mode,im.size,im.palette,im.info,im.category,im.readonly,im.pyaccess)
