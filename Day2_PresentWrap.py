def calc_lower_perimeter(l,w,h):
    perimeter_a = 2 * l + 2 * w
    perimeter_b = 2 * w + 2 * h
    perimeter_c = 2 * l + 2 * h

    if (perimeter_a < perimeter_b):
        if perimeter_a < perimeter_c:
            return perimeter_a
        else:
            return perimeter_c
    else:
        if (perimeter_b < perimeter_c):
            return perimeter_b
        else:
            return perimeter_c
##print(calc_lower_perimeter(2,3,4))

ribbon = 0
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

        ribbon = ribbon + calc_lower_perimeter(l, w, h) + l*w*h

print(surfacet)
print(ribbon)