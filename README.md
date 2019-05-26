# Python utility to generate quadratic recursive zooming in gifs
Can zoom in linearly, quadratically and square like the following:
![](zoom.png)
![](linear.gif)
![](quad.gif)
![](sqrt.gif)

# Limitations
Currently only optimized for square images, but can be changed easily

# How to
* Create a base image like zoom.png, 
* Find out the topleft x-y coordinates (INNER_X_LEFT, INNER_Y_TOP)
* As well as the size of the cursive sub-image (INNER_SIZE)
* Set gif params like steps, duration and resolution

# Requirements
pillow/PIL, numpy
