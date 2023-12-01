import discord_ansi

ansiArt = discord_ansi.ANSIArt(5, 5)
ansiArt.fillAll("blue") # fill entire image
# From (1, 1) to (4, 4) if counting from 1
# But it starts counting from 0, so it's (0, 0) to (3, 3)
ansiArt.fillSquare(0, 0, 3, 3, "orange")
# Set individual pixels
# (2, 2) if counting from 1
# But it starts counting from 0, so it's (1, 1)
ansiArt.setPixel(1, 1, "blue")
output = ansiArt.render()
print(output)
from pyperclip import copy
copy(output)
