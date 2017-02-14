from captcha import Captcha
from fann2 import libfann


class Solver(object):

    def __init__(self, network):
        self.ann = libfann.neural_net()
        self.ann.create_from_file("./networks/{}".format(network))
        self.cap_segmenter = Captcha()
        self.letters = "abcdefghklmnprstuvwyzABDEFGHIJKLMNRTUXY23456789"

    def solve_cap(self, captcha):
        self.cap_segmenter.update_cap(captcha)
        self.cap_segmenter.segment()
        segs = self.cap_segmenter.get_segments()
        answer = self.use_ann(segs)
        return answer

    def to_input(self, seg):
        input = []
        for x in range(seg.size[0]):
            for y in range(seg.size[1]):
                p = (x, y)
                col = seg.getpixel(p)
                norm = (((col / 255.00) * 2.00) - 1.00) * -1.00
                input.append(norm)
        return input

    def use_ann(self, segs):
        answer = ''
        for seg in segs:
            input = self.to_input(seg)
            output = self.ann.run(input)
            max = [0, -1]
            for x in range(len(output)):
                if output[x] > max[0]:
                    max = (output[x], x)
            answer += self.letters[max[1]]
        return answer
