def solution(n):
  dic = {1:0}
  n = int(n)
  def recur(n):
    if n in dic:
      return dic[n]
    if n % 2 == 0:
      count = 0
      temp = n
      while temp % 2 == 0:
        temp = temp//2
        count += 1
      dic[n] = count + recur(temp)
      current = temp
      for i in range(1, count+1):
          current *= 2
          dic[current] = dic[temp] + i 
      return dic[n]
    else:
      dic[n] = 2 + min(recur((n-1)//2), recur((n+1)//2))
      return dic[n]
  ans = recur(n)
  return ans

print(solution('123456789'))