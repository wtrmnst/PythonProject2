def pasture_area(wire, w):
    l = wire - 2 * w
    return float(w * l) if l > 0 else 0.0

def best_pasture(wire):
    w = wire / 4
    l = wire - 2 * w
    area = pasture_area(wire, w)
    return (float(w), float(l), float(area))