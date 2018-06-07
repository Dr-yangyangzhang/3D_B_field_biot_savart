from mayavi import mlab


def draw_coil(rc, color):
    pic = mlab.plot3d(rc[:, 0], rc[:, 1], rc[:, 2], tube_radius=0.01, color=color)
    return pic
