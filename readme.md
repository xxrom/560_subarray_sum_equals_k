# Clear explanation URL:
# https://medium.com/@edward.zhou/leet-code-560-subarray-sum-equals-k-explained-python3-solution-31ab6262615e

1,1,1   =  2
1,1
1,1

1,1,1,2 = 3
1,1,1
1,2


1,1,1,1,1,1,1,1 = 5
1,1,1,1,1
  1,1,1,1,1
    1,1,1,1,1
      1,1,1,1,1


1,1,1,1,1,2,2,2,2 = 5
1,1,1,1,1 +++
  1,1,1,1,2 ---
    1,1,1,2 +++ if a[i+1] < b[j+1] => i++ (diff = a[j+1] - a[i+1])
      diff = 2-1 = 1 => diff > 0 => i++ => diff -= a[i]
      if diff == 0 => ansCounter += 1
      if diff <= 0 => check next j => j++

      1,1,2,2 --- if a[i] < b[j] => index ++
      i     j
        1,2,2 ++
          2,2,2 --
           ---


k = 100
[28,54,7,-70,22,65,-6]
28 + 54











        0 1 2 3 4  5 6 7
nums = [2,2,3,0,4,-1,1,6], k = 7

2,2,3 = 7 - {0-2: 7}

2,2,3,0,4,-1 ...
