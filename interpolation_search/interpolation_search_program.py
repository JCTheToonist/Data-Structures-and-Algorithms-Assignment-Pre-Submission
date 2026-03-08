def interpolation_search(array, find, low, high, failedresults=[]):
    pos = int(low + ((find - array[low]) * (high - low) / (array[high] - array[low]))) # Calculates probe position
    foundvalue = array[pos] # Extracts value of the probe position to be compared

    ## Displays variables for the searching process so users can see what's happening ##
    print(f"Array: {[array[n] for n in range(low, high+1)]}") # Display array
    print(f"Lower bound: {low} / Higher bound: {high}\nLower bound item: {array[low]} / Higher bound item: {array[high]}") # Message to show calculated variables
    print(f"Position = {low} + ({find} - {array[low]}) * ({high} - {low}) / ({array[high]} - {array[low]})")
    print(f"Probe position: {pos}\nFound value: {foundvalue}\n")
    ####

    if foundvalue == find: # Returns if value is found successfully
        return f"Element found at index: {pos}"
    else:

     # If result is not equal, it is put in the failed results list
     if foundvalue in failedresults: # If it finds the same failed result again, it outputs an error to stop infinite loop
        return "Could not be found"
     else:
        failedresults.append(foundvalue) # Adds found value to failed results

     # Failed results cause array to be changed to sub-array
     if foundvalue < find: # foundvalue is lower than find
        return interpolation_search(array, find, pos+1, high, failedresults) # Higher sub-array
     if foundvalue > find: # foundvalue is higher than find
        return interpolation_search(array, find, low, pos-1, failedresults) # Lower sub-array

# Search array. Can be set to any array.
array = [1, 3, 7, 10, 14, 15, 16, 18, 20, 21, 22, 23, 25, 33, 35, 42, 45, 47, 50, 52]
print("Array:", array)
# Specifies which value to find within the array
# find = 0
find = int(input("Input the number you want to search for: "))

# Runs the function
print(interpolation_search(array, find, 0, len(array)-1))