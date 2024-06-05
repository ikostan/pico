# MicroPython Simulation in Wokwi for VS Code

Wokwi is an online Electronics simulator. You can
use it to simulate Arduino, ESP32, STM32, and many
other popular boards, parts and sensors.

## Prerequisites

1. Install the Wokwi for VS Code extension.
2. Install the mpremote tool, e.g. pip install mpremote.

## Usage

1. Clone this project and open it in VS Code.
2. From the command palette, select "Wokwi: Start Simulator".
   You may need to activate your license first.
3. Select one of the directories to simulate, e.g. "esp32".
4. While the simulator is running, open a command prompt, and type:

```bash
python -m mpremote connect port:rfc2217://localhost:4000 run main.py
```

This will connect to the simulator and run the main.py file on the board. 

**Note:** keep the simulator tab visible while running the command,
otherwise the simulator will pause and the command will timeout.

For more detailed information see [source here](https://github.com/wokwi/wokwi-vscode-micropython/tree/main).
