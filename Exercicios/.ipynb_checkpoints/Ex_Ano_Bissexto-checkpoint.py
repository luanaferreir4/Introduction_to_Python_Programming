def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 == 0:
            return False
        else:
            return True

    return leap


assert is_leap(2000) == True
assert is_leap(2001) == False
assert is_leap(2002) == False
assert is_leap(2003) == False
assert is_leap(2004) == True
assert is_leap(2005) == False






year = int(input())
print(is_leap(year))
