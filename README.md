# KPMG-tennis
python app for technical assessment of KPMG

To run the program run the `main.py` file. The usage is as follows:
```
Usage of the program is: main.py [arg] <arg parameters>
    -f or --file    - file to open follow with valid file path;
    -h or --help    - print this;
```

Score input can be either in the form of:
- manually inputting a score in the form of `player 1 - player 2` when prompted to do so by the program `What is the current score?`
- using the file flag to add a file containing the input one would give to the manual version (run using `python main.py -f [file]`)
- piping the manual input using linux piping (run using `python main.py < [file]`)

> Note that for the last usage of the program the file will need to have a "quit" or "cancel" at the end of the file to immediately quit the program after parsing the file.

Example of an input file content:
```
sdgoh
1-1
4-5
29835-23698
0-0
1-0
2-0
2-1
2-2
2-3
2-4
quit
```

This repo contains this file as well as:
- the main.py program
- a test_scores.txt file to simulate a tennis match