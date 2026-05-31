class Solution:
    def maxArea(self, h: List[int]) -> int:
        # using 2 pointer
        # smaller bar = height of the well
        # bigger bar = width of the well
        left = 0
        right = len(h) - 1
        max_area = 0
        while left < right :
            curr_area = (min(h[left], h[right]) * (right - left))

            max_area = max(curr_area, max_area)

            if h[left] > h[right]:
                right -= 1
            else:
                left += 1
        return max_area



        