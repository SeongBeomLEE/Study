# blocking / non-blocking, sync / async, concurrency / parallelism 정리
## Blocking과 Non-Blocking
- Blocking과 Non-Blocking은 함수 호출 시 제어권 리턴 유무로 파악할 수 있음
- A가 B를 호출한다고 가정하면, A는 B를 호출한 함수가 되고, B는 호출된 함수가 됨
- B가 바로 제어권을 A에게 넘겨서, A가 다른 일을 할 수 있으면 Non-Blocking임
- B가 자신의 작업을 모두 완료한 후, A에게 제어권을 넘겨주면(A가 B 함수가 작업을 하는 동안 계속 대기함) Blocking임

## Synchronous와 Asynchronous
- Synchronous와 Asynchronous은 함수 호출 시 작업 완료 여부 신경 유무로 파악할 수 있음
- A가 B를 호출한다고 가정하면, A는 B를 호출한 함수가 되고, B는 호출된 함수가 되고, 추가적으로 A는 B에게 요청한 작업이 끝나면 C작업을 수행하길 요구함
- A가 B에게 처음 요청한 작업의 완료 여부를 신경쓰지 않고, 바로 C 작업을 요구하면 Asynchronous임
- A가 B에게 처음 요청한 작업의 완료 여부를 신경쓰고, A가 B의 작업이 끝난 후에 C 작업을 요구하면 Synchronous임

## Blocking + Synchronous
- B가 자신의 작업을 모두 완료한 후, A에게 제어권을 넘겨주고, A는 계속 B의 작업이 완료될 때 까지 기다리는 경우

## Blocking + Asynchronous
- B가 자신의 작업을 모두 완료한 후, A에게 제어권을 넘겨주고, A는 B의 작업이 완료될 때 까지 기다리지 않고, 계속 다른 작업을 주는 경우이지만, B가 A에게 제어권을 주지 않아서, A는 계속 다른 작업을 줄 수 없기 때문에 Blocking + Synchronous 와 동일하게 동작한다고 생각함

## Non-Blocking + Synchronous
-  B가 자신의 작업을 모두 완료하지 않은 상태에서, A에게 곧바로 제어권을 넘겨주고, A는 계속 B의 작업이 완료될 때 까지 기다리는 경우이지만, A는 기다리는 동안 다른 작업을 수행할 수 있지만, A는 계속 B의 작업이 완료될 때 까지 기다리기 때문에 Blocking + Synchronous 와 동일하게 동작한다고 생각함

## Non-Blocking + Asynchronous
-  B가 자신의 작업을 모두 완료하지 않은 상태에서, A에게 곧바로 제어권을 넘겨주고, A는 B의 작업이 완료될 때 까지 기다리지 않고, 계속 다른 작업을 주는 경우로 A는 B의 작업 완료 여부를 신경 쓰지 않기 때문에 기다리는 동안 다른 작업을 계속 수행할 수 있으므로, A 입장에서는 동시성을 달성함

## concurrency과 parallelism
- 동시성은 싱글 코어에서 멀티 쓰레드를 동작시키기 위한 방식
    - 멀티 쓰레드란 멀티 태스킹을 위해 여러 개의 쓰레드가 번갈아가면서 실행되는 성질을 말함
    - 동시성을 이용한 싱글 코어의 멀티 태스킹은 동시에 실행되는 것처럼 보이는 것으로, 실제로는 각 쓰레드들이 번갈아가면서 조금씩 실행되고 있는 것임
        - 멀티 태스킹은 다수의 작업(혹은 프로세스, 이하 태스크)이 중앙 처리 장치(이하 CPU)와 같은 공용자원을 나누어 사용하는 것을 말함
    - 1명이 5개의 작업을 빠른 시간에 이것 저것 실행
    - I/O Bound: 수행시간에 I/O가 더 영향이 큰 작업. 네트워크, 디스크 등
    - 동시성에서는 Context Switch 발생함
        - Context Switch은 하나의 프로세스가 CPU를 사용 중인 상태에서 다른 프로세스가 CPU를 사용하도록 하기 위해, 이전의 프로세스의 상태를 보관하고 새로운 프로세스의 상태를 적재하는 작업을 말함

- 병렬성은 멀티 코어에서 멀티 쓰레드를 동작시키는 방식
    - 한 개 이상의 쓰레드를 포함하는 각 코어들이 동시에 실행되는 성질을 말함
    - 멀티 코어에서도 동시성은 사용 가능함
    - 병렬성은 데이터 병렬성(Data parallelism)과 작업 병렬성(Task parallelism)으로 구분됨
        - 데이터 병렬성은 전체 데이터를 서브 데이터들로 나눈 후 서브 데이터들을 병렬 처리하여 작업을 빠르게 수행하는 것을 말함
            - 서브 데이터는 멀티 코어의 수만큼 쪼개어 각각의 데이터들을 분리된 쓰레드에서 병렬 처리함
        - 작업 병렬성은 서로 다른 작업을 병렬 처리하는 것을 말함
            - 대표적인 예는 웹 서버로, 각각의 브라우저에서 요청한 내용을 개별 쓰레드에서 병렬로 처리함
    - 5명이 5개의 작업을 동시에 실행
    - CPU Bound: 수행시간에 CPU가 더 영향이 큰 작업. 압축, 정렬, 인코딩 등

## Process와 Thread
- Process는 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램을 말하며, 하나 이상의 스레드를 통해 실행됨
    - 종종 스케줄링의 대상이 되는 작업(task)이라는 용어와 거의 같은 의미로 쓰임
    - 여러 개의 프로세서를 사용하는 것을 멀티프로세싱이라고 하며 같은 시간에 여러 개의 프로그램을 띄우는 시분할 방식을 멀티태스킹이라고 함
    - 프로세스 관리는 운영 체제의 중요한 부분임

- Thread는 어떠한 프로그램 내에서, 특히 프로세스 내에서 실행되는 흐름의 단위를 말함
    - 일반적으로 한 프로그램은 하나의 스레드를 가지고 있지만, 프로그램 환경에 따라 둘 이상의 스레드를 동시에 실행할 수 있으먀, 이를 멀티스레드(multithread)라고 함

- 멀티프로세스와 멀티스레드는 양쪽 모두 여러 흐름이 동시에 진행된다는 공통점을 가지고 있음
- 멀티프로세스에서 각 프로세스는 독립적으로 실행되며 각각 별개의 메모리를 차지하고 있음
- 멀티스레드는 프로세스 내의 메모리를 공유해 사용할 수 있음
- 프로세스 간의 전환 속도보다 스레드 간의 전환 속도가 빠름
- 멀티스레드의 다른 장점은 CPU가 여러 개일 경우에 각각의 CPU가 스레드 하나씩을 담당하는 방법으로 속도를 높일 수 있음

## 참고 자료
- [Blocking/Non-Blocking & Sync/Async](https://goodgid.github.io/Blocking-NonBlocking-Synchronous-Asynchronous/)
- [Blocking-NonBlocking-Synchronous-Asynchronous](https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/)
- [Sync async-blocking-nonblocking-io](https://www.slideshare.net/unitimes/sync-asyncblockingnonblockingio)
- [동시성(Concurrency)과 병렬성(Parallelism)](https://goodgid.github.io/Concurrency-vs-Paraleelism/)
- [동시성(Concurrency) vs 병렬성(Parallelism)](https://atin.tistory.com/567)
- [동시성과 병렬성](https://ohgyun.com/741)
- [Concurrency and async / await](https://fastapi.tiangolo.com/async/)
- https://chat.openai.com/c/a5500fde-75b8-49c8-b55f-4de1a7917380