    def isPalindrome(self, x):
        if x >= 2**31-1 or x <= -2**31: return False
        else:
    
            if x < 0:
                return False
            str_1 = str(x)
            str_2 = str_1[::-1]
            if str_1 == str_2:
                return True
            else:
                return False
