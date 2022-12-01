surfacet = 0
with open('Day2Input.txt') as f:
    for line in f:
        values = line.rstrip().rsplit("x")
        l = int(values[0])
        w = int(values[1])
        h = int(values[2])
        a=l*w
        b=w*h
        c=l*h
        if a < b:
            if a < c:
                small_side_area = a
            else:
                small_side_area = c
        else:
            if b < c:
                small_side_area = b
            else:
                small_side_area = c

        surface = (2 * l * w + 2 * w * h + 2 * l * h) + small_side_area
        surfacet = surfacet + surface

print(surfacet)