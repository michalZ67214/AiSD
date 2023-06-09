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


def ONP(string_):
    s = Stack()
    chars = string_.split(' ')
    for char in chars:
        if char.isnumeric():
            s.push(char)
        elif char == '+':
            n2 = s.pop()
            n1 = s.pop()
            s.push(float(n1)+float(n2))
        elif char == '-':
            n2 = s.pop()
            n1 = s.pop()
            s.push(float(n1)-float(n2))
        elif char == '*':
            n2 = s.pop()
            n1 = s.pop()
            s.push(float(n1)*float(n2))
        elif char == '/':
            n2 = s.pop()
            n1 = s.pop()
            if n2 == 0:
                return 'Błąd. Dzielenie przez 0'
            s.push(float(n1)/float(n2))
        elif char == '^':
            n2 = s.pop()
            n1 = s.pop()
            s.push(float(n1)**float(n2))
        elif char == '=':
            return s.pop()
        
    
print(ONP('2 2 + ='))
print(ONP('3 2 5 * + ='))
print(ONP('2 5 2 + * ='))
print(ONP('7 3 + 5 2 - 2 ^ * ='))
print(ONP('4 3 1 - 2 3 * ^ / ='))