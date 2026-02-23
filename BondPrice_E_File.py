def getBondPrice_E(face, couponRate, yc):
    C = couponRate * face
    price = 0
    for t, y in enumerate(yc, start=1):
        if t == len(yc):
            cashflow = C + face
        else:
            cashflow = C
        pv = cashflow / (1 + y) ** t
        price += pv
    return price
