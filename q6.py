def find_max(num1, num2, num3, num4):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    return max_num

print(find_max(10, 20, 30, 40))
print(find_max(100, 200, 300, 400))