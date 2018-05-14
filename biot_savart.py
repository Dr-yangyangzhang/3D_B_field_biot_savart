import numpy as np

mu0 = 4 * np.pi / 10 ** 7


def biot_savart(rs, rc, ic, dl):
    ns = len(rs[:, 0])
    nl = len(dl[:, 0])
    B = np.zeros((ns, 3))

    for i in range(0, ns - 1):
        dB = [0, 0, 0]
        for j in range(0, nl - 1):
            rp = rs[i, :] - rc[j, :]
            db = (ic * mu0 / (4 * np.pi)) * (np.cross(dl[j, :], rp)) / np.linalg.norm(rp) ** 3
            dB = dB + db

        B[i, :] = dB

    bx = B[:, 0]
    by = B[:, 1]
    bz = B[:, 2]

    lb = round(ns ** (1 / 3))

    Bx = np.reshape(bx, (lb, lb, lb))
    By = np.reshape(by, (lb, lb, lb))
    Bz = np.reshape(bz, (lb, lb, lb))

    return Bx, By, Bz
