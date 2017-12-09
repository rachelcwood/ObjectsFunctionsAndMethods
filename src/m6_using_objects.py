"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rachel Wood.
"""  # DONE 1.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE 2
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    # remeber to render
    window = rg.RoseWindow(600, 600)

    circone = rg.Circle(rg.Point(300, 300), 80)
    circone.fill_color = 'red'
    circone.attach_to(window)
    window.render()

    circtwo = rg.Circle(rg.Point(300, 300), 120)
    circtwo.attach_to(window)
    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE 3
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

    window = rg.RoseWindow(600, 600)

    circ = rg.Circle(rg.Point(450, 300), 80)
    circ.fill_color = 'blue'
    circ.attach_to(window)
    window.render()

    # Printing Values
    # thickness
    print(circ.outline_thickness)
    # fill
    print(circ.fill_color)
    # center
    print(circ.center)
    # x- coor
    print(circ.center.x)
    # y- coor
    print(circ.center.y)

    pointone = rg.Point(500, 400)
    pointtwo = rg.Point(200, 200)

    rect = rg.Rectangle(pointone, pointtwo)
    rect.attach_to(window)
    window.render()

    # Printing Values
    # thickness
    print(rect.outline_thickness)
    # fill
    print(rect.fill_color)
    # center
    # xcor = rg.Rectangle.corner_1.x-rg.Rectangle.corner_2.x
    # ycor = rg.Rectangle.corner_1.y - rg.Rectangle.corner_2.y
    # get_center() is easier than calculating
    center = rect.get_center()
    print(center)
    # x- coor
    print(center.x)
    # y- coor
    print(center.y)

    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE 4
    # ------------------------------------------------------------------
    window = rg.RoseWindow(600, 600)

    lineone = rg.Line(rg.Point(150, 450), rg.Point(300, 300))
    lineone.attach_to(window)
    window.render()

    linetwo = rg.Line(rg.Point(500, 200), rg.Point(200, 500))
    linetwo.thickness = 5
    linetwo.attach_to(window)
    window.render()

    midpt = linetwo.get_midpoint()

    print()
    print('Lines test')
    print(midpt)
    print(midpt.x)
    print(midpt.y)

    window.close_on_mouse_click()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
