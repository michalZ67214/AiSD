class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items)



def parChecker(symbolString):
    s = Stack()
    index = 0
    error = True
    while index < len(symbolString) and error:
        symbol = symbolString[index]
        if symbol in ('(','{','['): s.push(symbol)
        else: 
            if s.isEmpty(): error=False
            else: 
                symbol_taken = s.pop()
                if symbol == '(' and symbol_taken == ')':
                    error = False
                elif symbol == '{' and symbol_taken == '}':
                    error = False
                elif symbol == '[' and symbol_taken == ']':
                    error = False
                else:
                    error = True
        index += 1
        
    if error and s.isEmpty(): return True
    else: return False
        
    
    
# dobrze
print(parChecker('(()()()())'))
print(parChecker('(((())))'))
print(parChecker('(()((())()))'))
print(parChecker('[(){}()()]'))
print(parChecker('{()[(())()]}'))

# źle
print(parChecker('((((((())'))
print(parChecker('()))'))
print(parChecker('(()()(()'))