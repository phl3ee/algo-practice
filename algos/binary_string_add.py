class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """Adding two "Binary Strings"
        No usage of bin() and other faster options
        """
        output = ""

        #pad the inputs so we can do long addition
        padding = len(a) - len(b)
        if padding > 0:
            b = "0" * padding + b
        else:
            a = "0" * (padding * - 1 ) + a

        carry = "0"
        for i in range(1, len(a) + 1):
            #print(a[-i] , b[-i], carry)
            if a[-i] == "1" and b[-i] == "1":
                if carry == "1":
                    output = "1" + output
                else:
                    output = "0" + output
                    carry = "1"
            if a[-i] == "0" and b[-i] == "0":
                if carry == "1":
                    output = "1" + output
                    carry = "0"
                else:
                    output = "0" + output
            # dirty string style XOR
            if a[-i] != b[-i]:
                if carry == "1":
                    output = "0" + output
                    carry = "1"
                else:
                    output = "1" + output

            #print(output, carry)

        if carry == "1":
            return "1" + output

        return output
