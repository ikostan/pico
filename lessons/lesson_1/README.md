# [Raspberry Pi Pico W LESSON 1: Write Your First Program for Absolute Beginners](https://www.youtube.com/watch?v=SL4_oU9t8Ss&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=1)

## Description

In this introductory video, I will show you how to install micropython on the Raspberry
Pi Pico W, I will show you how to install Thonny, the IDE, on your PC. Thonny will 
allow you to interact with the Pico W. Then in today's short introductory video,
you will write your first four programs, and will get a homework assignment. This
class is for absolute beginners, and I do not assume you already understand the
material I am presenting. My goal is not to 'Show Off', but to genuinely teach you
how you can do this type of work and projects on your own.

### MicroPython Simulation in Wokwi for VS Code

#### Prerequisites

1. Install the Wokwi for VS Code extension.
2. Install the mpremote tool, e.g. pip install mpremote.

#### Usage

1. Clone this project and open it in VS Code.
2. From the command palette, select "Wokwi: Start Simulator".
   You may need to activate your license first.
3. Select one of the directories to simulate, e.g. "esp32".
4. While the simulator is running, open a command prompt, and type:

```python
python -m mpremote connect port:rfc2217://localhost:4000 run main.py
```

This will connect to the simulator and run the main.py file on the board. 

**Note:** keep the simulator tab visible while running the command,
otherwise the simulator will pause and the command will timeout.

For more detailed informations see [source here](https://github.com/wokwi/wokwi-vscode-micropython/tree/main).

### Source material

[Raspberry Pi Pico W Lessons for Absolute Beginners](https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5)
by [Paul McWhorter](https://www.youtube.com/c/mcwhorpj/playlists)
