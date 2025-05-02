def pushDominoes(dominoes: str):
    left_forces = []
    right_forces = []
    left_forces = [0] * len(dominoes)
    right_forces = [0] * len(dominoes)
    n = len(dominoes)

    # pass 1: left to right
    force = 0
    for i in range(n):
        if dominoes[i] == "R":
            force = n
        elif dominoes[i] == "L":
            force = 0
        else:
            force = max(force - 1, 0)
        right_forces[i] = force

    # pass 2: right to left
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == "L":
            force = n
        elif dominoes[i] == "R":
            force = 0
        else:
            force = max(force - 1, 0)
        left_forces[i] = force

    result = list(dominoes)

    for i in range(n):
        if left_forces[i] > right_forces[i]:
            result[i] = "L"
        elif left_forces[i] < right_forces[i]:
            result[i] = "R"
        else:
            result[i] = "."

    return "".join(result)


print(pushDominoes(".L.R...LR..L.."))