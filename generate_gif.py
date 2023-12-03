import os
from os.path import join
import imageio.v2 as imageio


def generate_gif(name, folder_path):
    fig_files = []
    folder = folder_path
    files = os.listdir(folder)
    files.sort(key=lambda x: int(x[5:-4]))
    for file_name in files:
        if file_name.endswith('.png'):
            fig_files.append(join(folder, file_name))
    print("========== add figure files ==========")
    save_name = join('%s.gif' % name)
    with imageio.get_writer(save_name, mode='I', duration=0.1, fps=35) as writer:
        for fig in fig_files:
            image = imageio.imread(fig)
            writer.append_data(image)


name = "gif/multi_9"
folder_path = "result"


print("========== start generate dynamic gif ==========")
generate_gif(name, folder_path)
print("========== dynamic gif has been saved ==========")