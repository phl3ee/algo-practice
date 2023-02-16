class Solution:
    def hammingWeight(self, n: int) -> int:
        """32 bit implementation
        """
        binary_string = bin(n)[2:]

        if len(binary_string) > 32:
            return 0

        binary_string = binary_string.replace("0","")
        return len(binary_string)
