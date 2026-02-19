class MinStack:
    def __init__(self):
        # Stack holds pairs: [element_value, current_min]
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            # If stack empty, min is val itself
            self.stack.append([val, val])
        else:
            # Current minimum is top element's min value
            current_min = self.stack[-1][1]
            # New minimum is smaller of val and current min
            new_min = min(current_min, val)
            self.stack.append([val, new_min])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None  # Or raise exception as per requirement
        # Return the value part of the top element
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None  # Or raise exception as per requirement
        # Return the min part of the top element
        return self.stack[-1][1]