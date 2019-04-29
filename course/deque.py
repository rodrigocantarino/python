"""

Deque - list-like container with fast appends and pops on either end.
It's a high performance "list".

"""

from collections import deque

deq = deque('Rodrigo')

print(deq)

# Add elements
deq.append('P')  # Add a new element at the end of the deque

print(deq)

deq.appendleft('Sir')  # Add a new element at the begin of the deque

print(deq)

# Remove elements

deq.pop()  # Remove and return the last element

print(deq)

deq.popleft()  # Remove and return the first element

print(deq)


