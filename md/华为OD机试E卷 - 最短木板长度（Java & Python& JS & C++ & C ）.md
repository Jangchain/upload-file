## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小明有 n 块木板，第 i ( 1 ≤ i ≤ n ) 块木板长度为 ai。  
小明买了一块长度为 m 的木料，这块木料可以切割成任意块，拼接到已有的木板上，用来加长木板。  
小明想让最短的模板尽量长。请问小明加长木板后，最短木板的长度可以为多少？

## 输入描述

输入的第一行包含两个正整数， n ( 1 ≤ n ≤ 10^3 ), m ( 1 ≤ m ≤ 10^6 )，n 表示木板数， m 表示木板长度。  
输入的第二行包含 n 个正整数， a1, a2,…an ( 1 ≤ ai ≤ 10^6 )。

###

## 输出描述

输出的唯一一行包含一个正整数，表示加长木板后，最短木板的长度最大可以为多少？

## 示例1

输入

    
    
    5 3
    4 5 3 5 5
    

输出

    
    
    5
    

说明

> 给第1块木板长度增加1，给第3块木板长度增加2后，  
>  这5块木板长度变为[5,5,5,5,5]，最短的木板的长度最大为5。

## 示例2

输入

    
    
    5 2
    4 5 3 5 5
    

输出

    
    
    4
    

说明

> 给第3块木板长度增加1后，这5块木板长度变为[4,5,4,5,5]，剩余木料的长度为1。此时剩余木料无论给哪块木板加长，最短木料的长度都为4。

## 解题思路

采用贪心的思想：循环遍历木料的长度，每次都给最短的木板补一米的长度。补完之后重新排序，重复补一米的操作。知道木料用完。

采用优先队列（最小堆）来解决这个问题。以下是详细的解题思路：

  1. 首先，从输入中读取木板数量 `n` 和木料长度 `m`。
  2. 接下来，读取 `n` 个木板的长度，并将它们存储在一个数组或列表中。
  3. 创建一个优先队列（最小堆）`pq`，并将所有木板长度添加到队列中。优先队列会自动按照升序排列木板长度。
  4. 当木料长度 `m` 大于 0 时，执行以下操作：  
a. 从优先队列 `pq` 中取出最短的木板长度 `minWood`。  
b. 将最短木板长度加 1，得到新的木板长度 `newWoodLength`。  
c. 木料长度 `m` 减 1。  
d. 将新的木板长度 `newWoodLength` 添加到优先队列 `pq` 中。

  5. 当木料长度 `m` 用完后，从优先队列 `pq` 中取出最短的木板长度，并输出结果。

解题思路的关键在于使用优先队列（最小堆）来存储木板长度。这样可以在每次循环时快速找到最短的木板长度。在每次循环中，我们从优先队列中取出最短的木板长度，将其加长后再放回队列。这个过程重复
`m` 次，直到所有的木料都被用完。最后，从优先队列中取出最短的木板长度作为结果输出。

## Java

    
    
    import java.util.PriorityQueue;
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            // 创建一个Scanner对象，用于读取用户输入
            Scanner sc = new Scanner(System.in);
    
            // 读取木板数量n和木料长度m
            int n = sc.nextInt();
            int m = sc.nextInt();
    
            // 创建一个长度为n的数组a，用于存储木板长度
            int[] a = new int[n];
            // 读取n个木板长度，并存储到数组a中
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
    
            // 创建一个优先队列pq，用于存储木板长度，并按照升序排列
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            // 将数组a中的木板长度添加到优先队列pq中
            for (int ai : a) {
                pq.offer(ai);
            }
    
            // 当木料长度m大于0时，循环执行以下操作
            while (m > 0) {
                // 从优先队列pq中取出最短的木板长度minWood
                int minWood = pq.poll();
                // 将最短木板长度加1，得到新的木板长度newWoodLength
                int newWoodLength = minWood + 1;
                // 木料长度m减1
                m--;
                // 将新的木板长度newWoodLength添加到优先队列pq中
                pq.offer(newWoodLength);
            }
    
            // 从优先队列pq中取出最短的木板长度，并输出结果
            System.out.println(pq.peek());
        }
    }
    
    
    

