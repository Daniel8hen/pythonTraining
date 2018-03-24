from numpy import *


def compute_error_for_given_points(b, m, points):
    """A method to compute an error based on given points b, m, data(x, y pairs) """
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m*x + b)) **2
    reutrn (totalError / float(len(points)))


def step_gradient(current_b, current_m, points, learning_rate):
    """ The gradient descent itself, works by the partial deriviative with respect to b, m """
    #gradient_descent
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((current_m*x) + current_b))
        m_gradient += -(2/N) * x * (y - ((current_m*x) + current_b))
    new_b = current_b - (learning_rate * b_gradient)
    new_m = current_m - (learning_rate * m_gradient)

    return [new_b, new_m]


def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    """ An outer method for looping the gradient descent - 1000 times """
    b = starting_b
    m = starting_m

    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]


def run():
    """ The main """
    points = genfromtxt('data.csv', delimiter=',')
    #hyperparameters
    learning_rate = 0.0001 #can be changed, how fast our model works (balance)
    # y = mx + b (m - slope, b - y intercept)
    initial_b = 0
    initial_m = 0
    num_iterations = 1000 #could be bigger in case data is huge
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print(b)
    print(m)

if __name__ == '__main__':
    run()
