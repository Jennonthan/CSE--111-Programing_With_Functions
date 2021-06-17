'''
Brennon Laney
CSE 111
05/07/21
Purpose:
During this lesson, you will write code that draws the sky,
the ground, and clouds. During the next lesson, you will write
code that completes the scene. The scene that your program draws 
may be very different from the example scene above. However, 
your scene must be outdoor, the sky must have clouds, and the 
scene must include repetitive elements such as blades of grass, 
trees, leaves on a tree, birds, flowers, insects, fish, pickets 
in a fence, dashed lines on a road, buildings, bales of hay, 
snowmen, snowflakes, or icicles. Be creative.
'''

import tkinter as tk
from tkinter import Canvas
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object. Makes it so that 
    #TK runs in image instead of just terminal
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    # Sets the title of the window of the image
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_sky(canvas, scene_top, 250, scene_left, scene_right)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    draw_ground(canvas, 250, scene_bottom, scene_left, scene_right)
    draw_cloud(canvas, 100, 100, 400, 200)
    draw_cloud(canvas, 50, 50, 300, 200)
    draw_sun(canvas)
    for _ in range(0, 100):
        draw_snow(canvas)



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    '''
    This Code is meant to draw a grid for the picture so that I can 
    see where I need to place everything.
    '''
    for i in range (left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
    
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)

def draw_sky(canvas, top, bottom, left, right):
    '''
    This draws the sky
    '''
    canvas.create_rectangle(left, top, right, bottom, outline="gray20", width=1, fill="blue")

def draw_ground(canvas, top, bottom, left, right):
    '''
    This draws the ground
    '''
    canvas.create_rectangle(left, top, right, bottom, outline="gray20", width=1, fill="green")

def draw_cloud(canvas, left, top, right, bottom):
    '''
    This draws a cloud
    '''
    canvas.create_oval(left, top, right, bottom, outline="gray85", width=1, fill="gray85")

# def draw_sun(canvas):
#     canvas.create_oval(50, 50, 100, 100, oultine="salmon1", width=1, fill="salmon1")

def draw_sun(canvas):
    '''
    This draws a sun
    '''
    canvas.create_oval(600, 1, 700, 101, outline="salmon1", width=1, fill="salmon1")

def draw_snow(canvas):
    '''
    draw a snow
    '''
    left = random.randint(0, 800)
    top = random.randint(0, 800)
    right = left + 5
    bottom = top + 5
    canvas.create_oval(left, top, right, bottom, outline="snow", width=1, fill='snow')






def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom, \
            trunk_right, trunk_bottom, \
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y, skirt_right, skirt_bottom, skirt_left, skirt_bottom, outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()
