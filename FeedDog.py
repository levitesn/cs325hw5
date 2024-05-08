def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    i, j = 0, 0
    satisfied_dogs = 0

    while i < len(hunger_level) and j < len(biscuit_size):
        if biscuit_size[j] >= hunger_level[i]:
            satisfied_dogs += 1
            i += 1
        j += 1

    return satisfied_dogs