class Solution:
  def convert(self, s: str, numRows: int) -> str:
    '''
    P   A   H   N
    A P L S I I G
    Y   I   R
    
    -> PAHNAPLSIIGYIR
    
    Approach 1
    0 [PAHN]
    1 [APLSIIG]
    2 [YIR]
    '''
        
    if numRows == 1 or numRows >= len(s):
        return s
    
    delta = -1
    row = 0
    res = [[] for i in range(numRows)]
    
    # iterate thought string
    for c in s:
      res[row].append(c)
      
      if row == 0 or row == numRows -1:
          delta *= -1
      row += delta
    
    for i in range(len(res)):
        res[i] = ''.join(res[i])
    return ''.join(res)


    # if numRows == 1 or numRows >= len(s):
    #   return s
    
    # cycle = 2 * numRows - 2
    # res = []
    # for i in range(numRows):
    #   for j in range(i, len(s), cycle):
    #     res.append(s[j])
    #     k = j + cycle - 2 * i
    #     if i != 0 and i != numRows -1 and k < len(s):
    #       res.append(s[k])
              
    # return "".join(res)



# python3 '.\6. Zigzag Conversion.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.convert("PAYPALISHIRING", 3)
  t2 = s.convert("PAYPALISHIRING", 4)
  t3 = s.convert("A", 1)

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == "PAHNAPLSIIGYIR"
  assert t2 == "PINALSIGYAHRPI"
  assert t3 == "A"
