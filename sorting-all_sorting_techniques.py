#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import random

def heapify(arr, n, parent_pos): # no aux space but unstable i.e relative order of elements changes in interim steps
    
    largest_val_loc = parent_pos # Initialize largest as root 
    
    left_child_loc= ( parent_pos*2 ) +1    # left = 2*i + 1 
    
    right_child_loc= ( parent_pos*2 ) +2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if left_child_loc < n and arr[left_child_loc] > arr[largest_val_loc]:
        largest_val_loc = left_child_loc
  
    # See if right child of root exists and is 
    # greater than root 
    if right_child_loc < n and arr[right_child_loc ] > arr[largest_val_loc]:
        largest_val_loc = right_child_loc
            
  
    # Change root, if needed 
    if largest_val_loc != parent_pos:
        
        arr[largest_val_loc], arr[parent_pos]=arr[parent_pos],arr[largest_val_loc] # swap        
        
        heapify( arr, n, largest_val_loc) # Heapify the root. 

  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    # Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range(n/2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for arr_len in range(n-1, 0, -1): 
        arr[arr_len], arr[0] = arr[0], arr[arr_len]   # swap 
        heapify(arr, arr_len, 0) 
        
    return arr

def quick_sort(arr,n): # no aux space but unstable i.e relative order of elements changes in interim steps 
    #WORST CASE is O(n^2) when array is sorted and we consider last element as pivot but AVERAGE CASE O(nLogn) is only considered for quick sort with Random Pivot)
    
    if len(arr) <= 1:
        return arr
    else:
        pivot= random.choice(arr)  #For Random choice 
        arr.remove(pivot)
        #pivot=arr.pop() # pivot=arr.pop / delete(len(arr)-1) for choosing last element as pivot
        #pivot=arr.pop(0) # or pivot = arr.delete(0) for choosing first element as pivot
    greater=[]
    lower=[]
    
    for item in arr:
        
        if item <= pivot:
            lower.append(item)
            
        else:
            greater.append(item)
            
    return quick_sort(lower, len(lower)) + [pivot] + quick_sort(greater, len(greater))

def mergeSort(values): # Aux space used but stable

    if len(values)>1:
        m = len(values)//2
        #left = values[:m]
        #right = values[m:]
        left = mergeSort(values[:m])
        right = mergeSort(values[m:])

        values =[]
        p1=p2=0

        while p1<len(left) and p2<len(right):
            if left[p1]<right[p2]:
                values.append(left[p1])
                p1=p1+1
            else:
                values.append(right[p2])
                p2=p2+1

        while p1 < len(left):
            values.append(left[p1])
            p1=p1+1
        while p2 < len(right):
            values.append(right[p2])
            p2=p2+1
            
    return values
  
def binarySearch(key,arr):
    beg=0
    end=len(arr)-1
    binary_search(key,arr,beg,end)
    
def binary_search (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) / 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


def insertionSort(values1):
    
    n = len(values1)
    
    if n <= 1:
        return values1
    
    for x in range(0,n):
        
        temp=values1[x]
        
        for y in range(x+1,n):
            print(x, values1[x], y, values1[y])
            
            if values1[y] < temp:
                values1[y-1]=values1[y]
           
                values1[y]=temp
                
    return values1


                

def sorting1(arr1):
    return arr1.sort()

        
def bubble_sort(arr):
    
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
        
            if arr[i] > arr[j]:
                arr[i],arr[j]  = arr[j],arr[i] 
                
    return arr


def check_if_array_is_sorted(arr):
    
    for x in range(1, len(arr)):
        if arr[x-1] > arr[x]:
            return "No"
        
        return "Yes"
