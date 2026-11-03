def pasture_area(wire, w):
    l = (wire - 2 * w)/3
    if l < 0:
        return 0.0
    return w * l

def best_pasture(wire):
    w = wire / 4
    l = (wire - 2 * w)/3
    return (w, l, w*l)
