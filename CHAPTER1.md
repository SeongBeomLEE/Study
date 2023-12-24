# CHAPTER1 자료 구조와 알고리즘
## unpacking
- 파이썬의 언패킹은 튜플이나 리스트 뿐만 아니라 순환 가능한 모든 객체에 적용할 수 있음(문자열, 파일, iterator, generator 등)
- 길이를 알 수 없는 객체를 언패킹할 때는 *를 사용할 수 있음
    -  ```a, *b, c = [i for i in range(n)]```
## OrderedDict
- 삽입 순서에 맞춰 dict 구조를 사용하고 싶으면, OrderedDict를 사용할 수 있음
- OrderedDict는 내부적으로 doubly linked list로 삽입 순서와 관련 키를 기억함
- 새로운 아이템을 처음으로 삽입하면 리스트이 제일 끝에 위치시켜서, 기존 키에 재할당을 한다 해도 순서에는 변화가 생기지 않음
- 그런데 doubly linked list를 사용하기 때문에, OrderedDict의 크기는 일반적인 dict에 비해서 두배로 큼
## 두 딕셔너리의 유사점 찾기
- dict 내의 keys() 메소드는 key를 보여주는 key-view 객체를 반환하며, key-view 객체는 집합 연산을 수행할 수 있음
- dict 내의 items() 메소드는 key,value 쌍을 보여주는 item-view 객체를 반환하며, item-view 객체는 집합 연산을 수행할 수 있음
- dict 내의 values() 메소드는 value를 보여주는 value-view 객체를 반환하며, value-view 객체는 집합 연산을 수행할 수 없음