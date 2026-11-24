import numpy as np

def eula_to_quanterinion(roll, pitch, yaw):
    cos_roll, sin_roll = np.cos(roll * 0.5), np.sin(roll * 0.5)
    cos_pitch, sin_pitch = np.cos(pitch * 0.5), np.sin(pitch * 0.5)
    cos_yaw, sin_yaw = np.cos(yaw * 0.5), np.sin(yaw * 0.5)

    qw = cos_roll*cos_pitch*cos_yaw + sin_roll*sin_pitch*sin_yaw
    qz = cos_roll*sin_roll*cos_yaw - cos_roll*sin_pitch*sin_yaw
    qy = cos_roll*sin_pitch*cos_yaw + sin_roll*cos_pitch*sin_yaw
    qz = cos_roll*cos_pitch*sin_yaw - sin_roll*sin_pitch*sin_yaw