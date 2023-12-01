from binary_perceptron import BinaryPerceptron # Your implementation of binary perceptron
from plot_bp import PlotBinaryPerceptron
import csv  # For loading data.
from matplotlib import pyplot as plt  # For creating plots.
import remapper


class PlotRingBP(PlotBinaryPerceptron):

    IS_REMAPPED = True
    def __init__(self, bp, plot_all=True, n_epochs=20):
        super().__init__(bp, plot_all, n_epochs) # Calls the constructor of the super class

    def read_data(self):
        data_as_strings = list(csv.reader(open('ring-data.csv'), delimiter=','))
        if(self.IS_REMAPPED):
            self.TRAINING_DATA = [[remapper.remap(float(f1), float(f2))[0],remapper.remap(float(f1), float(f2))[1], int(c)] for [f1, f2, c] in data_as_strings]
        else:
            self.TRAINING_DATA = [[float(f1), float(f2), int(c)] for [f1, f2, c] in data_as_strings]

    def plot(self):
        plt.legend(loc='best')
        plt.show()



if __name__=='__main__':
    binary_perceptron = BinaryPerceptron(alpha=0.5)
    pbp = PlotRingBP(binary_perceptron)
    pbp.train()
    pbp.plot()
    
