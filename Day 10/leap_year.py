def leap_year(year):
    """
    it checks whether a year is a leap year or not 
    """
    is_leap_year=False
    if year%4==0:
        if year %100==0:
            if year %400==0:
                return True
            else :
                return False
        else:
            return True
    else :
        return False
    


print(leap_year(1989))