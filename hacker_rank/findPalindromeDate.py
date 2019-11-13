import datetime

def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True

def findPalindromeDate(year):
    """
    >>> findPalindromeDate(2016)
    38
    """
    year = int(year)
    assert year > 1000 and year < datetime.MAXYEAR
    checker = datetime.date(year,1,1)
    oneday = datetime.timedelta(days=1)
    count = 0
    while int(checker.year) < year + 100:
        right = "%s" % checker.year
        left = "%d%02d" % (checker.month, checker.day)
        string = "%s%s" % (left, right)
        if len(string)== 8 and left == right[::-1]:
            count += 1
        elif left == right[-3:][::-1]:
            
            count += 1
        checker += oneday
    return count
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    