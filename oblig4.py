"""
There are N queens on a chess board of NxN
How can they be positioned so that none of them attacks another according to the rules of chess:
2 queens can not be on:
the same row
the same column
the same diagonal

examine partial solujtion:
if 2 queens attack each other, reject it
if it has N=4 queens, accept as solution
otherwise contine

"""
# N = 5
COLUMNS = 'abcde'
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []


def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i],partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2)


def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        all_solutions.append(partial_sol)
        print(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)


def is_solution(candidate_solution):
    is_valid = False
    solve([])
    print(all_solutions)
    for sol in all_solutions:
        if sol == candidate_solution:
            is_valid = True
    print(f'Is candidate solution: {candidate_solution} valid? {is_valid}')

#solve([])


is_solution(['a1', 'd2', 'b3', 'e4', 'c5'])
