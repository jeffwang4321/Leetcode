from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encode each string as "{length}#{string}"
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the index of the next '#'
            j = s.find("#", i)
            # Extract the length of the sub-string
            length = int(s[i:j])
            # Move the pointer to the start of the sub-string
            i = j + 1
            # Extract the sub-string using the length
            res.append(s[i : i + length])
            i += length

        return res


# python3 '.\297. Serialize and Deserialize Binary Tree.py'
if __name__ == "__main__":
    s = Solution()
    strs = ["hello", "world", "a#b", ""]
    print("input:", strs)

    t1 = s.encode(strs)
    print("encode:", t1)

    t2 = s.decode(t1)
    print("decode:", t2)
