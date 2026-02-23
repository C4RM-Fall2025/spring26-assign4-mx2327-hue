df getBondPrice(y,face,couponRate,m,ppy=1):
    periods = m * ppy
    r = y / ppy
    C = coupon * face / ppy
    price = 0
    for t in range(1, periods + 1):
        price += C / (1 + r) ** t
    price += face / (1 + r) ** periods
    return price
