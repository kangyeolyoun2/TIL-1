# 5장. Function
- 스택: 접시 쌓기, 마지막에 들어온 데이터가 가장 먼저 나가는 구조

## 1. 전역 변수와 지역 변수
- 전역변수(global variable): 전체 영역에서 접근할 수 있는 변수, 함수안에서도 접근가능
- 지역변수(local vairable): 특정 지역(함수 내부) 안에서만 접근할 수 있는 변수


- `global` 키워드를 사용하여 함수안에서 전역변수를 변경할 수 있다.
---
```python
g_var = 10 #1

def func():
    global g_var #2
    g_var = 20
    
if __name__ == "__main__":
    print("g_var : {} before".format(g_var)) #3
    func()
    print("g_var : {} after".format(g_var))
```
    `g_var : 10 before`
    `g_var : 20 after` #4

- 전역변수 #1 선언후, 
- 함수안에서 g_var값의 변경을 시도 #2
- 전역 변수가 함수 안에서 변경되었는지 출력하여 확인 #3
- 함수를 호출한 쪽에서 변경되었는지 확인 #4
---


## 2. nonlocal 키워드
- 내부함수에서 다른 함수를 정의할 때 쓰는방법

```python
def outer():  
    a = 2 #1
    b = 3
    
    def inner():
        nonlocal a #2
        a = 100 #3
    inner()
    
    print(
    "locals in outer : a = {}, b = {}".format(a, b))

if __name__ == "__main__":
    outer()
```

    'locals in outer : a = 100, b = 3
    
- #2에서 nonlocal 키워드로 inner() 함수 안에서 outer() 함수의 지역변수 a를 사용할것으로 선언


## 3. 인자 전달 방식에 따른 분류

### 3.1 값에 의한 전달(call by value) 
- 파이썬에서는 없는 개념

---
```c++
#include <iostream>
using namespace std;

void change_value(int x, int value) // #1
{
    x = value; // #2
    cout << "x : " << x << " in change_value" << endl;
    
}

int main(void)
{
    int x = 10;  // #3
    change_value(x, 20);  //#4
    cout << "x : " << x << " in main" << endl;
    
    return 0;
    
}

```
    `x : 20 in change_value`
    `x : 10 in main`
---



---
```c++
#include <iostream>
using namespace std;

int test(int a, int b);

int main(void)
{
    int a = 10, b = 5; // #4
    int res = test(a, b); // %5
    cout << "result of test: " << res << endl;
    return 0;
}

int test(int a, int b) // # 1
{
    int c = a + b; // #2
    int d = a - b; // #3
    return c + d;
}
```
---
- 결과 값은 다음 이미지와 함께보자
<img src="./img/5-2.png" width="40%">

- main()에 스택프레임을 먼저 쌓고, test() 스택 프레임이 쌓입니다.
- 각각의 스택 프레임은 독립된 공간이며, test() 실행후 사라지고 이후 남은 main() 실행



### 3.2 참조에 의한 전달(call by reference)


---
```c++
#include <iostream>
using namespace std;

void change_value(int *x, int value) //#1
{
    *x = value; //#2
    cout << "x : " << *x << " in change_value" << endl;
}

int main(void)
{
    int x = 10; // #3
    change_value(&x, 20); // #4
    cout << "x : " << x << " in main" << endl;
    return 0;
}
```
    `x : 20 in change_value`
    `x : 20 in main`
---

-  `int *`은 int형 포인터를 의미합니다 #1

- ` #4번 실행전`
<img src="./img/5-6.png" width="40%">

- ` #4번 실행 후`
<img src="./img/5-7.png" width="40%">


### 3.3 객체 참조에 의한 전달(Python)

#### Code 1

---
```python
def func(li):
    li[0] = 'I am your father!'

if __name__ == "__main__":
    li = [1, 2, 3, 4]
    func(li)
    print(li)
```
    ['I am your father!', 2, 3, 4]
---

#### Code 2

---
```python
def func(li):
    li = ['I am your father!', 2, 3, 4] #2
    
if __name__ == "__main__":
    li = [1, 2, 3, 4]
    func(li)
```
    [1, 2, 3, 4]
---

- Code 1: 참조한 리스트에 접근해 변경을 시도
<img src="./img/5-3-3-1.jpeg" width="60%">

- Code 2: 아예 다른 리스트를 메모리 공간에 새로 만든 다음 이를 참조해 리스트를 변경
<img src="./img/5-3-3-2.jpeg" width="60%">


### 3.4 변경 불가능 객체는 함수 인자로 전달해 변경할 수 없을까?
- 아래 방법과 같이 return으로 객체를 전달해 주는 방식으로 해결!

---
```python
def change_value(tu):
    tu = ('I am your father!', 2, 3, 4)
    return tu

if __name__ == "__main__":
    tu = (1, 2, 3, 4)
    tu = change_value(tu)
    print(tu)
```
    ('I am your father!', 2, 3, 4)
---

## 4. 람다 함수
- 이름이 없는 함수, 다음 행으로 넘어가면 다시 사용 불가

---
```python
li = [i for i in range(1, 11)]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li.sort(key = lambda x: x % 2 ==0)

li
```
	[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
---

-  람다 함수에는 return값이 없기 때문에, 반드시 식이 들어가야 합니다.

