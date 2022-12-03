from pprint import pprint


def main():
    # Get input from file
    with open("input.txt", "r") as f:
        input_lines = f.readlines()

    # elf_groups: dictionary that holds the list of calories for each elf
    #   - key: index value representing one elf
    #   - value: dictionary holding total calories as one key and all calories list as another
    # cals: list of all calorie totals (OBJECTIVE VALUES contained)
    elf_groups = {}
    temp = []
    cals = []

    for index, line in enumerate(input_lines):
        line = line.strip()
        if len(line) == 0:
            # End of list for previous elf's inventory, next line will be the start of a new elf's inventory
            elf_groups[str(index)] = {}
            elf_groups[str(index)]["all_calories"] = temp
            elf_groups[str(index)]["total_calories"] = count_calories(temp)
            cals.append(elf_groups[str(index)]["total_calories"])
            temp = []
        else:
            temp.append(int(line))
    # Sort all calorie totals with the first index being the most and the last being the least
    cals.sort(reverse=True)
    print("--- OBJECTIVE OUTPUT ---")
    print(f"The top three calorie totals held by elves are: {cals[0:3]}")
    print(
        f"The total count of the top three calorie totals held by elves is: {sum(cals[0:3])}"
    )


def count_calories(arr: list):
    # Count the total calories for a single elf's inventory
    total = 0
    for x in arr:
        total += int(x)
    return total


if __name__ == "__main__":
    main()
