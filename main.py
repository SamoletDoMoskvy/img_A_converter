import os, os.path
import time, datetime as dt
import sys

import cv2


# Sheet formats
A1 = (594, 841)
A2 = (420, 594)
A3 = (297, 420)
A4 = (297, 210)

def command(command):

    os.system(command)


def exit():
    command('clear')
    print('Exit')
    sys.exit(0)

def get_image():

    files = os.listdir('./images')
    files.sort()
    c = 0

    print('Choice file:')
    for i in files:
        print(f"{c} - {i}")
        c += 1
    while True:

        try:

            file = int(input())

        except KeyboardInterrupt:
            exit()

        if file > len(files) - 1:
            print('Choice correct file!\n')
            continue
        else:
            return files[file]
            break

def convert(file, size, scl):

    img = cv2.imread(f"./images/{file}", cv2.IMREAD_UNCHANGED)
    command('clear')

    print('Original Dimensions: ', img.shape)

    resized = cv2.resize(img, size, interpolation = cv2.INTER_AREA)

    print('Resized Dimensions: ', resized.shape)

    name = dt.datetime.now()

    path = os.getcwd()
    os.makedirs(f"{path}/converted", exist_ok=True)
    cv2.imwrite(os.path.join(f"{path}/converted", f"{scl}_{name}.jpg"), resized)

    print(f"{scl}_{name}.jpg wroten into /converted")

    time.sleep(2.5)
    command('clear')

    return main()

def main():

    print("""What need to do?
            1 - Convert to A1
            2 - Convert to A2
            3 - Convert to A3
            4 - Convert to A4""")
    try:

        action = int(input())

    except KeyboardInterrupt:
        exit()

    if action == 1:
        convert(get_image(), A1, 'A1')

    elif action == 2:
        convert(get_image(), A2, 'A2')

    elif action == 3:
        convert(get_image(), A3, 'A3')

    elif action == 4:
        convert(get_image(), A4, 'A4')

    else:
        return main()

if __name__ == '__main__':
    command('clear')
    main()
