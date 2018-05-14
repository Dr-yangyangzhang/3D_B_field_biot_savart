import numpy as np


def circle_coil(c0, nr, Rc, nc):
    theta = np.linspace(0, 2 * np.pi, nc)
    rc = np.zeros((nc, 3))
    dl = np.zeros((nc, 3))

    if nr[0] == 1:
        xc = np.zeros((nc, 1)) + c0[0]
        yc = Rc * np.cos(theta) + c0[1]
        zc = Rc * np.sin(theta) + c0[2]

        rc[0:nc - 2, 1] = [(a + b) / 2 for a, b in zip(yc[0:-1], yc[1::1])]
        rc[0:nc - 2, 2] = [(a + b) / 2 for a, b in zip(zc[0:-1], zc[1::1])]
        rc[-1, 1] = np.mean([yc[0], yc[nc - 1]])
        rc[-1, 2] = np.mean([zc[0], zc[nc - 1]])
        rc[:, 1] = np.reshape(xc, nc, 1)

        dl[0:nc - 1, 1] = np.diff(yc)
        dl[0:nc - 1, 2] = np.diff(zc)
        dl[-1, 1] = yc[0] - yc[-1]
        dl[-1, 2] = zc[0] - zc[-1]
    elif nr[1] == 1:
        xc = Rc * np.cos(theta) + c0[0]
        yc = np.zeros((nc, 1)) + c0[1]
        zc = Rc * np.sin(theta) + c0[2]

        rc[0:nc - 1, 0] = [(a + b) / 2 for a, b in zip(xc[0:-1], xc[1::1])]
        rc[0:nc - 1, 2] = [(a + b) / 2 for a, b in zip(zc[0:-1], zc[1::1])]
        rc[-1, 0] = np.mean([xc[0], xc[-1]])
        rc[-1, 2] = np.mean([zc[0], zc[-1]])
        rc[:, 1] = np.reshape(yc, nc, 1)

        dl[0:nc - 1, 0] = np.diff(xc)
        dl[0:nc - 1, 2] = np.diff(zc)
        dl[nc - 1, 0] = xc[0] - xc[-1]
        dl[nc - 1, 2] = zc[0] - zc[-1]
    elif nr[2] == 1:
        xc = Rc * np.cos(theta) + c0[0]
        yc = Rc * np.sin(theta) + c0[1]
        zc = np.zeros((nc, 1)) + c0[2]
        rc[0:nc - 1, 0] = [(a + b) / 2 for a, b in zip(xc[0:-1], xc[1::1])]
        rc[0:nc - 1, 1] = [(a + b) / 2 for a, b in zip(yc[0:-1], yc[1::1])]
        rc[-1, 0] = np.mean([xc[0], xc[-1]])
        rc[-1, 1] = np.mean([yc[0], yc[-1]])
        rc[:, 2] = np.reshape(zc, nc, 1)

        dl[0:nc - 1, 0] = np.diff(xc)
        dl[0:nc - 1, 1] = np.diff(yc)
        dl[-1, 0] = xc[0] - xc[-1]
        dl[-1, 1] = yc[0] - yc[-1]

    return rc, dl


def straight_line(end_points, nr, nc):
    rc = np.zeros((nc, 3))
    dl = np.zeros((nc, 3))

    index = nr.index(1)

    seg = np.linspace(end_points[0][index], end_points[1][index], nc)

    rc[0:nc - 1, index] = [(a + b) / 2 for a, b in zip(seg[0:-1], seg[1::1])]
    dl[0:nc - 1, index] = np.diff(seg)
    rc[-1, index] = (seg[0] + seg[-1]) / 2
    dl[-1, index] = seg[0] - seg[-1]

    return rc, dl
