import cv2
import numpy as np
import matplotlib.pyplot as plt

char_0 = cv2.imread('chars/char_0.png', 0)
char_1 = cv2.imread('chars/char_1.png', 0)
char_2 = cv2.imread('chars/char_2.png', 0)
char_3 = cv2.imread('chars/char_3.png', 0)
char_4 = cv2.imread('chars/char_4.png', 0)
char_5 = cv2.imread('chars/char_5.png', 0)
char_6 = cv2.imread('chars/char_6.png', 0)
char_7 = cv2.imread('chars/char_7.png', 0)
char_8 = cv2.imread('chars/char_8.png', 0)
char_9 = cv2.imread('chars/char_9.png', 0)
print('examples read...')

speed_curve = []

samples_per_sec = 1

for i in range(0, 15723):
    if i%(30/samples_per_sec) == 0:
        number_str = str(i).zfill(5)
        path = 'images/falcon_heavy_' + number_str + '.jpg'
        img = cv2.imread(path, 0)

        char_a = img[193:220, 91:110]
        char_b = img[193:220, 111:130]
        char_c = img[193:220, 131:150]
        char_d = img[193:220, 151:170]
        char_e = img[193:220, 171:190]

        characters = [char_a, char_b, char_c, char_d, char_e]
        speed_str = ''

        for char in characters:
            error_0 = cv2.sumElems(cv2.subtract(char, char_0))[0]
            error_1 = cv2.sumElems(cv2.subtract(char, char_1))[0]
            error_2 = cv2.sumElems(cv2.subtract(char, char_2))[0]
            error_3 = cv2.sumElems(cv2.subtract(char, char_3))[0]
            error_4 = cv2.sumElems(cv2.subtract(char, char_4))[0]
            error_5 = cv2.sumElems(cv2.subtract(char, char_5))[0]
            error_6 = cv2.sumElems(cv2.subtract(char, char_6))[0]
            error_7 = cv2.sumElems(cv2.subtract(char, char_7))[0]
            error_8 = cv2.sumElems(cv2.subtract(char, char_8))[0]
            error_9 = cv2.sumElems(cv2.subtract(char, char_9))[0]
            errors = np.array([error_0, error_1, error_2, error_3, error_4, error_5, error_6, error_7, error_8, error_9])
            speed_str += np.array2string(np.argmin(errors))

        speed = int(speed_str)
        speed_curve.append(speed)

print(speed_curve)

accleration_curve = []

for i in range(len(speed_curve)-1):
    acc = -speed_curve[i]*(1000/60/60)+speed_curve[i+1]*(1000/60/60)
    accleration_curve.append(((acc/2)*samples_per_sec)/9.81)

plt.figure(1)
plt.subplot(211)
plt.plot(speed_curve)
plt.ylabel("speed in km/h")
plt.grid(True)
plt.subplot(212)
plt.plot(accleration_curve)
plt.ylabel("acceleration in G")
plt.grid(True)
plt.show()