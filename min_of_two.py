count = raw_input()

my_sums = []
my_sums2 = []
my_sol = ""

for i in range(int(count)):
    pair = raw_input()
    my_sums.append(pair)

for k in range(int(count)):
    fst = int(my_sums[k].split()[0])
    snd = int(my_sums[k].split()[1])
    my_sums2.append(min(fst,snd))

for j in range(len(my_sums2)):
    my_sol += str(my_sums2[j]) + " "

#print my_sums
print my_sol
