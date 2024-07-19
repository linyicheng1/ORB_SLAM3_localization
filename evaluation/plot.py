import numpy as np
import matplotlib.pyplot as plt

# 读取数据文件
file_path = '/home/vio/Code/VIO/visual_localization/ORB_SLAM3_localization/Examples/Stereo/g_long-term.txt'

timestamps = []
positions = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.split()
        timestamps.append(float(parts[0]))
        positions.append([float(parts[1]), float(parts[2]), float(parts[3])])

positions = np.array(positions)

# 绘制XY轨迹
plt.figure()
plt.plot(positions[:, 0], positions[:, 1], label='Trajectory')
plt.scatter(positions[:, 0], positions[:, 1], c='r')  # 轨迹点

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.title('XY Plane Trajectory')
plt.show()

plt.savefig('ggggg_long-term.png')
