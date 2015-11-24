count = raw_input()

solution = ""
my_array = []

def build_array(inputs):
    if not inputs.split()[0].isdigit():
        return build_solution(my_array)
    else:
        my_array.append(sum([int(dig) for dig in inputs.split() if dig.isdigit()]))

def build_solution(my_array):
    for n in my_array:
        solution += n + " "
    solution = solution.strip()
    return solution        

while True:
    rawin = raw_input()
    build_array(rawin)

