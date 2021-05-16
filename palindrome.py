def isPalindrome(x):

    y = x[::-1]
    return  y == x

"""
x = input("Input a string to check if it's a palindrome: ")

if isPalindrome(x):
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")
"""

def test_isPalindrome():
    example = 'Testset'
    expected = True
    result = isPalindrome(example)
    assert result == expected