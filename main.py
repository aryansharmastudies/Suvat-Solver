from sympy import symbols, solve
def input_known():
    val_name = ["S", "U", "V", "A", "T"]
    val_store = dict()
    for val in val_name:
        inp = input(f"{val}: ")
        val_store[val] = inp  # appends dictionary with key and values.
    return val_store  # returns dictionary with all keys and values.
def known(val_store):
    known = dict()
    for key, val in val_store.items():
        if val != "":
            known[key] = val
        else:
            pass
    return known

def find_formula(val_store, known):  # finding formulas
    ava_keys = list()  # shortform for available keys
    formula = list()
    # print(val_store)
    # print(known)
    # print(known.keys())
    for available in known.keys():
        ava_keys.append(available)
    # print(ava_keys)
    if "S" in ava_keys:  # determines what formulas apply knowing the given values.
        if "U" in ava_keys:
            if "V" in ava_keys:
                formula = ["f4", "f5"]
            elif "A" in ava_keys:
                formula = ["f2", "f4"]
            elif "T" in ava_keys:
                formula = ["f2", "f5"]
        elif "V" in ava_keys:
            if "A" in ava_keys:
                formula = ["f3", "f4"]
            elif "T" in ava_keys:
                formula = ["f3", "f5"]
        elif "A" in ava_keys:
            if "T" in ava_keys:
                formula = ["f2", "f3"]
    elif "U" in ava_keys:
        if "V" in ava_keys:
            if "A" in ava_keys:
                formula = ["f1", "f4"]
            elif "T" in ava_keys:
                formula = ["f1", "f5"]
        elif "A" in ava_keys:
            if "T" in ava_keys:
                formula = ["f1", "f2"]
    elif "V" in ava_keys:
        if "A" in ava_keys:
            if "T" in ava_keys:
                formula = ["f1", "f3"]

    # print(f"formula needed: {formula}")
    return formula
def calculator(known, formula):
    # s, u, v, a, t = 0, 0, 0, 0, 0
    f1 = "((V-U)/T) - A"
    f2 = "((U) * (T) + (1/2) * (A) * (T**2) - S)"
    f3 = "((V) * (T) - (1/2) * (A) * (T**2) - (S))"
    f4 = "((2 * (A) * (S)) + (U**2) - (V**2))"
    f5 = "((((U+V) * (T))/2) - (S))"
    # print(known)
    for eqn in formula:
        if eqn == "f1":
            for key, value in known.items():
                if f1.count(key) > 0:
                    f1 = f1.replace(key, value)
                else:
                    pass
            for char in f1.strip():
                if char.isalpha():
                    char = symbols(char)
                    sol = solve(f1)
                    print(f"{char}: {sol}")

        if eqn == "f2":
            for key, value in known.items():
                if f2.count(key) > 0:
                    f2 = f2.replace(key, value)
                else:
                    pass
            for char in f2.strip():
                if char.isalpha():
                    char = symbols(char)
                    sol = solve(f2)
                    print(f"{char}: {sol}")
        if eqn == "f3":
            for key, value in known.items():
                if f3.count(key) > 0:
                    f3 = f3.replace(key, value)
                else:
                    pass
            for char in f3.strip():
                if char.isalpha():
                    char = symbols(char)
                    sol = solve(f3)
                    print(f"{char}: {sol}")
        if eqn == "f4":
            for key, value in known.items():
                if f4.count(key) > 0:
                    f4 = f4.replace(key, value)
                else:
                    pass
            for char in f4.strip():
                if char.isalpha():
                    char = symbols(char)
                    sol = solve(f4)
                    print(f"{char}: {sol}")
        if eqn == "f5":
            for key, value in known.items():
                if f5.count(key) > 0:
                    f5 = f5.replace(key, value)
                else:
                    pass
            for char in f5.strip():
                if char.isalpha():
                    char = symbols(char)
                    sol = solve(f5)
                    print(f"{char}: {sol}")


if __name__ == "__main__":
    val_store = input_known()
    known = known(val_store) # stores all the variable that are know.
    formula = find_formula(val_store, known)
    calculator(known, formula)