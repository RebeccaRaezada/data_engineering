def bubble_sorting(arr):
    
    n=len(arr)
    
    for x in range(0, n-1):
        
        for y in range(x,n):
            
            if arr[y] > arr[x]:
                arr[x], arr[y]=arr[y],arr[x]
    return arr

arr=[1,4,0,3]
print(bubble_sorting(arr))
