route = []
def q0(st):
    route.clear()
    route.append("q0")
    position = 0
    ch = st[0]
    if ch == "6":
        return q1(st, position + 1)
    elif ch == "7":
        return q11(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q1(st, position):
    route.append("q1")
    ch = st[position]

    if ch == "-":
        return q2(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q2(st, position):
    route.append("q2")
    ch = st[position]

    if ch == "R":
        return q3(st, position + 1)
    elif "S" <= ch <= "Z":
        return q10(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q3(st, position):
    route.append("q3")
    ch = st[position]

    if "R" <= ch <= "Z":
        return q4(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q4(st, position):
    route.append("q4")
    ch = st[position]

    if ch == "-":
        return q5(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q5(st, position):
    route.append("q5")
    ch = st[position]

    if ch == "0":
        return q6(st, position + 1)
    elif "1" <= ch <= "9":
        return q9(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q6(st, position):
    route.append("q6")
    ch = st[position]

    if "1" <= ch <= "9":
        return q7(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q7(st, position):
    route.append("q7")
    ch = st[position]

    if "A" <= ch <= "Z":
        return q8()
    else:
        return {"status": False, "position": position, "route": route}


def q8():
    route.append("q8")
    return {"status": True, "route": route}


def q9(st, position):
    route.append("q9")
    ch = st[position]

    if "0" <= ch <= "9":
        return q7(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q10(st, position):
    route.append("q10")
    ch = st[position]

    if "A" <= ch <= "Z":
        return q4(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q11(st, position):
    route.append("q11")
    ch = st[position]

    if ch == "-":
        return q12(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q12(st, position):
    route.append("q12")
    ch = st[position]

    if "A" <= ch <= "Q":
        return q10(st, position + 1)
    elif ch == "R":
        return q13(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q13(st, position):
    route.append("q13")
    ch = st[position]

    if "A" <= ch <= "U":
        return q4(st, position + 1)
    elif ch == "V":
        return q14(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q14(st, position):
    route.append("q14")
    ch = st[position]

    if ch == "-":
        return q15(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q15(st, position):
    route.append("q15")
    ch = st[position]

    if ch == "0":
        return q16(st, position + 1)
    elif "1" <= ch <= "8":
        return q19(st, position + 1)
    elif ch == "9":
        return q20(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q16(st, position):
    route.append("q16")
    ch = st[position]

    if "1" <= ch <= "9":
        return q17(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q17(st, position):
    route.append("q17")
    ch = st[position]

    if "A" <= ch <= "Z":
        return q18()
    else:
        return {"status": False, "position": position, "route": route}


def q18():
    route.append("q18")
    return {"status": True, "route": route}


def q19(st, position):
    route.append("q19")
    ch = st[position]

    if "0" <= ch <= "9":
        return q17(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q20(st, position):
    route.append("q20")
    ch = st[position]

    if "0" <= ch <= "8":
        return q17(st, position + 1)
    elif ch == "9":
        return q21(st, position + 1)
    else:
        return {"status": False, "position": position, "route": route}


def q21(st, position):
    route.append("q21")
    ch = st[position]

    if "A" <= ch <= "T":
        return q22()
    else:
        return {"status": False, "position": position, "route": route}


def q22():
    route.append("q22")
    return {"status": True, "route": route}
