# def arrayCheck(nums):
#     n = 0
#     while n < (len(nums)-2):
#         if nums[n]==1 and nums[n+1]==2 and nums[n+2]==3:
#             print("True")
#             return True
#         n += 1
#     print("False")
#     return False
#
# arrayCheck([1, 1, 2, 3, 1])
# arrayCheck([1, 1, 2, 4, 1])
# arrayCheck([1, 1, 2, 1, 2, 3])
#
#
# def stringBits(str):
#     print(str[::2])
#     return str[::2]
#
# stringBits('Hello')
# stringBits('Hi')
# stringBits('Heeololeo')


#
# def end_other(a, b):
#     str = ""
#     if len(a) >= len(b):
#         print(b.lower() in (a[-len(b):].lower()))
#         return(b.lower() in (a[-len(b):].lower()))
#     else:
#         print(a.lower() in (b[-len(a):].lower()))
#         return(a.lower() in (b[-len(a):].lower()))
#
# end_other('Hiabc', 'abc')
# end_other('AbC', 'HiaBc')
# end_other('abc', 'abXabc')
# end_other('ab', 'abXXXiiii')
# # end_other('a;ldkfa', 'fa')
#
#
# def doubleChar(str):
#     nStr=""
#     for char in str:
#         nStr += (2*char)
#
#     print(nStr)
#     return(nStr)
#
# doubleChar("the")
# doubleChar("Zach")

# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3
#
# def no_teen_sum(a, b, c):
#     print(fix_teen(a) + fix_teen(b) + fix_teen(c))
#     return(fix_teen(a) + fix_teen(b) + fix_teen(c))
#
# def fix_teen(n):
#     if n == 15 or n == 16:
#         return (n)
#     elif n >=13 and n <= 19:
#         return (0)
#     else:
#         return(n)
#
# no_teen_sum(1, 2, 3)
# no_teen_sum(2, 13, 1)
# no_teen_sum(2, 1, 14)
# no_teen_sum(15, 16, 8)


# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    evens = filter(even_nums, nums)
    print(len(list(evens)))
    return(len(list(evens)))

def even_nums(n):
    return n%2 == 0


count_evens([2,1,2,3,4])
count_evens([2,2,0])
count_evens([1,3,5])



def count_evens_two(nums):
    evens = filter(lambda n:n%2 == 0, nums)
    print(len(list(evens)))
    return(len(list(evens)))

count_evens_two([2,1,2,3,4])
count_evens_two([2,2,0])
count_evens_two([1,3,5])
