def series_num(n):
    if n<=0:
        return 0 
    else:
        return n + series_num(n-2)
number = int(input("Enter the number:"))
if number >= 0:
    print("sum:" , series_num(number))
else:
    print("Enter positive number")