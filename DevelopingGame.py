n, m = map(int, input().split())

status = [0, 0, 0]

status[0], status[1], status[2] = map(int, input().split()) # x, y, direction

# 입력받는 부분은 예시를 참고하였습니다.
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

count = 0
mov = [[0, 1], [1, 0], [0, -1], [-1, 0]] # x 움직임, y 움직임 / 북, 동, 남, 서 방향 순서

while True:

  i = 1
  array[status[0]][status[1]] = -1
 
  while i <= 4:
    next_dir = (status[2] -i + 4) % 4 # 반시계 방향으로 체크
    next_loc = array[status[0] + mov[next_dir][0]][status[1] + mov[next_dir][1]] # 다음 위치의 값 확인
    i += 1
    if next_loc != 1 and next_loc != -1: # 만약 가보지 않은 육지라면
      #status 업데이트
      status[0] = status[0] + mov[next_dir][0]
      status[1] = status[1] + mov[next_dir][1]
      status[2] = next_dir
      count += 1
      break
    else:
      continue

  if i == 5:
    back_dir = (status[2] + 2) % 4
    back_loc = array[status[0] + mov[back_dir][0]][status[1] + mov[back_dir][1]]

    if back_loc == -1:
      status[0] = status[0] + mov[back_dir][0]
      status[1] = status[1] + mov[back_dir][1]
    else:
        print(count)
        break

  else:
    continue
