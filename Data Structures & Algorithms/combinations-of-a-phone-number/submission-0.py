class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        result = []
        path = []

        # dictonary for phone digit with letters
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        # index to iteate over digits = 34 , index= 0 == 3, index= 1 ==4
        def dfs_phone(index):
            # base case 1
            if index == len(digits):
                result.append("".join(path))
                return 

            letters = phone[digits[index]]
            for letter in letters:
                path.append(letter)
                dfs_phone(index+1)
                path.pop()

        dfs_phone(0)
        return result




        