## Python

    
    
    import heapq
    
    # 读取木板数量n和木料长度m
    n, m = map(int, input().split())
    
    # 读取n个木板长度，并存储到列表a中
    a = list(map(int, input().split()))
    
    # 创建一个优先队列pq，用于存储木板长度，并按照升序排列
    pq = a.copy()
    heapq.heapify(pq)
    
    # 当木料长度m大于0时，循环执行以下操作
    while m > 0:
        # 从优先队列pq中取出最短的木板长度minWood
        minWood = heapq.heappop(pq)
        # 将最短木板长度加1，得到新的木板长度newWoodLength
        newWoodLength = minWood + 1
        # 木料长度m减1
        m -= 1
        # 将新的木板长度newWoodLength添加到优先队列pq中
        heapq.heappush(pq, newWoodLength)
    
    # 从优先队列pq中取出最短的木板长度，并输出结果
    print(pq[0])
    

## JavaScript

    
    
    const readline = require("readline");
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let input = [];
    rl.on("line", (line) => {
        input.push(line);
    });
    
    rl.on("close", () => {
        // 读取木板数量 n 和木料长度 m
        const [n, m] = input[0].split(" ").map(Number);
        let boards = input[1].split(" ").map(Number);
    
        // 排序木板数组，以模拟优先队列的最小堆功能
        boards.sort((a, b) => a - b);
    
        let remainingWood = m;
    
        while (remainingWood > 0) {
            // 每次取出最短的木板（数组首元素），加长 1
            boards[0] += 1;
            remainingWood--;
    
            // 每次操作后重新排序，保持最短木板在数组首位
            boards.sort((a, b) => a - b);
        }
    
        // 输出当前最短的木板长度
        console.log(boards[0]);
    });
    
    

## C++

    
    
    #include <iostream>
    #include <queue>
    #include <vector>
    
    int main() {
        // 创建一个输入流对象，用于读取用户输入
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
    
        // 读取木板数量n和木料长度m
        int n, m;
        std::cin >> n >> m;
    
        // 创建一个长度为n的vector a，用于存储木板长度
        std::vector<int> a(n);
        // 读取n个木板长度，并存储到vector a中
        for (int i = 0; i < n; i++) {
            std::cin >> a[i];
        }
    
        // 创建一个优先队列pq，用于存储木板长度，并按照升序排列
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        // 将vector a中的木板长度添加到优先队列pq中
        for (int ai : a) {
            pq.push(ai);
        }
    
        // 当木料长度m大于0时，循环执行以下操作
        while (m > 0) {
            // 从优先队列pq中取出最短的木板长度minWood
            int minWood = pq.top();
            pq.pop();
            // 将最短木板长度加1，得到新的木板长度newWoodLength
            int newWoodLength = minWood + 1;
            // 木料长度m减1
            m--;
            // 将新的木板长度newWoodLength添加到优先队列pq中
            pq.push(newWoodLength);
        }
    
        // 从优先队列pq中取出最短的木板长度，并输出结果
        std::cout << pq.top() << std::endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    
    #define MAX_N 1000  // 假设木板数最大为 1000
    
    // 辅助函数：将数组按升序排序
    void sort(int arr[], int n) {
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    int main() {
        int n, m;
        scanf("%d %d", &n, &m);
    
        int boards[MAX_N];
        for (int i = 0; i < n; i++) {
            scanf("%d", &boards[i]);
        }
    
        // 初始排序
        sort(boards, n);
    
        int remainingWood = m;
    
        // 每次操作木料时都找到最小木板进行加长
        while (remainingWood > 0) {
            boards[0] += 1;  // 将最短木板加长 1
            remainingWood--;
    
            // 保持数组升序，以确保数组首元素是最短木板
            sort(boards, n);
        }
    
        // 输出最短木板的长度
        printf("%d\n", boards[0]);
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

