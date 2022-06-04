# As far as I am concerned, it does what it says on the tin ¯\_(ツ)_/¯

import random
import shutil
import sys
import time

MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.05
STREAM_CHARS = ['0', '1']
DENSITY = 0.10
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print("MATRIX BINARY STREAM, FOR THE MASSES =>> THE CAKE IS A LIE")
print("Ctrl-C will transport you back into the real world, if you're into that sort of thing...")
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
