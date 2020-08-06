# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def quadratic_residue(p):
    residues = []

    for q in range(1, p):
        for x in range(1, p):
            if x**2 % p == q % p:
                residues.append(q)
                break

    return residues


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i = 101
    print(f'P: {i}, Residues: {quadratic_residue(i)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
