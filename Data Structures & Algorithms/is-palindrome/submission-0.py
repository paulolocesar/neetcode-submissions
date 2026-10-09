class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []

        for l in s:
            if l.isalnum():
                word.append(l.lower())

        return word == word[::-1]