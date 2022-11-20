class Solution:
  def isMatch(self, s: str, p: str) -> bool:
      
    # DFS no Memoization 
    # def dfs(i, j):
    #   if i >= len(s) and j >= len(p):
    #     return True
    #   if j >= len(p):
    #     return False
    
    #   match = i < len(s) and (s[i] == p[j] or p[j] == ".")
    
    #   if (j + 1) < len(p) and p[j + 1] == "*":
    #     return dfs(i, j + 2) or (match and dfs(i + 1, j)) # dont use * or use *
          
    
    #   if match:
    #     return dfs(i + 1, j + 1)
    
    #   return False     
      
    # Top-Down Memoization       
    cache = {}
    def dfs(i, j):
      if (i, j) in cache:
        return cache[(i, j)]
      
      if i >= len(s) and j >= len(p):
        return True
      if j >= len(p):
        return False
      
      match = i < len(s) and (s[i] == p[j] or p[j] == ".")
      
      if (j + 1) < len(p) and p[j + 1] == "*":
        cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j)) # dont use * or use *
        return cache[(i, j)]
      
      if match:
        cache[(i, j)] = dfs(i + 1, j + 1)
        return cache[(i, j)]
      
      cache[(i, j)] = False
      return False
    
    return dfs(0, 0)


# python3 '.\10. Regular Expression Matching.py'
if __name__ == "__main__":
  s = Solution()

  # Test Cases
  t1 = s.isMatch("aa", "a")
  t2 = s.isMatch("aa", "a*")
  t3 = s.isMatch("ab", ".*")

  # Output
  print(t1)
  print(t2)
  print(t3)

  # Expected
  assert t1 == False
  assert t2 == True
  assert t3 == True
