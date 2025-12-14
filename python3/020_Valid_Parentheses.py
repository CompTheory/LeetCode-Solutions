class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")" : "(", "}" : "{", "]" : "["}
        stack = []

        for var in s:
            if var not in hashmap:
                stack.append(var)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != hashmap[var]:
                    return False
        return not stack