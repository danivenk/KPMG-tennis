import sys


def main(argv):
    """
        main function of the program, it takes 2 scores and prints the result
            to the terminal
    """

    # match len(argv):
    #     case 4 if (argv[0] == "-p1" and argv[2] == "-p2"):
    #         try:
    #             p1 = int(argv[1])
    #             p2 = int(argv[3])
    #         except ValueError:
    #             usage()
    #     case _:
    #         usage()

    # a = "1 - 1"
    # b = a.split("-")

    # print(b)
    # print(int(b[0]), int(b[1]))

    # print(get_score(1, "2"))

    while True:
        input_str = input("What is the current score? \n")

        if "cancel" in input_str or "quit" in input_str:
            break

        try:
            print(get_score(*input_str.split("-")))
        except (ValueError, TypeError):
            pass

    return 0


def get_score(player1: int, player2: int) -> str:
    """
        gets the score string given a score for player 1 and player 2

        Arguments:
            player1 [int] - score for player 1;
            player2 [int] - score for player 2;
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


def usage():
    """
        usage print of the code and exit out.
    """

    # usage print statement
    print(f"\n{sys.argv[0]} -p1 [score] -p2 [score]\n"
          "\t-p1\t- score of player 1\n"
          "\t-p2\t- score of player 2\n")
    exit()


if __name__ == "__main__":
    main(sys.argv[1:])
