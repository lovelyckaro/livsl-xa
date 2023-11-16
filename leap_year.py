
def is_divisible_by(n: int, divisor:int) -> bool:
    """ Returns if n is evenly divisible by divisor    
    """
    return n % divisor == 0

def is_leap_year(year: int) -> bool:
    """ Returns if the year is a leap year
        A year is a leap year if it is divisible by four,
        except if it is divisible 100, then it is not a leap year,
        except except if it is divisible by 400 then it is a leap year anyways
    """
    divisible_by_four = is_divisible_by(year, 4)
    divisible_by_hundred = is_divisible_by(year, 100)
    divisible_by_fourhundred = is_divisible_by(year, 400)
    return divisible_by_four and ((not divisible_by_hundred) or divisible_by_fourhundred)

year = input("Year: ")
if is_leap_year(int(year)):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")
    
    