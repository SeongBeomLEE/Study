# Pytorch Memory fragmentation로 인한 Out of Memory
- 메모리 조각화는 할당된 블록 사이에 작고 사용할 수 없는 간격을 남기는 방식으로 메모리를 할당 및 할당 취소할 때 발생함
- PyTorch에서 메모리 조각화는 동적 메모리 할당, 가변 텐서 크기, 모델 복잡성 및 레이어 크기, 배치 크기 변형, GPU 메모리 제약 등의 원인으로 발생함
- 이는 메모리 사용량 증가, 성능 저하, 메모리 부족, 가비지 수집 오버헤드 증가 등의 이슈를 발생시킴
- 따라서 환경 변수에 max_split_size_mb 설정을 줘서 메모리 조각화 이슈를 최소화 해야함
    - PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:int(20 미만의 값을 주면 에러 발생)
- 그런데 max_split_size_mb는 하이퍼파라미터로 실험를 통해서 적절한 값을 찾아야 함

## 참고 자료
- [Unexpected OOM after warmup for request that has token less than max-batch-prefill-token](https://github.com/huggingface/text-generation-inference/issues/1374)
- [How can I set max_split_size_mb to avoid fragmentation in Pytorch?](https://dev.to/shittu_olumide_/how-can-i-set-maxsplitsizemb-to-avoid-fragmentation-in-pytorch-37h9)
- [Memory Management using PYTORCH_CUDA_ALLOC_CONF](https://iamholumeedey007.medium.com/memory-management-using-pytorch-cuda-alloc-conf-dabe7adec130)