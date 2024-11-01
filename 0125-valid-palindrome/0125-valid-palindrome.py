class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = [char.lower() for char in s if char.isalnum()]

        n = len(pal)
        
        if n % 2 == 1:
            p1 = pal[:n//2+1]
        else:
            p1 = pal[:n//2]
            
        p2 = pal[n:n//2-1:-1]

        for c1, c2 in zip(p1, p2):
            if c1 != c2:
                return False

        return True