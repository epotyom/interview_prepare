def sort(data):
  """
  Quicksort function

  Arguments:
    data(list): list of numbers to sort
  """
  sortIteration(data, 0, len(data)-1)
  
def sortIteration(data, first, last):
  """
  Iteration of quicksort

  Arguments:
    data(list): list to be sorted
    first(int): first element of iteration
    last(int): last element of iteration
  """
  if first < last:
    divpoint = divide_and_conquer(data, first, last)
  
    sortIteration(data, first, divpoint-1)
    sortIteration(data, divpoint+1, last)

def divide_and_conquer(data, first, last):
  divpoint = first # select divpoint, any method 
  left_mark = first + 1
  right_mark = last
  done = False
  while not done:
    while left_mark <= right_mark and data[left_mark] < data[divpoint]:
      left_mark += 1
  
    while right_mark >= left_mark and data[right_mark] > data[divpoint]:
      right_mark -= 1
  
    if left_mark > right_mark:
      done = True
    else:
      tmp = data[left_mark]
      data[left_mark] = data[right_mark]
      data[right_mark] = tmp
  
  tmp = data[divpoint]
  data[divpoint] = data[right_mark]
  data[right_mark] = tmp

  return right_mark
      
  
  
