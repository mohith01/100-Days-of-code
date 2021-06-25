## Binary Search

Binary Search follows O(log<sub>2</sub>n)

```
low = 0 #lowest index
high = len(list)-1 #Last index
#Check the mid element
mid = (low+high) / 2 #Find the mid index
guess = list[mid]
# If guess is too low, you increase your low index
if guess < item
  low= mid + 1
# If guess is too high you reduce your high index
if guess> item
  high = mid-1
#Do this until you complete your loop or find the reqd element
```

