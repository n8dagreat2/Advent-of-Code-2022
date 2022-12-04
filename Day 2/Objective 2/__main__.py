point_system = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}


def main():
    with open("input.txt", "r") as f:
        input_lines = f.readlines()

    # Objective variable, holds your score
    total_score = 0

    for i in input_lines:
        total_score += point_outcome(i.strip().split())

    print("--- OBJECTIVE OUTPUT ---")
    print(f"Your total score is {total_score} after {len(input_lines)} round(s)")


def point_outcome(arr: list):
    # arr: 2 element array with the first element holding your opponent's play and the second element is the outcome according to your side
    # Returns: total score depending on whether you win, lose, or draw
    if arr[1] == "Y":
        # Outcome needs to be a draw
        return point_system[arr[0]] + point_system[arr[1]]
    if arr[1] == "X":
        # Opponent wins, you lose
        if arr[0] == "A":
            # Opponent chooses rock, thus you choose scissors
            return point_system["C"] + point_system[arr[1]]
        elif arr[0] == "B":
            # Opponent chooses paper, thus you choose rock
            return point_system["A"] + point_system[arr[1]]
        elif arr[0] == "C":
            # Opponent chooses scissors, thus you choose paper
            return point_system["B"] + point_system[arr[1]]
    else:
        # You win
        if arr[0] == "A":
            # Opponent chose rock, thus you choose paper
            return point_system["B"] + point_system[arr[1]]
        elif arr[0] == "B":
            # Opponent chose paper, thus you choose scissors
            return point_system["C"] + point_system[arr[1]]
        elif arr[0] == "C":
            # Opponent chose scissors, thus you choose rock
            return point_system["A"] + point_system[arr[1]]


if __name__ == "__main__":
    main()
