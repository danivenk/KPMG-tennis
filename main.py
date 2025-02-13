import sys


def main(argv):
    """
        main function of the program, it takes 2 scores and prints the result
            to the terminal
    """

    match len(argv):
        case 4 if (argv[0] == "-p1" and argv[2] == "-p2"):
            try:
                p1 = int(argv[1])
                p2 = int(argv[3])
            except ValueError:
                usage()
        case _:
            usage()

    scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    match p1-p2:
        case 2 if p1 >= 4:
            print("Player 1 wins!")
        case 1 if p1 >= 3:
            print("Advantage for player 1")
        case 0 if p1 >= 3:
            print("Deuce")
        case -1 if p2 >= 3:
            print("Advantage for player 2")
        case -2 if p2 >= 4:
            print("Player 2 wins!")
        case _ if p1-p2 > 2:
            print("Player 1 wins!\nScore beyond normal score")
        case _ if p2-p1 > 2:
            print("Player 2 wins!\nScore beyond normal score")
        case _:
            print(f"Score (p1 - p2):\t{scores[p1]} - {scores[p2]}")

    return 0


def usage():
    """
        usage print of the code and exit out.
    """

    print(f"\n{sys.argv[0]} -p1 [score] -p2 [score]\n"
          "\t-p1\t- score of player 1\n"
          "\t-p2\t- score of player 2\n")
    exit()


if __name__ == "__main__":
    main(sys.argv[1:])
