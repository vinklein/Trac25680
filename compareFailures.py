sep = '*' * 70+'\n'
file_a = 'py3.6testall.log'
file_b = 'py3.7testall.log'


def process_lines(lines):
    look_next_line = False
    res = []
    for line in lines:
        if not look_next_line and line == sep:
            look_next_line = True
        elif look_next_line and line != sep:
            look_next_line = False
            if line[:4] == 'File':
                t = line.split()
                # create an error 'id' with <filename>:<line>
                res.append('{0}:{1}'.format(t[1][1:-2], t[3][:-1]))
    return res


if __name__ == "__main__":
    import os
    print(os.getcwd())

    with open(file_a, 'r') as file:
        lines_a = file.readlines()

    with open(file_b, 'r') as file:
        lines_b = file.readlines()

    print(len(lines_a))
    ids_a = process_lines(lines_a)
    ids_b = process_lines(lines_b)

    print("nb doctests failures with python3.6: {}".format(len(ids_a)))
    print("nb doctests failures with python3.7: {}".format(len(ids_b)))

    b_not_in_a = []
    for e in ids_b:
        if e not in ids_a:
            b_not_in_a.append(e)

    a_not_in_b = []
    for e in ids_a:
        if e not in ids_b:
            a_not_in_b.append(e)

    print("new python3.7 failures : {}".format(len(b_not_in_a)))
    print("python3.6 failures not appearing with python 3.7 : {}".format(len(a_not_in_b)))

    print("Some new failures with python3.7")
    # Sample of new failures ids
    for i in range(5):
        from random import randint
        print(b_not_in_a[randint(0, len(b_not_in_a)-1)])
