# 队列与栈两种数据结构的区别和Python实现
from collections import deque
# 栈的实现
stack = []

# 入栈
stack.append(1)  
print(stack)
stack.append(2) 
print(stack)
stack.append(3) 
print(stack)
stack.append(4) 
print(stack)
print('*'*100)

# 出栈
n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
n = stack.pop()
print(stack, n)
print('*'*100)


# 队列的实现
queue = deque()

# 入队列
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(4)
print(queue)
print('*'*100)

# 出队列
queue.popleft()
print(queue, n)
queue.popleft()
print(queue, n)
queue.popleft()
print(queue, n)
queue.popleft()
print(queue, n)