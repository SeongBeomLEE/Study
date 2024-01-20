# practical-python
[practical-python](https://github.com/dabeaz-course/practical-python) 공부 기록

## 또 읽으면 좋은 내용
- [07_Objects](https://github.com/dabeaz-course/practical-python/blob/master/Notes/02_Working_with_data/07_Objects.md)
  - python에서 assignment operations 들은 절대 복사본을 만들지 않는다.
  - python에서 assignment operations 들은 단지 reference copy를 할 뿐이다. (pointer copy)
  - 따라서 리스트 안에 리스트를 넣고, 리스트 안에 있는 리스트의 값의 변화를 주면, 리스트안에 있는 리스트가 저장되어 있는 메모리의 값 자체가 변화한 것이기 때문에 해당 메모리를 잡고 있는 모든 값들이 변화하는 것이다. (이 내용을 유추해보면 리스트는 내부에 메모리 위치를 저장한다고 볼 수 있음)
  - 그런데 Variables은 memory locations을 의미하는 것이 이니라 name을 의미한다.
  - 따라서 a 라는 Variables에 새로운 값을 넣더라도, 기존에 a가 가지고 있던 값에 메모리에 변화를 주는게 아니라, 그냥 a라는 Variables이 다른 메모리 공간에 있는 값을 읽게 되는 것임.
  - python에서 (int, float, string)의 datatype은 read-only기 때문에 동일한 값을 가지면 동일한 메모리 위치를 공유함
  - list는 자체가 하나의 개체이기 때문에 리스트 내에 값이 모두 동일한 메모리 위치를 가지더라도 리스트 자체는 서로 다른 메모리 위치를 사용함
  - 따라서 동일한 메모리 위치를 공유하는 list(or set)를 deepcopy를 통해서 서로 다른 메모리 위치를 사용하게 만들 수 있음 (그런데 내부에 (int, float, string)의 datatype 값들은 동일한 메모리 위치를 공유함, 또한 set도 hashable type 만을 값으로 사용할 수 있기 때문에 내부 값들이 서로 같은 위치를 공유함, [What does "hashable" mean in Python?](https://stackoverflow.com/questions/14535730/what-does-hashable-mean-in-python))
  - python의 "is" 는 두 값이 서로 같은 메모리를 공유하는지 확인하는 것, 단순히 값이 같은지 여부를 판단하려면 "==" 를 사용하는 것이 좋음
  - python에서 Numbers, strings, lists, functions, exceptions, classes, instances, 등등 모든 것이 objects임
  - 이는 이름을 부여할 수 있고, 데이터로 사용할 수 있고, container에 담을 수 있고, 이 밖에 제약 없이 다양하게 사용할 수 있다는 것을 의미함
  - 이래서 때때로 모든 objects를 "first-class" 라고 부르는 것임 ([First Class functions in Python](https://www.geeksforgeeks.org/first-class-functions-python/))
- [06_Design_discussion](https://github.com/dabeaz-course/practical-python/blob/master/Notes/03_Program_organization/06_Design_discussion.md)
  - Function Design의 주요 목표는 모듈화와 예측 가능성임
  - python은 다른 프로그래밍 언어와 다르게, main function과 main method라는 개념이 없음
  - 그 대신 파이썬은 source file 들 중에 제일 처음 시작하는 파일의 __main__ check을 통해서 main module 처럼 사용할 수 있음
  - 함수의 예측 가능성을 높이기 위해서 Doc String, Type Annotation, arguments name 을 짧고 간결하게 작성해주는 것이 좋음
  - 상황에 따라 다르겠지만, 함수의 유연성은 때때로 더 나은 서비스를 만드는데 도움을 줄 수 있기 때문에, 예측 가능성을 위해서 함수의 유연성을 제한하는 것은 좋은 습관이 아닐 수 있음 (read_data 함수를 작성할 때, file_name을 받을 것이냐, Iterable 객체를 받을 것이냐, Duck typing)

## 공부 기록
- 2023.11.24 [02_Working_with_data/02_Containers](https://github.com/dabeaz-course/practical-python/blob/master/Notes/02_Working_with_data/02_Containers.md)
- 2023.11.25 [03_Program_organization/00_Overview](https://github.com/dabeaz-course/practical-python/blob/master/Notes/03_Program_organization/00_Overview.md)
- 2023.11.26 [03_Program_organization/05_Main_module](https://github.com/dabeaz-course/practical-python/blob/master/Notes/03_Program_organization/05_Main_module.md)
- 2023.12.17 [03_Program_organization/06_Design_discussion](https://github.com/dabeaz-course/practical-python/blob/master/Notes/03_Program_organization/06_Design_discussion.md)