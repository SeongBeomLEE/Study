# CHATER4 이터레이터와 제너레이터
## 이터레이터와 제너레이터
- object iteration은 파이썬의 강력한 기능 중 하나로, 순환을 단순히 시퀀스 내부 아이템에 접근하는 방법으로 생각할 수도 있지만, 순환을 통해서 순환 객체 만들기, itertools 모듈의 순환 패턴 적용하기, generator 함수 만들기 등을 할 수 있음
- Iterator는 __iter__와 __next__를 method로 가지는 class임
- Generator는 yield 문을 사용하는 function임
- 제너레이터 내에서 "yield" 문으로 제너레이터를 반환하고 싶으면, "yield from" 을 사용하면 됨(yield from을 사용안하면, 그냥 제너레이터를 반환함)
```python
class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []
    
    def __repr__(self) -> str:
        return "Node{!r}".format(self._value)
    
    def add_child(self, node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    
if __name__ == "__main__":
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
```
## 119p~