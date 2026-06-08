class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        window_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        for i in range(len(s1)):
            window_map[s2[i]] = window_map.get(s2[i], 0)+ 1
        
        if s1_map == window_map:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            window_map[s2[left]] -= 1
            
            if window_map[s2[left]] == 0 :
                del window_map[s2[left]]

            window_map[s2[right]] = window_map.get(s2[right],0) + 1
            left += 1
            if window_map == s1_map:
                return True
        return False




