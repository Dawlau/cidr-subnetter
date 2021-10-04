# Cidr subnetter

This is a subnetter that outputs an optimal LAN configuration, based on the CIDR standard. This subnetter has been developed with [Python 3.8](https://www.python.org/).

## Features

The subnetter takes as input a file of the following format (check the input.txt file for an example):
```
<Starting IP>
<name of LAN 1> <number of hosts in the LAN 1>
<name of LAN 2> <number of hosts in the LAN 2>
...
```
The output contains the Network address, Broadcast address and the Range of addresses for every LAN, based on  the starting IP.

Sample output:

```
IP = 142.185.192.192/15
10001110.10111001.11000000.11000000

N.A. = 142.184.0.0/15
B.A. = 142.185.255.255/15
R.A. = 142.184.0.1-142.185.255.254/15

Tirana3
N.A. = 142.184.0.0/19
B.A. = 142.184.31.255/19
R.A. = 142.184.0.1-142.184.31.254/19

Tirana1
N.A. = 142.184.32.0/20
B.A. = 142.184.47.255/20
R.A. = 142.184.32.1-142.184.47.254/20

Tirana2
N.A. = 142.184.48.0/27
B.A. = 142.184.48.31/27
R.A. = 142.184.48.1-142.184.48.30/27
```

## How to run

Create an input file as specified in the Features section and then run:
```
python3 subnet.py
```

## Final notes

I hope you find this subnet tool useful. If you find any bugs, feel free to submit them to blahoviciandrei1@gmail.com
