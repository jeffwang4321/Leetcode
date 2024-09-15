# def StringChallenge(s):
#     # We keep reducing the string until no further replacements are possible
#     while True:
#         reduced = False
#         i = 0
#         while i < len(s) - 1:
#             # Check adjacent pairs and apply the replacement rules
#             pair = s[i : i + 2]
#             if pair in ["ab", "ba"]:
#                 s = s[:i] + "c" + s[i + 2 :]
#                 reduced = True
#             elif pair in ["bc", "cb"]:
#                 s = s[:i] + "a" + s[i + 2 :]
#                 reduced = True
#             elif pair in ["ca", "ac"]:
#                 s = s[:i] + "b" + s[i + 2 :]
#                 reduced = True
#             else:
#                 i += 1
#         # If no reduction happened in this pass, we're done
#         if not reduced:
#             break
#     return len(s)


def StringChallenge(s):
    """
    This function takes a string s as input and returns the length of the string after applying the following rules:
    - If the string contains "ab" or "ba", replace it with "c"
    - If the string contains "bc" or "cb", replace it with "a"
    - If the string contains "ca" or "ac", replace it with "b"
    The function keeps applying these rules until no further replacements are possible.
    """
    string_map = {"ab": "c", "ba": "c", "bc": "a", "cb": "a", "ca": "b", "ac": "b"}

    while True:
        old_string = s
        for pair, char in string_map.items():
            ## Below if statement is not needed since replace() will not change the string if the substring is not found
            # if pair in s:
            s = s.replace(pair, char)

        if s == old_string:  # If no replacements were made, we're done
            break
    return len(s)


# Example usage:
print(StringChallenge("cab"))  # Output: 2
print(StringChallenge("bcab"))  # Output: 1
print(StringChallenge("cbbabcab"))  # Output: 2
