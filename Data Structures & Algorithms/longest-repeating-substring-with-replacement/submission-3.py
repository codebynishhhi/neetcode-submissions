class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        left = 0
        result = 0

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right], 0) + 1

            max_freq = max(hmap.values())
            window_size = right - left + 1
            # string is invalid only when the number of replacements is > k
            # no. of replacements = window_size - max_frq
            # num_replacements = window_size - max_freq

            while window_size - max_freq > k :
                hmap[s[left]] -= 1
                left += 1

                # recalculate window size & max frequency
                window_size = right - left + 1
                max_freq = max(hmap.values())


            result = max(result, window_size)
        return result


