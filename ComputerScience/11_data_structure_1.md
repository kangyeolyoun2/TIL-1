
## 1. 자료 구조 
- 자료 구조란 데이터를 효율적으로 검색, 변경, 삭제할 수 있도록 저장하거나 관리하는 방법을 말함. 
- 자료 구조에서 이해해야 할 세가지 
    - 데이터를 어떻게 `삽입`하는가?
    - 데이터를 어떻게 `검색`하는가?
    - 데이터를 어떻게 `삭제`하는가?
 
- 자료 구조 종류
    - 연결 리스트
    - 스택
    - 큐
    - 트리
- `상황에 따라 적절한 자료 구조가 달라질 수 있음.`

## 2. 추상자료형 (ADT, Abstract Data Type)
- `자료 구조에서 삽입, 탐색, 삭제 등을 담당하는 함수들의 사용 설명서`.
- 추상 자료형은 인터페이스(함수의 이름, 인자, 반환형 등을 명시한 것)와 구현을 분리. 
- `추상화 한다` = 함수가 어떻게 구현되었는 지 몰라도 함수를 이용할 수 있음. 

### 1.1 배열(array)
- 가장 기본적인 자료구조로, `같은 자료형을 가진 변수의 모임`.
- 메모리에 순서대로 할당되므로 캐시히트가 일어날 확률이 높으며, 인덱스를 통해 변수에 매우 빠르게 접근할 수 있음. 
- `새로운 데이터의 삽입이 없다면 배열을 쓰는 것이 가장 합리적.`

### 1.2 연결 리스트 (Linked List)
- `데이터와 참조로 구성된 노드`가 한 방향 혹은 양방향으로 쭉 이어져 있는 자료 구조. 
    - 단일 연결 리스트 : 노드가 한 방향만 참조
    - 이중 연결 리스트 
        - 다음 노드를 가리키는 참조와 이전 노드를 가리키는 참조. 
        - `힙 세그먼트를 구현하는 큰 틀을 제공.`
- 노드
    - 자료 구조를 구현할 때 `데이터를 담는 틀`로, 저장할 데이터와 다음 노드를 가리키는 참조로 이루어짐. 

**노드 구현 코드**


```python
class Node:
    def __init__(self, data = None):
        self.__data = data  # 데이터 부분
        self.__next = None # 참조 부분 
        
        # 은닉기능을 쓰는 이유 : 데이터에 수정할 때 발생하는 오류를 최소화하기 위해. 
    
    def __del__(self):
        print("data of {} is deleted".format(self.data))
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
        
    # setter는 인자가 하나 더 필요.
    # getter를 정의해야 setter메서드 이용가능.
        
    @property 
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, n):
        self.__next = n 
```

**연결리스트 구현 코드**
- 멤버 
    - head : 연결 리스트의 첫 번째 데이터
    - tail : 연결 리스트의 마지막 데이터
    - d_size : 리스트에 저장된 데이터의 개수 
    <img src="./TIL/ComputerScience/imgs/11-1.jpeg" width="60%">
- ADT
    - append 
        - 데이터를 삽입하는 함수
        - 반환형 : None
    - search_target 
        - 데이터를 순회하면서 대상 데이터를 찾아 그 위치와 함께 반환.
        - 연결리스트는 순회할 때 매번 처음부터 순서대로 순회해야 함.
        - 반환형 : (data, pos)
    - search_pos 
        - 인자로 위치를 전달하면 연결리스트에서 해당 위치에 있는 데이터를 반환.
        - 연결리스트는 순회할 때 매번 처음부터 순서대로 순회해야 함.
        - 반환형 : data 
    - remove
        - 데이터를 삭제하는 함수
        - 반환형 : None
    - empty
        - 연결리스트가 비어있다면 참, 비어있지 않다면 거짓을 반환
    - size 
        - 연결리스트의 데이터 개수를 반환


