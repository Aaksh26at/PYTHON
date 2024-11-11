def insertion_Sort(arr):
  n = len(arr)
  for current in range(1,n):
    # value in arr
    currentCard = arr[current] # 4    
    
    #it will run the loop from current-1 to 0
    correctPosition = current -1   # 1

    while (correctPosition >= 0):
      if arr[correctPosition] < currentCard:
        break 
      else:
        arr[correctPosition+1] = arr[correctPosition]
      correctPosition -= 1
    
    arr[correctPosition+1] = currentCard

  return arr


l1 = [9,1,4,2,5,0,6]
result = insertion_Sort(l1)
print(result)