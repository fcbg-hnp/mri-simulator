# MRI-Simulator
Simulate the triggers sent by the MRI (key pressed) for python 3.

## Installation
Run ```pip install -e .``` to install the library in development mode.

## Usage
1. Modify the ```config.ini``` with you desired parameters:
  * key_type      =   the key value to send
  * repetition    =   the number of times the key will be sent
  * period        =   the period in between two keys pressed                     [msec]
  * waitingTime  =   the pre-waiting time before starting sending keys pressed  [msecs]
2. Launch the main from a terminal ```python main.py``` 
