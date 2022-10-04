# get_n asks the user to input the number of members in the coalition, and saves this as n
def get_n():
    while True:
        try:
            get_n.n = int(input("How many members are in the coalition?:"))
            break
        except ValueError:
            print("Enter an integer")


# powerset creates a list containing every unique subset of its input.
def powerset(x):
    powerset.powerlist = []
    temp = []
    for i in range(2 ** len(x)):
        s = list((bin(i).replace("0b", "")))
        if i > 0:
            powerset.powerlist.append(temp)
        temp = []
        for p in range(len(s)):
            if s[p] == '1':
                temp.append(x[len(s) - p - 1])
    powerset.powerlist.append(temp)


def get_v():
    for i in range(0, len(powerset.powerlist)):
        while True:
            try:
                s = int(input("State the value of coalition " + str(i + 1) + " of " + str(len(powerset.powerlist))
                              + ":" + str(powerset.powerlist[i]) + " "))
                break
            except ValueError:
                print("Enter an integer")
        if len(powerset.powerlist[i]) > 0:
            t = s / len(powerset.powerlist[i])
            for g in range(0, len(powerset.powerlist[i])):
                dic.shap[(powerset.powerlist[i])[g]] += int(t)


def dic():
    dic.shap = {}
    for i in range(1, get_n.n + 1):
        dic.shap[i] = 0


get_n()
powerset(list(range(1, get_n.n + 1)))
dic()
get_v()
print(dic.shap)
