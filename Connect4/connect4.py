# 입력 번호 정보

#  0  1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31 32 33 34
# 35 36 37 38 39 40 41
# 42 43 44 45 46 47 48


def board(entry):
    for i in range(0, 49, 7):
        print(entry[i:i+7])
    print(f'turn = {turn}')
    print("\n")

player1 = input("게임을 시작하는 플레이어의 이름을 입력하세요: ")
player2 = input("두번째 플레이어의 이름을 입력하세요: ")
entry = [0] * 49  # 보드를 49칸으로 초기화 (7x7)

turn = 1
gameover = 0

# 게임 진행 시퀀스
while turn <= 48 and gameover == 0: 
    board(entry)  # 현재 보드 상태를 출력
    c = int(input("원하는 칸을 선택하세요 (0-48): "))
    
    if entry[c] != 0:  # 이미 선택된 칸인지 확인
        print("이미 선택된 칸입니다. 다른 칸을 선택하세요.")
        continue

    # 밑에 줄이 비어있는지 확인 (밑에 칸이 차 있어야 함)
    while c <= 41 and entry[c + 7] == 0:
        c += 7

    if turn % 2 == 1: 
        entry[c] = 1  # 선공
    else: 
        entry[c] = 2  # 후공
    turn += 1
    
    # 게임 종료 시퀀스
    for i in range(0, 43, 7):  # 가로로 4개
        for j in range(i, i + 4):
            if entry[j] == entry[j + 1] == entry[j + 2] == entry[j + 3] != 0: 
                if entry[j] == 1: 
                    print(f'{player1}이 승리했습니다!')
                else: 
                    print(f'{player2}이 승리했습니다!')
                gameover = 1
                break

    for i in range(7):  # 세로로 4개
        for j in range(i, 22, 7):  # 인덱스 범위를 조정하여 21을 넘지 않도록 수정
            if entry[j] == entry[j + 7] == entry[j + 14] == entry[j + 21] != 0: 
                if entry[j] == 1: 
                    print(f'{player1}이 승리했습니다!')
                else: 
                    print(f'{player2}이 승리했습니다!')
                gameover = 1
                break

    for i in [3, 2, 10, 1, 9, 17, 0, 8, 16, 24, 7, 15, 23, 14, 22, 21]:  # 왼쪽 위 -> 오른쪽 아래 대각선
        if entry[i] == entry[i + 8] == entry[i + 16] == entry[i + 24] != 0:
            if entry[i] == 1: 
                print(f'{player1}이 승리했습니다!')
            else: 
                print(f'{player2}이 승리했습니다!')
            gameover = 1
            break

    for i in [21, 28, 22, 35, 29, 23, 42, 36, 30, 24, 43, 37, 31, 44, 38, 45]:  # 오른쪽 위 -> 왼쪽 아래 대각선
        if entry[i] == entry[i - 6] == entry[i - 12] == entry[i - 18] != 0:
            if entry[i] == 1: 
                print(f'{player1}이 승리했습니다!')
            else: 
                print(f'{player2}이 승리했습니다!')
            gameover = 1
            break

print("게임이 종료되었습니다.")
