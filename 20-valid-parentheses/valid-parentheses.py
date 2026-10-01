class Solution:
    def isValid(self, s: str) -> bool:
        result=[]
        for i in s:
            if i=='[' or i=='{' or i=="(":
                result.append(i)
            else:
                if len(result)==0:
                    return False
                else:
                    top=result.pop()
                    if i==")" and top !='(':
                        return False
                    elif i=="]" and top !='[':
                        return False
                    elif i=='}' and top !='{':
                        return False
        return len(result)==0