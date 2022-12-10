import utils


def move_score_1(opp, me):
    match opp:
        case "A":
            match me:
                case "X":
                    return 3
                case "Y":
                    return 6
                case "Z":
                    return 0
        case "B":
            match me:
                case "X":
                    return 0
                case "Y":
                    return 3
                case "Z":
                    return 6
        case "C":
            match me:
                case "X":
                    return 6
                case "Y":
                    return 0
                case "Z":
                    return 3


def result_score_1(me):
    match me:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3


def move_score_2(opp, me):
    match opp:
        case "A":
            match me:
                case "X":
                    return 3
                case "Y":
                    return 1
                case "Z":
                    return 2
        case "B":
            match me:
                case "X":
                    return 1
                case "Y":
                    return 2
                case "Z":
                    return 3
        case "C":
            match me:
                case "X":
                    return 2
                case "Y":
                    return 3
                case "Z":
                    return 1


def result_score_2(me):
    match me:
        case "X":
            return 0
        case "Y":
            return 3
        case "Z":
            return 6


def calculate_score(scoring_function):
    with utils.get_input(2022, 2) as f:
        return sum(scoring_function(*line.strip().split(" ")) for line in f)


print(calculate_score(lambda opp, me: move_score_1(opp, me) + result_score_1(me)))
print(calculate_score(lambda opp, me: move_score_2(opp, me) + result_score_2(me)))
