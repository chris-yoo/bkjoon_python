from collections import deque

T = int(input())
queue = deque(list(map(int, input().split())))
stack = []
label = deque([i for i in range(1, T + 1)])


def isPossible(queue: deque, stack: list, label: deque):
    # 큐에 있는 모든 원소 처리
    while queue:
        # 현재 라벨과 큐의 첫 원소가 일치하면
        if queue[0] == label[0]:
            queue.popleft()
            label.popleft()
        # 스택 맨 위 원소와 라벨이 일치하면
        elif stack and stack[-1] == label[0]:
            stack.pop()
            label.popleft()
        # 둘 다 일치하지 않으면 큐에서 스택으로 이동
        else:
            stack.append(queue.popleft())

    # 큐가 비었으면 스택에 남은 원소들 처리
    while stack:
        if stack[-1] == label[0]:
            stack.pop()
            label.popleft()
        else:
            return "Sad"  # 순서가 맞지 않으면 불가능

    # 모든 원소가 처리되었는지 확인
    return "Nice" if not label else "Sad"


print(isPossible(queue, stack, label))
