i = 1
while i <= 9:
    j = 1
    while j <= i:  # j是列,i是行,列要小于行
        print(f'{j}*{i}={j * i}', end='\t')
        j = j + 1
    print()
    i = i + 1
