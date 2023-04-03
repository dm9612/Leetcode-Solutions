class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x==0:
            return True
        else:
            str_x = str(x)
            reverse_str_x = str_x[::-1]
            reverse_int_x = int(reverse_str_x)
            return x == reverse_int_x
