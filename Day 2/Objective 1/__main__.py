point_system = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}


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
    # arr: 2 element array with the first element holding your opponent's play and the second element being your play
    # Returns: total score depending on whether you win, lose, or draw
    if point_system[arr[0]] - point_system[arr[1]] == 0:
        # Both picked the same symbol (Draw)
        return point_system[arr[1]] + 3
    if (
        (arr[0] == "A" and arr[1] == "Z")
        or (arr[0] == "B" and arr[1] == "X")
        or (arr[0] == "C" and arr[1] == "Y")
    ):
        # Opponent wins
        return point_system[arr[1]]
    else:
        # You win
        return point_system[arr[1]] + 6


if __name__ == "__main__":
    main()
