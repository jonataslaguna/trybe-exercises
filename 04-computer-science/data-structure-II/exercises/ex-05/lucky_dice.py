def get_seven(rolls):
    seen_before = set()
    lucky_rolls = []
    for roll in rolls:
        if 7-roll in seen_before:
            lucky_rolls.append((7-roll, roll))
            seen_before.discard(7-roll)
        else:
            seen_before.add(roll)
    return lucky_rolls


if __name__ == "__main__":
    rolls = [1, 2, 3, 5, 6, 2, 3, 3, 2, 4, 2, 1, 1]

    print(get_seven(rolls))
