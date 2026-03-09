# Interpolation Search
This Python program simulates Interpolation Search, a searching algorithm that approximates the closest position of a given value in an array, based on the low and high bounds of the array.

To set up the program, define the _array_ and _find_ variables:
* array: The array of values which the search will go through.
* find: The value which the array will search for. (Right now it's been set so you can input which value to search for.)

## Probe Position
The algorithm will find a probe position, a position in the array which is the most optimal for finding the location.

The formula for probe position:
```{low} + ({find} - {array[low]}) * ({high} - {low}) / ({array[high]} - {array[low]})```
- _find_ = The value being searched.
- _low_ = Low bound of the array, representing the minimum position searched.
- _high_ = High bound of the array, representing the maximum position searched.
- _array[low]_ = The item of the position _low_ in the array.
- _array[high]_ = The item of the position _high_ in the array.

## How it works
1. Set _low_ to 0 and _high_ to the length of the array - 1.
2. Find the probe position using the formula above.
3. Check if the item of the probe position matches the value being searched.
   - If it's equal, output the item's position. The search is now complete.
   - If it's lower than the searched value, search the higher sub-array [pos+1, high].
   - If it's higher than the searched value, search the lower sub-array [low, pos-1].
4. If the search isn't complete, it will call the function recursively to search again, this time searching the new sub-array instead.

###If the value can't be found
The program has a failsafe to detect if the searched value is not in the array. If triggered, it will output a message that the searched value cannot be found.
Whenever the probe doesn't match, the probe position's value will be included in a "failed predictions" list. While attempting to search for a value that is not present, the program will keep looping between two values trying to find a value that doesn't exist.
So if it loops to a value that has already been deemed not to count, it will trigger the failsafe. This is done to prevent the recursion from looping indefinitely.
