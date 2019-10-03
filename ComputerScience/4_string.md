# 4장. 문자와 문자열
## 1. 문자 인코딩
- `문자 인코딩(character encoding)`은 문자 집합을 메모리에 저장하거나 통신하는데 사용하기 위해 부호화하는 방식
- `문자 집합(character set)`은 문자(character)를 모아 둔 것
- 0과 1밖에 모르는 컴퓨터에 문자를 인식시키기 위해서는 문자 하나에 정수 하나를 매핑해두어야 한다. 이렇게 매핑된 정수를 `코드 포인트(code point)`라고 한다.
- 문자와 문자에 매핑된 코드 포인트를 모아놓은 집합을 `부호화된 문자 집합(Coded Character Set, CCS)`이라고 한다.

## 2. 아스키
- 아스키: `American Standard Code for Information Interchange`, 미국정보교환표준부호
- 비트 7개로 문자를 표현하는 문자 인코딩 방식

|코드 포인트(16진수)|코드 포인트(10진수)|매핑된 문자|
|---|---|---|
|0x30|48|'0'|
|0x41|65|'A'|
|0x61|97|'a'|

- 예시 코드

---
```python
ch = 'A'
bch = ch.encode()
bch, bch[0]
```
    b'A', 65
---

- 32비트 컴퓨터에서 `int`형은 일반적으로 4바이트인데, ASCII는 7비트면 충분.
- 문자를 표현하기 위해 `char`형이라는 새로운 정수 자료형을 개발

## 3. 유니코드
- 언어의 확장을 위해 도입된 인코딩 방식
- 7비트일 때는 128개 문자를 표현할 수 있지만, 16비트로 확장하면 65,536개의 문자를 표현할 수 있다.
- UTF-8, UTF-16, UTF-32 방식 등이 있다.

#### 1) UTF-8(Universal Coded Character Set Transformation Format-8 bit)
- 가변길이 인코딩 방식
- 코드 유닛의 크기는 8비트

|유니코드 코드 포인트|메모리 크기|비고|
|---|---|---|
|U+0000 ~ U+007F|1 Byte||
|U+0080 ~ U+07FF|2 Byte||
|U+0800 ~ U+7FFF|3 Byte|한글 표현|
|나머지|4 Byte||

#### 2) UTF-16
- 2바이트 단위로 문자를 표현
- 코드 유닛의 크기는 16비트

|유니코드|메모리 크기|비고|
|---|---|---|
|기본 다국어 평면|2 Byte|한글 표현|
|나머지|4 Byte||

#### 3) UTF-32
- 모든 문자를 4바이트 단위로 문자를 표현
- 코드 유닛의 크기는 32비트

#### 변환 코드 예시

---
```python
ch = '가'
ch.encode, ch.encode('UTF-8'), ch.encode('UTF-16'), ch.encode('UTF-32')
```
    b'\xea\xb0\x80', b'\xea\xb0\x80', b'\xff\xfe\x00\xac', b'\xff\xfe\x00\x00\x00\xac\x00\x00' 
---

## 4. 파이썬 문자열의 특징
- `C/C++`에서는 문자열을 변수로 만들면 요소인 문자를 변경할 수 있고, 문자열을 상수로 만들면 요소를 변경할 수 없다.
-  파이썬의 문자열은 요소를 변경할 수 없습니다.

---
```python
string = 'abcde'
string[2] = 'a'
```
    Traceback (most recent call last):
        File "<pyshell#3>", line 1, in <module>
            string[2] = 'a'
    TypeError: 'str' object does not support item assignment
---

- 내장함수 중 하나인 `replace()` 함수를 사용하면 바뀐 문자열을 반환하지만, 요소를 직접 변경한 것은 아니다!

---
```python
string = 'abcde'
new_string = string.replace('c', 'x')
new_string, string
```
    'abxde', 'abcde'
---

