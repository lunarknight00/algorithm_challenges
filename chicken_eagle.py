#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

def solve(data, moves):
    i = 0
    m = len(moves)
    j = 0
    while i < len(moves) - 1:
        print(i)
        j = i +1
        if moves[i] != moves[i+1]:
            print(moves[i])
            data.pop(moves[i]-1)
        print(data)
        i = i + 2
    if len(data)>0:
        print("Success!",end = " ")
        data = sorted(data)
        for n in data:
            print(n, end = " ")

if __name__ == "__main__":
    # 读取第一行的n
    dim = sys.stdin.readline().strip()
    dim = dim.split()
    n,m = dim
    n = int(n)
    m = int(m)
    value1 = sys.stdin.readline().strip()
    chickens = list(map(int, value1.split()))
    value2 = sys.stdin.readline().strip()
    moves = list(map(int, value2.split()))
    solve(chickens, moves)