import numpy as np
from scipy.linalg import expm
import scipy as sp

def stm_ti(A, t_f, t_0):
    return expm(A * (t_f - t_0)) # time invariant state transition matrix

def vstm_ti(A, t_f, t_0, steps=1000):
    t_span = np.linspace(t_0, t_f, num=steps)
    return [ stm_ti(A, t, t_0) for t in t_span]

def test_stm_ti():
    import matplotlib.pyplot as plt
    A = np.array([
        [1, 1],
        [-1, 1]
    ])

    x_0 = np.array([0, 1]);
    n = 1000

    out = vstm_ti(A, 1, 0, n)
    plt.plot(np.linspace(0, 1, n), [np.dot(o[0], x_0) for o in out])
    plt.plot(np.linspace(0, 1, n), [np.dot(o[1], x_0) for o in out])
    plt.show()
    return out

def vstm_tv(A, t_f, t_0, n=1000):
    # A is callable which returns an array
    l = len(A(t_0))
    t_span = np.linspace(t_0, t_f, num=n)
    delta_t = (t_f - t_0)/n
    phi = [expm(A(t) * delta_t) for t in t_span]
    stm = [np.identity(l)]
    for p in phi:
        stm.append(np.dot(p, stm[-1]))

    return stm

def test_vstm_tv():
    import matplotlib.pyplot as plt
    A = lambda t: np.array([
        [0, 1],
        [-t, 0]
    ])

    x_0 = np.array([0.5, 0])
    t_0 = 0
    t_f = 3 * np.pi

    n = 600
    return vstm_tv(A, t_f, t_0, n)[1:]
