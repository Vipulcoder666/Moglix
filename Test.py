# Write a program: Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
# Example 1:Input: s = "(()"Output: 2Explanation: The longest valid parentheses substring is "()".
# Example 2:Input: s = ")()())"Output: 4Explanation: The longest valid parentheses substring is "()()".
# Example 3:Input: s = ""Output: 0
# Constraints:
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

def longest_valid_parentheses(s):
    stack = [-1]
    ans = 0

    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])

    return ans


s = input("Enter parenthesess string: ")
print("Longest valid parentheses length:", longest_valid_parentheses(s))