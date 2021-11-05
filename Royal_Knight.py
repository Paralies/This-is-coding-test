loc = input()
vert = int(loc[1]) - 1
hor = int(ord(loc[0])) - 97

loc_list = [vert, hor]
mov = [[-2, 1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2] ] #[세로 움직임, 가로 움직임]

i = 0
avail = 0

for i in range(len(mov)):
    movedVert = loc_list[0] + mov[i][0]
    movedHor = loc_list[1] + mov[i][1]

    if movedVert >= 0 and movedVert <= 7:
      if movedHor >= 0 and movedHor <= 7:
        avail += 1

print(avail)
