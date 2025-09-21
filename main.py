def print_board() -> None:
    size = 8
    for r in range(size):
        row = []
        for c in range(size):
            row.append('##' if (r + c) % 2 == 0 else '  ')
        print(''.join(row))


if __name__ == "__main__":
    print_board()


