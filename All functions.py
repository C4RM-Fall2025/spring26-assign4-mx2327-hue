def WhoAmI():
    return('mx2327')

def getBondPrice(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    r = y / ppy
    C = couponRate * face / ppy
    price = 0
    for t in range(1, periods + 1):
        price += C / (1 + r) ** t
    price += face / (1 + r) ** periods
    return price

def getBondDuration(y, face, couponRate, m, ppy=1):
    periods = m * ppy
    r = y / ppy
    C = couponRate * face / ppy
    price = 0
    weighted_sum = 0
    for t in range(1, periods + 1):
        if t == periods:
            cashflow = C + face
        else:
            cashflow = C
        pv = cashflow / (1 + r) ** t
        price += pv
        weighted_sum += t * pv
    duration = weighted_sum / price
    return duration / ppy

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

def getBondPrice_Z(face, couponRate, times, yc):
    C = couponRate * face
    price = 0
    for y, t in zip(yc, times):
        if t == times[-1]:
            cashflow = C + face
        else:
            cashflow = C
        pv = cashflow / (1 + y) ** t
        price += pv
    return price

def FizzBuzz(a, b):
    result = []
    for n in range(a, b + 1):
        if n % 15 == 0:
            result.append("fizzbuzz")
        elif n % 3 == 0:
            result.append("fizz")
        elif n % 5 == 0:
            result.append("buzz")
        else:
            result.append(n)        
    return result
