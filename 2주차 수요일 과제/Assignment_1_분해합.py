n = input('자연수를 입력하세요: ')
i = 1
while i <= int(n):
    s = str(i)
    m = i + sum(list(map(int, list(s))))
    if m == int(n):
        print(i)
        break
    if i == int(n):
        print(0)
        break
    i += 1

