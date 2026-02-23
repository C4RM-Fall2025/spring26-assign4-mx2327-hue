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
    
    return duration/ppy
