class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:

            current = chars[read]
            count = 0

            # Count repeated characters
            while read < n and chars[read] == current:
                count += 1
                read += 1

            # Write character
            chars[write] = current
            write += 1

            # Write count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write