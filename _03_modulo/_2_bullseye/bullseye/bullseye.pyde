def setup():
    # Set the size of your sketch
    size(500,500)
    
    pass

def draw():
    circlesize = 400
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(8):
        if i % 2 == 0:
            fill(255,0,0)
        else:
            pass
        ellipse(250,250,circlesize,circlesize)
        circlesize = circlesize - 50
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
