def check_year(year):
    year = str(year)
    slice1 = year[0:2]
    slice2 = year[2:4]
    int1 = int(slice1)
    int2 = int(slice2)
    year = int(year)

    if (int1 + int2)**2 == year:
        return True
    else:
        return False
    
def check_year1(year):
    first_two = year // 100
    second_two = year % 100
    return (first_two + second_two)**2 == year 


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False

    print(check_year1(1995)) # False
    print(check_year1(2024)) # False
    print(check_year1(2025)) # True
    print(check_year1(2026)) # False
    print(check_year1(3025)) # True
    print(check_year1(5555)) # False