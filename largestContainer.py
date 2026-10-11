'''
given an array of ints on a graph.  the number acts as a container.  with these numbers return the largest volumn of liquid that can be returned
 j - 1 represents the width of the container
 
sum = min(height(i), height[j]) * (j-i)
'''

def largest_volum(heights: list[int]) -> int:
    max_water = 0
    left, right = 0, len(heights) - 1
    while (left < right):
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(max_water, water)
        if (left < right):
            left += 1
        if (left > right):
            right -= 1
        else:
            left += 1
            right -= 1
    return max_water

assert largest_volum([]) == 0
assert largest_volum([1]) == 0
assert largest_volum([0, 1, 0]) == 0
assert largest_volum([3, 3, 3, 3]) == 9
assert largest_volum([1, 2, 3]) == 2
assert largest_volum([3, 2, 1]) == 2