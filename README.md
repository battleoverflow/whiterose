# Whiterose
Whiterose is a pure Python library built to return the current time in real-time within a single stdout. This Python library does not require any external libraries.

## Installation
You can install this library via Pypi:
```bash
$ pip3 install whiterose
```

## Usage
A script has been provided for testing the current functionality of the library.
```bash
$ python3 example.py
```

### Options
timer_s() - Time updates in real-time every second

timer_m() - Time updates in real-time every minute

timer_h() - Time updates in real-time every hour

## Examples
You can call the library by using this syntax:
```python
# This example will print the time to the console every second
from whiterose.whiterose import Whiterose

wr = Whiterose()

def one_s_timer():
    wr.timer_s(1) # 1 second

if __name__ == '__main__':
    one_s_timer()
```

```python
# This example will print the time to the console every 4 seconds
from whiterose.whiterose import Whiterose

wr = Whiterose()

def one_s_timer():
    wr.timer_s(4) # 4 seconds

if __name__ == '__main__':
    one_s_timer()
```

```python
# This example will print the time to the console every 2 minutes
from whiterose.whiterose import Whiterose

wr = Whiterose()

def one_m_timer():
    wr.timer_m(2) # 2 minutes

if __name__ == '__main__':
    one_m_timer()
```