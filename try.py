import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import pandas as pd
import math as m
import shutil
import os
def draw_0(ax):
    global yao
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (0, 0)),
        (Path.LINETO, (yao, 0)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path)
    ax.add_patch(patch)
    return [yao, 0]


def draw_1(position, theta1, ax):
    global datui
    y = position[1] - datui * m.sin(theta1)
    x = position[0] - datui * m.cos(theta1)
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, position),
        (Path.LINETO, (x, y)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path)
    ax.add_patch(patch)
    return [x, y]


def draw_2(position, theta2, ax):
    global xiaotui
    y = position[1] - xiaotui * m.sin(theta2)
    x = position[0] + xiaotui * m.cos(theta2)
    Path = mpath.Path
    path_data = [
        (Path.MOVETO, position),
        (Path.LINETO, (x, y)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    patch = mpatches.PathPatch(path)
    ax.add_patch(patch)
    return [x, y]


# df1 = pd.read_excel('case1.xlsx')
# data1 = df1.iloc[:, [0]].values
# df2 = pd.read_excel('case2.xlsx')
# data2 = df2.iloc[:, [0]].values
df1 = pd.read_excel('dynamic_data.xlsx')
data1 = df1.iloc[:, [1]].values
df2 = pd.read_excel('dynamic_data.xlsx')
data2 = df2.iloc[:, [2]].values
# L1 = 52
# L2 = 93
# k1 = 93 / 0.2284
# k2 = 52 - k1
# l2 = 0.354
# l3 = 0.4738
# l4 = 0.9491
# a2 = 0.2284
# a3 = 1.2804
# a4 = 0.5727
yao = 100
datui = 52
xiaotui = 93

# Path = mpath.Path
# path_data = [
#     (Path.MOVETO, (0, 0)),
#     (Path.LINETO, (1, 1)),
# ]
# codes, verts = zip(*path_data)
# path = mpath.Path(verts, codes)
# patch = mpatches.PathPatch(path)
# ax.add_patch(patch)

shutil.rmtree("result")
os.mkdir("result")
current_frame = 1
b = np.zeros([18, 2])
while current_frame <= 18:
    fig, ax = plt.subplots()
    ax.set_xlim(-130, 130)
    ax.set_ylim(-130, 10)
    ax.set_axis_off()
    draw_0(ax)
    a = draw_1([yao, 0], float(data1[current_frame])/180*m.pi, ax)
    b[current_frame - 1] = draw_2(a, float(data2[current_frame])/180*m.pi - float(data1[current_frame])/180*m.pi, ax)
    plt.savefig("result" + "/frame" + str(current_frame) + ".png", dpi=200)
    plt.close()
    current_frame += 1


x = b[:, 0]
y = b[:, 1]

plt.plot(x, y)
plt.ylim(-130, 10)
plt.xlim(-50, 180)
plt.savefig("traj/traj1")