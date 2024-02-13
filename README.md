# chaos-balls

A Simulation of balls bouncing around in a circular ring, inspired by a [Numberphile video](https://youtu.be/6z4qRhpBIyA) on chaotic systems. The simulation demonstates how chaos and complexity arises from something as simple as balls bouncing in a ring. Written in python3 and pygame.

## Requirements

- [python 3.9](https://www.python.org/downloads/release/python-397/)

Install these packages using pip:

- pygame. preferably version 2.0.1

```
pip install pygame -V 2.0.1
```

## Run

Simply run the chaos_balls.py file either by double clicking it or running the following command in the terminal
~~~
py chaos_balls.py
~~~

## Features

To Add/Remove balls and manipulate their properties, i.e velocity, position, etc you can do so by opening chaos_balls.py in a text editor and follow the instructions around line 150. Will make this more user friendly in the future but for now just mess around with the source code.

### Example

First we will create the object:

```redball_test = Balls()```
Now the arguments that go in the class Balls are seen in the template below:

```template = Balls("name", color, radius, thickness, x-coordinate, y-coordinate, [collision sound file] optional)```

- name: name of the ball, call it whatever you like -> str
- color: color of the ball. color is a tuple of the format (r,g,b)
- radius: radius of the ball -> float or int
- thickness: set to 0 if you want a solid ball. If set to a non-zero value, then ball will be drawn as a ring and the thickness controls how thick the outline is. -> float or int
- x & y coordinates: The position of the center of the ball. Note the top left corner of the window is the origin (0,0) and y increases (positive) going down
- collision sound file: the audio file that's played during collisions with the walls of the ring. Feel free to use your own audio files, make sure to sure to convert them to .wav and add them to the audio folder.

To add a red ball at the position 200, 300.

```redball_test = Balls("test", (255, 0, 0), 8, 0, 200, 300)```

Note: color is red which is ```(255,0,0)``` in rgb. x coordinate is set to ```width//2``` which is midway and
y coordinate is set to ```height//2 +10``` which is midway and 10 pixels down.

## Controls

- Spacebar to pause

That's about it!
