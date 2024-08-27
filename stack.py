# # List can be used as Stack(LIFO)
# # Recommended approach to use stack and queques are using collections.deque(uses linked list internally) rather than using list/ dynamic array
# from collections import deque
# # stack = deque()
# # print(dir(stack))

# # stack.append('link 1')
# # stack.append('link 2')
# # stack.append('link 3')
# # stack.append('link 4')
# # stack.append('link 5')
# # stack.append('link 6')

# # print(stack)
# # print(stack.pop())
# # print(stack)

# class Stack:
#     def __init__(self):
#         self.container = deque()
#     def push(self,val):
#         self.container.append(val)
#     def pop(self):
#         return self.container.pop()
#     def peek(self):
#         return self.container[-1]
#     def isEmpty(self):
#         return len(self.container)==0
#     def size(self):
#         return len(self.container)  

# def isBalanced(s):
#     match_dict = {
#         ')':'(',
#         ']':'[',
#         '}':'{'
#     }
#     stack = []

#     for ch in s:
#         if ch == '(' or ch == '{' or ch == '[':
#             stack.append(ch)
#         else:
#             if stack and stack[-1] == match_dict[ch]:
#                 stack.pop()
#             else:
#                 return False
        
#     return len(stack)==0


         
# def reverseString(s):
#     stack = Stack()

#     for ch in s:
#         stack.push(ch)
    
#     reverse_string = ''

#     while stack.size()!=0:
#         reverse_string += stack.pop() 
#     return reverse_string

# if __name__ == '__main__':
#     print(reverseString('Ello governurr'))

