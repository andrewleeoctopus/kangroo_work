import numpy as np
import matplotlib.pyplot as plt

# -----------define HJ agolrathiem para
delta = 0.5  # step size
alfa = 1  # speed rate
beta = 0.5  # decrease rate
epsilon = 0.002  # min stepsize
iniPO = np.array([6, 1])  # initial point
G = 10  # 探测次数


# -----------define function
# min f(x):=(1−x1​)^2+5(x2​−x1^​2)^2
def fun(A):
    ff = (1 - A[0]) ** 2 + 5 * (A[1] - A[0] ** 2) ** 2
    return ff


iniPO_ff = np.array([fun(iniPO)])
X = iniPO
X_ff = iniPO_ff
Y = X
Y_ff = X_ff
x = iniPO
y = iniPO

# -----------explore step
dim = iniPO.shape[0]  # dimension
e = [1] * dim
E = np.diag(e)
k = 0
while delta > epsilon:
    for i in range(0, dim):
        y_new_plus = y + delta * E[i, :]
        ff = fun(y)
        ff_new = np.array([fun(y_new_plus)])
        temp = Y
        temp_ff = Y_ff
        Y = np.vstack((temp, y_new_plus))
        Y_ff = np.vstack((temp_ff, ff_new))
        plt.plot([Y_ff.shape[0] - 1, Y_ff.shape[0]], Y_ff[-2:, :], c='b', marker='*')
        # plt.show()
        if ff_new < ff:
            y = y_new_plus
        else:
            y_new_minus = y - delta * E[i, :]
            ff = fun(y)
            ff_new = np.array([fun(y_new_minus)])
            temp = Y
            temp_ff = Y_ff
            Y = np.vstack((temp, y_new_minus))
            Y_ff = np.vstack((temp_ff, ff_new))
            plt.plot([Y_ff.shape[0] - 1, Y_ff.shape[0]], Y_ff[-2:, :], c='b', marker='*')
            # plt.show()
            if ff_new < ff:
                y = y_new_minus
                # get all points
    Y_Data = np.hstack((Y, Y_ff))
    # get new base point
    x = y
    # get all base points
    temp_x = X
    X = np.vstack((temp_x, x))
    temp_x_ff = X_ff
    X_ff = np.vstack((temp_x_ff, fun(x)))
    X_Data = np.hstack((X, X_ff))

    # -----------Move step

    if ff_new < ff:
        print()
        y = X[-1, :] + alfa * (X[-1, :] - X[-2, :])
        ff = fun(y)
        temp = Y
        Y = np.vstack((temp, y))
        temp_ff = Y_ff
        Y_ff = np.vstack((Y_ff, ff))
        plt.plot([Y_ff.shape[0] - 1, Y_ff.shape[0]], Y_ff[-2:, :], c='b', marker='*')
        Y_Data = np.hstack((Y, Y_ff))
    else:
        # temp = Y
        # Y = np.vstack((temp,y))
        # temp_ff = Y_ff
        # Y_ff = np.vstack((Y_ff,ff))
        # plt.plot([Y_ff.shape[0]-1,Y_ff.shape[0]], Y_ff[-2:,:], c='b', marker='*')
        # Y_Data = np.hstack((Y,Y_ff))
        delta = beta * delta
    print('k', k)
    print('')
    # -----------wheather stop
    if k >= G:  # 当k大于等于G跳出循环
        break
    k = k + 1

print('--------')
print('Y_Data', Y_Data)
print('X_Data', X_Data)
print('delta', delta)
print('--------')

