# Venom - A simple Botnet Implementation

Venom is a simple botnet implementation written in Python using a very basic
several bot and one botmaster design.

## Prerequisite

To test this botnet on your local machine, [Python 3](https://www.python.org/)
is required - Has been tested using Python 3.9

## The Components

The project consists of 3 components -

- `bot.py` - A bot which would run an attack when `botmaster.py` sends the
             command
- `botmaster.py` - The botmaster which is responsible for sending commands
                   to each of the bots
- `cli.py` - This is a cli interface to run commands which tells the botmaster
             what kind of attack needs to be executed as well as can be used to
             stop a running attack

## Working

The `cli.py` is a basic cli interface which takes in the input from the user
and verifies the input command and writes the command to `target.txt`.

The `botmaster.py` is a simple TCP server that listens to connections from bots.
When a bot connects to the botmaster, the botmaster reads the command to be sent
from `target.txt` and replis with the same (closing the connection thereafter).

The `bot.py` is the bot that attacks the target machines. It polls the botmaster
every `20 seconds` (variable) and executes the command received. If the command
`NONE` is received, the bot doesn't do anything and waits for another `20 seconds`
to poll again.

The `cli.py` accepts commands in the following format

```python
SEND <attack-type> <target-address> <target-port> <N>
```

Here,

- `<attack-type>` - The type of attack that needs to be executed
- `<target-address>` - The address (domain name or IP address) of the target server
- `<target-port>` - The port of the target to which the bots need to connect
- `<N>` - Number of connections each bot should initiate to the target

The `<attack-type>` can be

- `TCP-SYN` - Each bot creates N threads to connect to the target, creates TCP
              connections and closes the conenctions after a delay of 1 second.
- `HTTP` - Each bot creates N threads and connects to the target, sending HTTP
           requests to the target.
- `UDP` - Each bot creates N threads and sends a "Hello" message to the target
          using UDP.

## Usage

Start by cloning the repository and setting the current working directory
to the source

```bash
git clone https://github.com/aneeshsharma/Venom
cd Venom
```

Now, firstly start the `botmaster.py` using

```bash
python botmaster.py
```

> Note: On some systems it might be required to use `python3` instead

Then, for the purpose of demonstration, you can run a few bots on your local
machine. To run a bot use

```bash
python bot.py
```

You can run as many bots as you like. All the bots would be polling to the same
botmaster.

Finally run the `cli.py` to execute commands and run attacks

```bash
python cli.py
```

This would give you a cli interface to run the attacks. Type `help` or `h` to
show a list of possible commands.

