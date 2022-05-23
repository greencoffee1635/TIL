'''
최소힙
최소힙은 완전이진트리로 구현된 자료구조입니다.
그 구성은 부모 노드값이 왼쪽자식과 오른쪽 자식노드의 값보다 작게 트리를 구성하는 것입니다.
그렇게 하면 트리의 루트(root)노드는 입력된 값들 중 가장 작은 값이 저장되어 있습니다.
예를 들어 5 3 2 1 4 6 7순으로 입력되면 최소힙 트리는 아래와 같이 구성됩니다.

    1       0레벨 부모 
  2   3     1레벨 자식, 형제 
5  4  6  7  2레벨 자식, 형제1, 형제2 

-> 최소 힙 자료구조 
-> 계속 올라가는 것을 업힙이라고 한다.

최소힙 자료를 이용하여 다음과 같은 연산을 하는 프로그램을 작성하세요.
1) 자연수가 입력되면 최소힙에 입력한다.
2) 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다. (출력할 자료가 없으면 -1를 출력한다.)
3) -1이 입력되면 프로그램 종료한다.

- 입력설명
첫 번째 줄부터 숫자가 입력된다.
입력되는 숫자는 100,000개 이하이며 각 숫자의 크기는 정수형 범위에 있다.

- 출력설명
연산을 한 결과를 보여준다.

- 입력예제 1
5
3
6
0
5
0
2
4
0
-1

- 출력예제 1
3
5
2
'''

# 1.
import heapq as hq

a = []  # heapq하려면 list가 필요하다.

while True:
    n = int(input())
    if n == -1:  # -1이면 입력이 종료
        break
    if n == 0:  # heap에 자료가 없을 때
        if len(a) == 0:  # heap자료 구조가 비어 있는 것
            print(-1)
        else:  # heap자료구조에 데이터가 있는 것
            print(hq.heappop(a))  # heappop a에서 자료를 1개 빼준다.
    else:
        hq.heappush(a, n)  # 0이 아니면 a라는 list에 n값을 push


# 2. another code 내장함수 안쓰고 구현하기
class Heap:  # min heap
    def __init__(self):
        self.values = [0]

    def is_empty(self):
        return len(self.values) == 1

    def push(self, value):
        index = len(self.values)
        self.values.append(value)
        while index > 1:
            if self.values[index // 2] > self.values[index]:
                self.swap(index, index // 2)
            else:
                break
            index = index // 2

    def swap(self, index1, index2):
        self.values[index1], self.values[index2] = self.values[index2], self.values[index1]

    def pop(self):
        min_value = self.values[1]
        self.values[1] = self.values.pop()
        index = 1
        n = len(self.values) - 1
        while True:
            if n < index * 2:  # no child
                break
            elif n < index * 2 + 1:  # only left child
                if self.values[index] > self.values[index * 2]:
                    self.swap(index, index * 2)
                    index = index * 2
                else:
                    break
            else:  # have both children
                if self.values[index] > self.values[index * 2] or self.values[index] > self.values[index * 2 + 1]:
                    if self.values[index * 2] < self.values[index * 2 + 1]:
                        self.swap(index, index * 2)
                        index = index * 2
                    else:
                        self.swap(index, index * 2 + 1)
                        index = index * 2 + 1
                else:
                    break

        return min_value


heap = Heap()

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if heap.is_empty():
            print(-1)
        else:
            print(heap.pop())
    else:
        heap.push(n)
