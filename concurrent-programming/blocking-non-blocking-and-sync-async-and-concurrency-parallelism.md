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
    - 1명이 5개의 작업을 빠른 시간에 이것 저것 실행
    - I/O Bound: 수행시간에 I/O가 더 영향이 큰 작업. 네트워크, 디스크 등
    - 동시성에서는 Context Switch가 발생함

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

## 참고 자료
- [Blocking/Non-Blocking & Sync/Async](https://goodgid.github.io/Blocking-NonBlocking-Synchronous-Asynchronous/)
- [Blocking-NonBlocking-Synchronous-Asynchronous](https://homoefficio.github.io/2017/02/19/Blocking-NonBlocking-Synchronous-Asynchronous/)
- [Sync async-blocking-nonblocking-io](https://www.slideshare.net/unitimes/sync-asyncblockingnonblockingio)
- [동시성(Concurrency)과 병렬성(Parallelism)](https://goodgid.github.io/Concurrency-vs-Paraleelism/)
- [동시성(Concurrency) vs 병렬성(Parallelism)](https://atin.tistory.com/567)
- [동시성과 병렬성](https://ohgyun.com/741)
- [Concurrency and async / await](https://fastapi.tiangolo.com/async/)
- https://chat.openai.com/c/a5500fde-75b8-49c8-b55f-4de1a7917380