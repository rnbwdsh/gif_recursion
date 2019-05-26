from PIL import Image
from numpy import average, array, exp, sqrt

# modify these params
OUTER_SIZE = 3600
INNER_SIZE = 360
INNER_X_LEFT = 2665
INNER_Y_TOP = 1290
STEPS = 50
GIF_RES = 1000
DURATION = 20
MODE = "linear" # or quad or sqrt

# init helper data structures
cropstart = array([0, 0, OUTER_SIZE, OUTER_SIZE])
cropend = array([INNER_X_LEFT, INNER_Y_TOP, INNER_X_LEFT+INNER_SIZE, INNER_Y_TOP+INNER_SIZE])
image = Image.open("zoom.png")
frames = []

for i in range(STEPS+1):
    mode = {"linear": [STEPS-i, i], "quad": [(STEPS-i)**2, i**2], "sqrt":[sqrt(STEPS-i), sqrt(i)]}
    # calculate new crop
    new_dim = average([cropstart] + [cropend], weights=mode[MODE], axis = 0)
    # append cropped, rescaled frame to gif
    frames.append(image.crop(new_dim).resize((GIF_RES, GIF_RES)))
# save output
frames[0].save(MODE+'.gif', format='GIF', append_images=frames[1:], save_all=True, duration=DURATION, loop=0)