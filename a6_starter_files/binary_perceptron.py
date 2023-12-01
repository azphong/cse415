"""binary_perceptron.py
One of the starter files for use in CSE 415, Autumn 2023
Assignment 6.
Complete this python file.

This program can be run from the given Python program
called run_2_class_2_feature_iris_data.py.
"""


def student_name():
    return "Aaron Hong"  # Replace with your own name here


class BinaryPerceptron:
    """
    Class representing the Binary Perceptron
    ---
    It is an algorithm that can learn a binary classifier
    """
    
    def __init__(self, weights=None, alpha=0.5):
        """
        Initialize the Binary Perceptron
        ---
        weights: Weight vector of the form [w_0, w_1, ..., w_{n-1}, bias_weight]
        alpha: Learning rate
        """
        if weights is None:
            self.weights = [0, 0, 0]
        else:
            self.weights = weights[:]
        self.alpha = alpha
    
    def classify(self, x_vector):
        """
        Method that classifies a given data point into one of 2 classes
        ---
        Inputs:
        x_vector = [x_0, x_1, ..., x_{n-1}]
        Note: y (correct class) is not part of the x_vector.

        Returns:
        y_hat: Predicted class
              +1 if the current weights classify x_vector as positive i.e. the required dot product must be >=0,
        else  -1 if it is classified as negative.
        """
        # ADD YOUR CODE HERE
        sum = 0
        for i in range(len(x_vector)):
            sum += self.weights[i]*x_vector[i]
        if sum>=0:
            return 1
        else:
            return -1
        #raise NotImplementedError
    
    def train_with_one_example(self, x_vector, y):
        """
        Method that updates the model weights using a particular training example (x_vector,y)
        and returns whether the model weights were actually changed or not
        ---
        Inputs:
        x_vector: Feature vector, same as method classify
        y: Actual class of x_vector
            +1 if x_vector represents a positive example,
        and -1 if it represents a negative example.
        Returns:
        weight_changed: True if there was a change in the weights
                        else False
        """
        # ADD YOUR CODE HERE
        xk = self.classify(x_vector)
        print(x_vector,xk,y)
        if(xk!=y):
            new_w = [0.0 for i in range(len(self.weights))]
            for i in range(len(x_vector)):
                if(xk == -1 and y == 1):
                    new_w[i] = self.weights[i]+self.alpha*x_vector[i]
                else:
                    new_w[i] = self.weights[i]-self.alpha*x_vector[i]
            new_w[-1] = self.weights[-1]+y*self.alpha
            self.weights = new_w
            return True
        else:
            return False
        raise NotImplementedError
    
    def train_for_an_epoch(self, training_data):
        """
        Method that goes through the given training examples once, in the order supplied,
        passing each one to train_with_one_example.
        ---
        Input:
        training_data: Input training data
        [[x_vector_1, y_1], [x_vector_2, y_2], ...]
        where each x_vector is concatenated with the corresponding y value.

        Returns:
        changed_count: Return the number of weight updates.
        (If zero, then training has converged.)
        """
        # ADD YOUR CODE HERE
        changed_count = 0
        for data in training_data:
            if(self.train_with_one_example(data[:-1],data[-1])):
                changed_count += 1
            #print(self.weights)
        return changed_count
        raise NotImplementedError


def sample_test():
    """
    May be useful while developing code
    Trains the binary perceptron using a synthetic training set
    Prints the weights obtained after training
    """
    DATA = [
        [-2, 7, +1],
        [1, 10, +1],
        [3, 2, -1],
        [5, -2, -1]]
    bp = BinaryPerceptron()
    print("Training Binary Perceptron for 3 epochs.")
    for i in range(3):
        bp.train_for_an_epoch(DATA)
    print("Binary Perceptron weights:")
    print(bp.weights)
    print("Done.")


if __name__ == '__main__':
    sample_test()
