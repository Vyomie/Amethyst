 
def test(cords):
    update = '18,428'
    for i in range(1, 101):
        if i < 11:
            row = 1
        else:
            if str(i)[1] == '0':
                row = int(str(i-1)[0])
            else:
                if i > 90:
                    row = 10
                else:
                    row = int(str(i+10)[0])
        x, y = update.split(",")
        x = float(x)
        y = float(y)
        if i%10 != 0:
            if row % 2 == 0:
                x = x - 45.5
            else:
                x = x + 45.5
        else:
            y = y - 45.5

        cord = f'{x},{y}'
        update = cord
        cords.append(cord)