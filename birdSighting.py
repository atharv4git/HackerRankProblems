import math
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    scount=0
    typearr=[[]*2 , []*len(arr)]
    types = []*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j and arr[i]==arr[j]:
                types.append(arr[i])
                print("append complete "+str(i))
                break
            var1 = types[i]
            var2 = types[j]
            if i!=j and var1==var2:
                scount+=1
                break
            if scount>1:
                typearr[0].append(types[i])
                typearr[1].append(scount)
                scount=0
                print("appending in typearr complete "+str(i))
                break

            
    print(types)
    print(typearr)        
                        
if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(str(result) + '\n')