```python
class Linked_list:
    
    def __init__(self,):
        self.head = None
        self.tail = None
        self.d_size = 0
        
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
    
    def size(self):
        return self.d_size
    
    def append(self, data):
        
        new_node = Node(data)
        
        # 연결리스트가 비어있을 경우
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
        
        # 데이터가 하나 이상 있을 때 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.d_size += 1
            
    def search_target(self, target, start = 0):
        
        if empty():
            return None
        pos = 0
        cur = self.head  # cur를 head에 위치시킴으로써 순회를 시작. 
        
        if pos >= start and target == cur.data:
            return cur.data, pos
        
        while cur.next: # cur.next가 None값을 가리키면 순회를 멈춤!
            pos +=1
            cur = cur.next
            if pos >= start and target == cur.data:
                return cur.data, pos
        
        return None, None
    
    def search_pos(self, pos):
        
        # pos가 범위를 벗어나는 경우 
        if pos > self.size() - 1:
            return None
        
        cnt = 0
        cur = self.head
        if cnt == pos:
            return cur.data
        
        while cnt < pos:  # cnt가 pos와 같아지면 while문을 빠져나와 cur 데이터를 반환 
            cur = cur.next
            cnt += 1 
            
        return cur.data 
    
    def remove(self, target):
        if self.empty():
            return None
        
        bef = self.head
        cur = self.head
        
        # 삭제노드가 첫 번째 노드일 때 
        if target == cur.data:
            # 데이터가 하나일 때
            if self.size() == 1:
                self.head = None
                self.taile = None
            # 데이터가 두 개 이상일 때
            else:
                self.head = self.head.next #head를 다음 노드로 옮김. 
            self.d_size -= 1 
            return cur.data 
            
            # 삭제 노드가 첫 번째 노드가 아닐 때
            while cur.next:
                bef = cur
                cur = cur.next
                if target == cur.data:
                    # 삭제 노드가 마지막 노드일 때
                    if cur == self.tail:
                        self.tail = bef
                    # 일반적인 경우 
                    else:
                        bef.next = cur.next
                        self.d_size -= 1 
                        return cur.data
                
                return None
```

<img src="./TIL/ComputerScience/imgs/111-2.jpeg" width="60%">
<img src="./TIL/ComputerScience/imgs/11-3.jpeg" width="60%">
<img src="./TIL/ComputerScience/imgs/11-4.jpeg" width="60%">
<img src="./TIL/ComputerScience/imgs/11-5.jpeg" width="60%">
<img src="./TIL/ComputerScience/imgs/11-6.jpeg" width="60%">

### 1.3 스택 (Stack)
- 데이터를 차곡차곡 쌓아 올린 모습
- 접시 쌓기
- LIFO (last in first out)

**스택의 ADT**
- push
    - 데이터를 스택의 맨 위에 추가합니다
    - 반환형 : None
- pop
    - 스택의 맨 위의 데이터를 삭제하면서 반환
- empty
    - 스택이 비어있으면 참, 비어 있지 않다면 거짓 반환
- peek 
    - 스택의 맨 위에 있는 데이터를 반환하되 삭제하지 않음. 


```python
class Stack:
    
    def __init__(self):
        self.container = list()
        
    def push(self, data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()
    
    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def peek(self):
        return self.container[-1]
```

### 1.4 큐 (Queue)
- 줄서기
- FIFO(first in first out)

**큐의 ADT**
- enqueue
    - 큐의 마지막에 데이터를 추가
    - 반환형 : None
- dequeue 
    - 큐에서 가장 먼저 들어온 데이터를 삭제하면서 반환
- empty
    - 큐가 비어있으면 참, 비어있지 않으면 거짓을 반환 
- peek 
    - 큐에서 가장 먼저 들어온 데이터를 반환하되 삭제하지는 않음


```python
class Queue:
    
    def __init__(self):
        self.container = list()
        
    def enque(self, data):
        self.container.append(data)
        
    def deque(self):
        return self.container.pop(0)
    
    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def peek(self):
        return self.container[0]
```
