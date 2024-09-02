
    queen = NQueen(n)
    solutions = queen.solve_nq()
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(row)
        print()