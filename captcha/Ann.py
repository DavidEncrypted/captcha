from fann2 import libfann
from fann2 import *
import copy

class NeuralNet(object):
    def __init__(self, layers, trainfile, trainfile2, saveto1, saveto2):
        self.layers = layers
        self.ann = self.create_ann()
        self.saveto1 = saveto1
        self.saveto2 = saveto2
        self.fullList = self.to_list(trainfile, trainfile2)
        self.trainlist = [self.fullList[0][0:(int(round(len(self.fullList[0]) / 20.00 * 19.00)))],self.fullList[1][0:(int(round(len(self.fullList[0]) / 20.00 * 19.00)))]]
        self.testlist = [self.fullList[0][(int(round(len(self.fullList[0]) / 20.00 * 19.00))):len(self.fullList[0])],
                          self.fullList[1][(int(round(len(self.fullList[0]) / 20.00 * 19.00))):len(self.fullList[0])]]
        print len(self.trainlist[0]), "train-full" , len(self.fullList[0])
        print len(self.testlist[0]), "test-full", len(self.fullList[0])

        print "read test1"



        self.repeats = 0
        self.epochs = 0
    def create_ann(self):
        ann = libfann.neural_net()
        ann.create_standard_array(self.layers)
        ann.set_learning_rate(0.7)
        ann.set_activation_function_output(libfann.SIGMOID_SYMMETRIC_STEPWISE)
        ann.set_activation_function_hidden(libfann.SIGMOID_SYMMETRIC_STEPWISE)
        ann.set_activation_steepness_hidden(0.4)
        ann.set_activation_steepness_output(0.4)
        return ann

    def to_list(self, trainfile, trainfile2):
        traindata = self.get_train_data(trainfile)
        print "Read 1"
        traindata2 = self.get_train_data(trainfile2)
        print "Read 2"
        traindata.merge_train_data(traindata2)
        print "Merged"
        return [traindata.get_input(),traindata.get_output()]

    def get_train_data(self, trainfile):
        traindata = libfann.training_data()
        traindata.read_train_from_file(trainfile)
        return traindata

    def full_train(self, parts, repeats):

        for i in range(parts):

            leng = len(self.trainlist[0])
            begin = int(round((float(leng) / float(parts)) * float(i)))
            size = int(round(float(leng) / float(parts)))


            partlist = [self.trainlist[0][begin:begin+size],self.trainlist[1][begin:begin+size]]


            #print "!!!", leng, len(self.trainlist[0])
            #print begin, size, "actualsize: ", len(partlist[0])
            self.repeats = 0
            for j in range(repeats):
                self.train_single(partlist, self.testlist)
                self.repeats += 1
            self.epochs += 1

        print "\n\nDone 1 full cycle!!!!\n\n\n"


    def single_epoch(self, trainl):
        for i in range(len(trainl[0])):
            self.ann.train(trainl[0][i],trainl[1][i])

    def train_single(self, train, test):

        self.single_epoch(train)

        print  "{}.{}: Train single MSE: ".format(self.epochs, self.repeats), self.ann.get_MSE(), self.ann.get_bit_fail()
        self.ann.reset_MSE()

        for i in range(len(test[0])):
            self.ann.test(test[0][i], test[1][i])
        print "{}.{}: Test single MSE: ".format(self.epochs, self.repeats), self.ann.get_MSE(), "Test Bit Fail: ", self.ann.get_bit_fail()
        self.ann.reset_MSE()


        if self.epochs % 10 == 0:
            self.ann.save(self.saveto1 + str(self.epochs) + self.saveto2)
