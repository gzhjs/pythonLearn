def checkConflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX - state[i]) in (0, nextY - i):#如果在同一行或同一对角线则冲突
            return True
    return False

def solve(num, state=()):
    for pos in range(num):
        if not (checkConflict(state, pos)):
            if(len(state) == num - 1):# 如果是最后一个皇后，直接产出；否则，进行下一步的递归
                yield (pos,)
            else:
                for result in solve(num, state+(pos,)):
                    yield (result + (pos,))

def printQueens(solutions, num = 8):
    index = 1; # 解法记数
    for solution in solutions:
        print(str(index) + "==============")
        for i in solution:
            print(". " * i + "X " + ". " * (num - i - 1))
        index += 1

res = solve(8)
printQueens(res)