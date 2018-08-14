#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    """
    Enter a list as a parameter
    Function will return if 1,2,3 is anywhere in the list
    """
    n = 0
    while n < (len(nums)-2):
        if nums[n]==1 and nums[n+1]==2 and nums[n+2]==3:
            print("True")
            return True
        n += 1
    print("False")
    return False

arrayCheck([1, 1, 2, 3, 1])
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
    """
    Parameter = any string
    Returns str with every other letter missing starting with str[1]
    """

    print(str[::2])
    return str[::2]

stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')


#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    """
    Given two strings, will return if one string is at the end of the other.
    NOT CASE SENSITIVE
    """
    if len(a) >= len(b):
        print(b.lower() in (a[-len(b):].lower()))
        return(b.lower() in (a[-len(b):].lower()))
    else:
        print(a.lower() in (b[-len(a):].lower()))
        return(a.lower() in (b[-len(a):].lower()))


#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    nStr=""
    for char in str:
        nStr += (2*char)

    print(nStr)
    return(nStr)


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    print(fix_teen(a) + fix_teen(b) + fix_teen(c))
    return(fix_teen(a) + fix_teen(b) + fix_teen(c))

def fix_teen(n):
    if n == 15 or n == 16:
        return (n)
    elif n >=13 and n <= 19:
        return (0)
    else:
        return(n)


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    evens = filter(even_nums, nums)
    print(len(list(evens)))
    return(len(list(evens)))

def even_nums(n):
    return n%2 == 0


# or better way below using lambda

def count_evens_two(nums):
    evens = filter(lambda n:n%2 == 0, nums)
    print(len(list(evens)))
    return(len(list(evens)))
