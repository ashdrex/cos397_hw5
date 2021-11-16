# =========================================================================
#
#  Copyright COS 397
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

'''
This module sorts lists of integers...
Use bubble, quick, or insertion.
'''

'''
bubble sort
'''
def bubble(int_list):
  # don't use unnecessary processing power
  if len(int_list) == 1:
    return int_list

  # get the length of the list
  length = len(int_list)

  # traverse through all list elements
  for i in range(length-1):             # traverse the length
    for j in range(0, length-1-i):      # account for elements in place
      if int_list[j] > int_list[j+1]:
        # swap
        int temp = int_list[j]
        int_list[j] = int_list[j+1]
        int_list[j+1] = temp

'''
quick sort
'''
def partition(int_list, low, high):
  # begin with high end as pivot
  pivot = int_list[high]

  # pointer for high element
  i = low - 1

  # traverse through all list elements
  for j in range(low, high):
    if int_list[j] <= pivot:
      i = i + 1 # specify greater element

      #swap elements i and j
      (int_list[i], int_list[j]) = (int_list[i], int_list[j])
  # swap pivot element with greater element specified by i
  (int_list[i+1], int_list[high]) = (int_list[high], int_list[i+1])
  
  # return the position of where partition is done
  return i + 1


def quicksort(int_list, low, high):
  if(low < high):
    pi = partition(int_list, low, high)  # split indices in halves

    quicksort(int_list, low, pi-1)       # quicksort low end
    quicksort(int_list, pi+1, high)      # quicksort high end

def quick(int_list):
  # don't use unnecessary processing power
  if len(int_list) == 1:
    return int_list
  
  # get low and high values
  low = int_list[0]
  max_index = len(int_list)-1
  high = int_list[max_index]

  # call quicksort
  return quicksort(int_list, low, high)

'''
insertion sort
'''
def insertion(int_list):
  # don't use unnecessary processing power
  if len(int_list) == 1:
    return int_list

  # traverse through all list elements
  for i in range(0, len(int_list)-1):
    key = int_list[i]

    # move all of elements that are greater than key one position ahead
    j = i-1

    while j >= 0 and key < int_list:
      int_list[j+1] = int_list[j]
      j -= 1
    int_list[j+1] = key