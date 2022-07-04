#leetcode
 def isPalindrome(self, x: int) -> bool:
        X = x
        if x < 0 or (x % 10 == 0 and X != 0):
            return False
        rev = 0
        while x != 0:
            rev = rev*10 + x % 10
            x //= 10
        return True if rev == X else False
#check this code

#submission abuot permutations that fails 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        partial=[]
        partial.append(s1[0])
        for i in range(1,len(s1)):
            for j in reversed(range(len(partial))):
                curr = partial.pop(j)
                for k in range(len(curr)+1):
                    partial.append(curr[:k]+s1[i]+curr[k:])
        for i in partial:
            if i in s2:
                return True
        return False

#
#
#
#
#
#
#
#
#
Satellites are falling! All the time.

To paraphrase Buzz Lightyear, “Satellites don’t orbit - they fall…with style.”

Here’s how orbiting works:

Jump straight down off a chair. Let’s call this “falling”.
Notice that you land directly in front of the chair.
Now, repeat the jump, but this time move sideways a bit when you jump. (please be careful!)
Notice that you land off to the side of the chair.
Now, imagine you were able to move sideways very fast while jumping off the chair. You’d move farther and farther away from the chair before you landed.
Now, imagine you were able to move sideways REALLY fast while jumping off the chair. You’d eventually move so far from the chair that the Earth would curve beneath you.
Eventually, if you were moving sideways fast enough, you’d never “catch” the ground. You’d just keep falling…forever.