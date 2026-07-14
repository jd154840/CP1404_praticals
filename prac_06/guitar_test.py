from guitar import Guitar

in_file = open("guitars.txt", 'r')
for line in in_file:
    part = line.strip().split(',')
    part[1] = int(part[1])
    part[2] = float(part[2])
    guitar = Guitar(part[0], part[1], part[2])
    print(guitar)
in_file.close()

