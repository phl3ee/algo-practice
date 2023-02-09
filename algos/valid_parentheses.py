class Solution:
    def isValid(self, s: str) -> bool:

        #no-ops
        #if the str is not modulo 2 it's unbalanced, bomb out
        if len(s) % 2 != 0:
            return False

        #build a dict to map corresponding close characters
        closerMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        # Every open has to have a close
        # An open can be followed by another open,
        # but only the last open parsed can be closed
        checklist = []
        for i in s:
            if i in closerMap:
                if not checklist or (checklist[-1] != closerMap[i]):
                    return False
                else:
                    del checklist[-1]
            else:
                checklist.append(i)

        #Final check, checklist should be empty after parsing
        if not checklist:
            return True
        else:
            return False
