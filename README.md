# MRI-Simulator

Simulate the triggers sent by the MRI (key pressed) in python 3.

## Installation

This repository can be installed with `pip install git+https://github.com/fcbg-hnp-meeg/mri-simulator`.

## Usage

```
from mrisim.config import read_config
from mrisim import simulate

# use read_config to load a custom .ini configuration
fname = "my_config.ini"
key, repetition, period, wait = read_config(fname)

# use simulate to run the key-press simulation
simulate(key, repetition, period, wait)
```

An entry-point `mrisim` is available. Use `mrisim --help` in a terminal for
information about the arguments.
