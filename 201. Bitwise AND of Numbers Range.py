
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        tmp=m
        i=1
        result=0
        while tmp > 0:
            if tmp%2 == 1:
                if m + ( (2 ** i) - (((2**i)-1) & m)) > n:
                    result |= 2**(i-1)
            tmp //= 2
            i += 1
        return result

sln=Solution()
assert 4== sln.rangeBitwiseAnd(5,7)
assert 0== sln.rangeBitwiseAnd(0,1)
assert 1== sln.rangeBitwiseAnd(1,1)
assert 32== sln.rangeBitwiseAnd(46,55)
assert 32== sln.rangeBitwiseAnd(45,55)
assert 32== sln.rangeBitwiseAnd(46,55)
assert 4096== sln.rangeBitwiseAnd(4567,5588)
assert 8== sln.rangeBitwiseAnd(9,15)
assert 0== sln.rangeBitwiseAnd(1,2)
assert 0== sln.rangeBitwiseAnd(125,129)
