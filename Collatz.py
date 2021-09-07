import time
knowns = [1, 2, 4]
start_pos = 100
current = []

def main(x):
    if x % 2 != 0:
        x = x * 3 + 1
        return int(x)
    else:
        x = x / 2
        return int(x)

while True:
    time.sleep(0.05)
    print(start_pos)
    if start_pos in knowns:
        start_pos -= 1
        continue
    current.append(start_pos)
    num = main(start_pos)
    while num not in knowns:
        print(num)
        time.sleep(1)
        current.append(num)
        num = main(num)
    knowns = knowns + current
    start_pos -=1
    print(knowns)
    

    

