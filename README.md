# Venom - A simple Botnet Implementation

Venom is a simple botnet implementation written in Python using a very basic several bot and one botmaster design.

## Prerequisite

To test this botnet on your local machine, [Python 3](https://www.python.org/)
is required - Has been tested using Python 3.9

## The Components

The project consists of 3 components -

- `bot.py` - A bot which would run an attack when `botmaster.py` sends the command
- `botmaster.py` - The botmaster which is responsible for sending commands
                   to each of the bots
- `cli.py` - This is a cli interface to run commands which tells the botmaster
             what kind of attack needs to be executed as well as can be used to
             stop a running attack

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

You can run as many bots as you like. All the bots would be polling to the same botmaster.

Finally run the `cli.py` to execute commands and run attacks

```bash
python cli.py
```

This would give you a cli interface to run the attacks. Type `help` or `h` to
show a list of possible commands.

