
def longest_palindromic_substring(text):
    '''
    Findes the longest palindromic substring in a string
    Input: string
    )utput: string
    '''
    if not isinstance(text, str):
        raise ValueError('Input is not a string')
    if len(text) <= 0:
        raise ValueError('Input string is empty')
    longest = ''
    for i in range(len(text)):
        for j in range(i, len(text)):
            if text[i:j+1] == text[i:j+1][::-1]:
                if len(text[i:j+1]) > len(longest):
                    longest = text[i:j+1]
    return longest


# class Solution(object):
#    def longestPalindrome(self, s):
#       dp = [[False for i in range(len(s))] for i in range(len(s))]
#       for i in range(len(s)):
#          dp[i][i] = True
#       max_length = 1
#       start = 0
#       for l in range(2,len(s)+1):
#          for i in range(len(s)-l+1):
#             end = i+l
#             if l==2:
#                if s[i] == s[end-1]:
#                   dp[i][end-1]=True
#                   max_length = l
#                   start = i
#             else:
#                if s[i] == s[end-1] and dp[i+1][end-2]:
#                   dp[i][end-1]=True
#                   max_length = l
#                   start = i
#       return s[start:start+max_length]


if __name__ == '__main__':
    print(longest_palindromic_substring('banana'))