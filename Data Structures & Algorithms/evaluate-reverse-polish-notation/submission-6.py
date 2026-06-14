class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_dict = {'+', '-', '/', '%', '*'}
        for curr_token in tokens:
            if curr_token not in operator_dict:
                # if current token is not operator meaning its number
                # convert string to int and append to stack
                stack.append(int(curr_token))

            else:
                b = stack.pop()
                a = stack.pop()

                if curr_token == "+":
                    stack.append(a+b)
                elif curr_token == "-":
                    stack.append(a-b)
                elif curr_token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0]