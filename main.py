N = 25
dies = "#"
point = "."


#решения
def pic1(placeX, placeY):
    return dies if placeX > placeY else point

def pic2(placeX, placeY):
    return dies if placeX == placeY else point

def pic3(placeX, placeY):
    return dies if placeX == N -1 - placeY else point

def pic4(placeX, placeY):
    return dies if placeX - 6 < N-1 -placeY else point

def pic5(placeX, placeY):
    return dies if placeX >= placeY * 2 and placeX <= placeY * 2 +1 else point

def pic6(placeX, placeY):
    return dies if placeX < 10 or placeY < 10 else point

def pic7(placeX, placeY):
    return dies if placeX > N - 10 and placeY > N - 10 else point

def pic8(placeX, placeY):
    return dies if placeX * placeY == 0 else point

def pic9(placeX, placeY):
    return dies if abs(placeX-placeY) > 10 else point

def pic10(placeX, placeY):
    return dies if placeX  > placeY and placeX <= 2 * placeY +1  else point


def pic11(placeX, placeY):
    return dies if placeX  == 1 or placeX == N -2 or placeY == 1 or placeY == N-2 else point


def pic12(placeX, placeY):
    return dies if (placeX * placeX + placeY * placeY) <= 400 else point

#рисуем решение
for placeY in range(0,N):
    for placeX in range(0,N):
        magic = pic12(placeX, placeY)
        print(magic, end=' ')
    print('\n')

