picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# iterate over the picture
for row in picture:
    # the final image
    line = ""
    for pixel in row:
        # if 0 -> ' '
        # if 1 ->  *
        line += "*" if pixel else " "
    # print line-by-line
    print(line)
        