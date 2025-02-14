import sys


def main(argv: list[str]) -> int:
    """
        main function of the program, it takes 2 scores and prints the result
            to the terminal

        Arguments:
            argv [list[str]] - list of commandline args to run the program with;
    """

    # main match switch
    match len(argv):

        # if file arg given pare output line by line.
        case 2 if (argv[0] == "-f" or argv[0] == "--file"):
            try:
                with open(argv[1], "r") as file:
                    for line in file:
                        parse_input(line.rstrip())
            except FileNotFoundError:
                usage(True)

        # print help if requested
        case 1 if (argv[0] == "-h" or argv[0] == "--help"):
            usage()

        # else run main loop
        case 0:
            while True:

                # ask score
                input_str = input("What is the current score? \n")

                # if cancel or quit is prompted stop
                if "cancel" in input_str or "quit" in input_str:
                    break

                parse_input(input_str.rstrip())
        case _:
            usage(True)

    return 0


def parse_input(in_str: str):
    """
        parse an input string including error handling

        Arguments:
            in_str [str] - string to parse;
    """

    try:
        print(f"{in_str} -> {get_score(*in_str.split("-"))}")
    except (ValueError, TypeError):
        print(f"{in_str} is an invalid input")


def get_score(player1: int, player2: int) -> str:
    """
        gets the score string given a score for player 1 and player 2

        Arguments:
            player1 [int] - score for player 1;
            player2 [int] - score for player 2;

        returns the score string
    """

    # make sure the variables are the right type
    try:
        assert player1 is int and player2 is int
    except AssertionError:
        player1 = int(player1)
        player2 = int(player2)

    # dict for the names of each score
    scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    # scoring logic
    match player1-player2:
        case 2 if player1 >= 4:
            return "Player 1 wins!"
        case 1 if player1 >= 3:
            return "Advantage for player 1"
        case 0 if player1 >= 3:
            return "Deuce"
        case -1 if player2 >= 3:
            return "Advantage for player 2"
        case -2 if player2 >= 4:
            return "Player 2 wins!"
        case _ if player1-player2 > 2:
            return "Player 1 wins!\nScore beyond normal score"
        case _ if player2-player1 > 2:
            return "Player 2 wins!\nScore beyond normal score"
        case _:
            return "Score (player1 - player2):" \
                   f"\t{scores[player1]} - {scores[player2]}"


def usage(exit_bool: bool = False):
    """
        usage print of the code and exit out.

        Arguments:
            exit_bool [bool] - should it exit the program
    """

    print(f"\nUsage of the program is: {sys.argv[0]} [arg] <arg parameters>\n"
          "\t-f or --file\t- file to open follow with valid file path;\n"
          "\t-h or --help\t- print this;\n")

    if exit_bool:
        exit()


if __name__ == "__main__":
    main(sys.argv[1:])
