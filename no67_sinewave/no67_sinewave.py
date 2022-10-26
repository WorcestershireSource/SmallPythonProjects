import math, shutil, time

WIDTH, HEIGHT = shutil.get_terminal_size()

print('What message do you want to display?')
message = input('> ')
multiplier = (WIDTH - 1 - len(message)) / 2

step = 0.0

while True:
    padding = round((math.sin(step) + 1) * multiplier)
    padding_txt = ' ' * padding
    print(padding_txt + message)
    step += 0.25
    time.sleep(0.05)
    current_w, current_h = shutil.get_terminal_size()
    if WIDTH + 1 != current_w:
        multiplier = (current_w - 1 - len(message)) / 2



