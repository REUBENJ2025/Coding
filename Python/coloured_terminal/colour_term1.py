import time, sys, colorsys

text = "Testing coloured text"
t = 0

while True:
    out = ""
    for i, ch in enumerate(text):
        hue = (t + i/len(text)) % 1
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        R, G, B = int(r*255), int(g*255), int(b*255)
        out += f"\033[38;2;{R};{G};{B}m{ch}\033[0m"
    sys.stdout.write(out + "\r")
    sys.stdout.flush()
    t += 0.01
    time.sleep(0.02)
