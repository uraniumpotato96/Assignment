"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
"""

def evenDigitsOnly(n):
    return all(i%2 == 0 for i in [int(i) for i in str(n)])