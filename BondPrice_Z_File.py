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
