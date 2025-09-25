stack = ["QuizA", "QuizB", "QuizC"]
stack.pop()  # Undo one
top = stack[-1]
print("Top after undo:", top)  # Output: QuizB
stack = ["Upload", "Fill Form", "Confirm"]
stack.pop()  # Undo Confirm
stack.pop()  # Undo Fill Form
remaining = stack[-1]
print("Remaining after undo:", remaining)  # Output: Upload
stack = ["X", "Y", "Z"]
stack.pop()  # Removes Z
stack.pop()  # Removes Y
stack.append("W")
top = stack[-1]
print("Top after operations:", top)  # Output: W
queue = list(range(1, 13))  # Clients 1 to 12
for _ in range(7):
    queue.pop(0)  # Serve one
front = queue[0]
print("Client now in front:", front)  # Output: 8
queue = ["P1", "P2", "P3", "P4", "P5", "P6"]
last_served = queue[-1]
print("Last served patient:", last_served)  # Output: P6

