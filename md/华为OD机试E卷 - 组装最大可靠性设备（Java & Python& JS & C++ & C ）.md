## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

一个设备由N种类型元器件组成(每种类型元器件只需要一个，类型type编号从0~N-1)，

每个元器件均有可靠性属性reliability，可靠性越高的器件其价格price越贵。

而设备的可靠性由组成设备的所有器件中可靠性最低的器件决定。

给定预算S，购买N种元器件( 每种类型元器件都需要购买一个)，在不超过预算的情况下，请给出能够组成的设备的最大可靠性。

## 输入描述

`S N`，其中`S`为总的预算，`N`元器件的种类

`total`，表示元器件的总数，每种型号的元器件可以有多种

此后输入有`total`行具体器件的数据

`type reliability price`。其中`type`为整数类型，代表元器件的类型编号从`0 ~ N-1`；`reliabily`
整数类型，代表元器件的可靠性；`price` 整数类型，代表元器件的价格

##### 备注

  * 0 <= S,price <= 10000000
  * 0 <= N <= 100
  * 0 <= type <= N-1
  * 0 <= total <= 100000
  * 0 < reliability <= 100000

## 输出描述

符合预算的设备的最大可靠性，如果预算无法买齐N种器件，则返回 -1

## 示例1

输入

    
    
    500 3
    6
    0 80 100
    0 90 200
    1 50 50
    1 70 210
    2 50 100
    2 60 150
    

输出

    
    
    60
    
    

说明

> 预算500，设备需要3种元件组成，方案
>
> 类型0的第一个(可靠性80),
>
> 类型1的第二个(可靠性70),
>
> 类型2的第二个(可靠性60),
>
> 可以使设备的可靠性最大 60

## 示例2

输入

    
    
    100 1
    1
    0 90 200
    

输出

    
    
    -1
    

说明

> 组成设备需要1个元件，但是元件价格大于预算，因此无法组成设备，返回-1

## 解题思路

这道题的核心是：在给定预算的情况下，从每种类型的元器件中选择一个，使得组装的设备可靠性最大，而设备的可靠性由所有元器件中最低的可靠性决定。题目要求在不超过预算的前提下，找到能够组成设备的最大可靠性。

#### 题目解析：

  1. **设备由N种类型的元器件组成** ：

     * 每种类型的元器件只需要购买一个。
     * 类型从0到N-1，每种类型的元器件有不同的价格和可靠性。
  2. **可靠性** ：

     * 每个元器件都有一个可靠性属性，设备的整体可靠性由选择的元器件中**最低的可靠性** 决定。
     * 因此，选择元器件时，需要找到一种组合，使得选出的N种元器件的**最低可靠性最大化** 。
  3. **预算限制** ：

     * 你需要在总预算`S`内，购买N种元器件。

#### 解题思路：

  1. **分类处理元器件** ：

     * 对输入的元器件按照类型分类，将每种类型的元器件分组，这样可以针对每个类型单独选择最合适的元器件。
  2. **动态规划求解** ：

     * 可以使用动态规划来解决这个问题。设`dp[i][j]`表示在考虑到第`i`种元器件时，预算不超过`j`时的最大可靠性。
     * 初始状态`dp[0][...]`表示只选择第0类元器件时的情况。
     * 对于每种类型，遍历该类型所有可选的元器件，更新状态，使得在不超过预算的情况下，最大化可靠性。
  3. **选择合适的元器件** ：

     * 对每个类型的元器件，从中挑选可靠性高且价格在预算范围内的元器件。
     * 在更新状态时，设备的可靠性取决于选出的所有元器件中**最低的可靠性** ，因此在选择元器件时，要尽量保证最终的最小可靠性最大化。
  4. **边界情况** ：

     * 如果预算不足以购买每种类型的元器件，则返回`-1`。

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static int maxReliability(int S, int N, int[][] components) {
            // 初始化每种类型的元器件
            List<int[]>[] types = new ArrayList[N];
            for (int i = 0; i < N; i++) {
                types[i] = new ArrayList<>();
            }
    
            // 将每个元器件根据其类型进行分类
            for (int[] component : components) {
                int t = component[0];  // 设备类型
                int r = component[1];  // 设备可靠性
                int p = component[2];  // 设备价格
                types[t].add(new int[]{r, p});
            }
    
            // 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
            int[][] dp = new int[N + 1][S + 1];
            for (int[] row : dp) {
                Arrays.fill(row, -1);
            }
            dp[0][0] = Integer.MAX_VALUE;  // 初始化为无穷大，表示没有选择任何元器件时可靠性无穷大
    
            // 对每种类型的元器件进行处理
            for (int i = 1; i <= N; i++) {
                // 遍历每种类型的所有元器件
                for (int[] component : types[i - 1]) {
                    int r = component[0];  // 设备可靠性
                    int p = component[1];  // 设备价格
                    // 从后向前更新dp数组，确保每个元器件只使用一次
                    for (int budget = S; budget >= p; budget--) {
                        if (dp[i - 1][budget - p] != -1) {
                            dp[i][budget] = Math.max(dp[i][budget], Math.min(dp[i - 1][budget - p], r));
                        }
                    }
                }
            }
    
            // 找到预算范围内的最大可靠性
            int result = Arrays.stream(dp[N]).max().getAsInt();
            return result == -1 ? -1 : result;
        }
    
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            // 从输入获取预算和元器件信息
            int S = sc.nextInt();  // 预算
            int N = sc.nextInt();  // 元器件类型数量
            int total = sc.nextInt();  // 总元器件数目
    
            int[][] components = new int[total][3];  // 存储每个元器件的类型、可靠性和价格
            for (int i = 0; i < total; i++) {
                components[i][0] = sc.nextInt();  // 元器件类型
                components[i][1] = sc.nextInt();  // 元器件可靠性
                components[i][2] = sc.nextInt();  // 元器件价格
            }
    
            // 计算并输出最大可靠性
            System.out.println(maxReliability(S, N, components));
        }
    }
    

## Python

    
    
    def max_reliability(S, N, components):
        # 初始化每种类型的元器件
        types = [[] for _ in range(N)]
        
        # 将每个元器件根据其类型进行分类
        for t, r, p in components:
            types[t].append((r, p))
        
        # 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
        dp = [[-1] * (S + 1) for _ in range(N + 1)]
        dp[0][0] = float('inf')  # dp[0][0] 初始化为无穷大，表示没有选择任何元器件时可靠性无穷大
    
        # 对每种类型的元器件进行处理
        for i in range(1, N + 1):
            # 遍历每种类型的所有元器件
            for r, p in types[i - 1]:
                # 从后向前更新dp数组，确保每个元器件只使用一次
                for budget in range(S, p - 1, -1):
                    if dp[i - 1][budget - p] != -1:
                        dp[i][budget] = max(dp[i][budget], min(dp[i - 1][budget - p], r))
    
        # 找到预算范围内的最大可靠性
        result = max(dp[N])
        
        # 如果结果仍然是-1，表示无法满足条件，返回-1
        return result if result != -1 else -1
    
    # 从输入获取预算和元器件信息
    S, N = map(int, input().split())
    total = int(input())
    
    components = []
    
    for _ in range(total):
        t, r, p = map(int, input().split())
        components.append((t, r, p))
    
    # 计算并输出最大可靠性
    print(max_reliability(S, N, components))
    

## JavaScript

    
    
    function maxReliability(S, N, components) {
        // 初始化每种类型的元器件
        let types = Array.from({ length: N }, () => []);
    
        // 将每个元器件根据其类型进行分类
        for (let [t, r, p] of components) {
            types[t].push([r, p]);
        }
    
        // 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
        let dp = Array.from({ length: N + 1 }, () => Array(S + 1).fill(-1));
        dp[0][0] = Infinity;  // dp[0][0] 初始化为无穷大
    
        // 对每种类型的元器件进行处理
        for (let i = 1; i <= N; i++) {
            // 遍历每种类型的所有元器件
            for (let [r, p] of types[i - 1]) {
                // 从后向前更新dp数组
                for (let budget = S; budget >= p; budget--) {
                    if (dp[i - 1][budget - p] !== -1) {
                        dp[i][budget] = Math.max(dp[i][budget], Math.min(dp[i - 1][budget - p], r));
                    }
                }
            }
        }
    
        // 找到预算范围内的最大可靠性
        let result = Math.max(...dp[N]);
        return result === -1 ? -1 : result;
    }
    
    // 从输入获取预算和元器件信息
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.on('line', (input) => {
        const [S, N] = input.split(' ').map(Number);
        rl.on('line', (totalInput) => {
            const total = Number(totalInput);
            let components = [];
            let count = 0;
    
            rl.on('line', (line) => {
                components.push(line.split(' ').map(Number));
                count++;
                if (count === total) {
                    console.log(maxReliability(S, N, components));
                    rl.close();
                }
            });
        });
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <algorithm>
    #include <climits>
    using namespace std;
    
    int maxReliability(int S, int N, vector<vector<int>>& components) {
        // 初始化每种类型的元器件
        vector<vector<pair<int, int>>> types(N);
        for (const auto& comp : components) {
            int t = comp[0], r = comp[1], p = comp[2];
            types[t].emplace_back(r, p);
        }
    
        // 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
        vector<vector<int>> dp(N + 1, vector<int>(S + 1, -1));
        dp[0][0] = INT_MAX;  // dp[0][0] 初始化为无穷大
    
        // 对每种类型的元器件进行处理
        for (int i = 1; i <= N; ++i) {
            // 遍历每种类型的所有元器件
            for (const auto& [r, p] : types[i - 1]) {
                // 从后向前更新dp数组
                for (int budget = S; budget >= p; --budget) {
                    if (dp[i - 1][budget - p] != -1) {
                        dp[i][budget] = max(dp[i][budget], min(dp[i - 1][budget - p], r));
                    }
                }
            }
        }
    
        // 找到预算范围内的最大可靠性
        return *max_element(dp[N].begin(), dp[N].end());
    }
    
    int main() {
        int S, N, total;
        cin >> S >> N >> total;
    
        // 从输入获取元器件信息
        vector<vector<int>> components(total, vector<int>(3));
        for (int i = 0; i < total; ++i) {
            cin >> components[i][0] >> components[i][1] >> components[i][2];
        }
    
        // 计算并输出最大可靠性
        int result = maxReliability(S, N, components);
        cout << (result == -1 ? -1 : result) << endl;
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <limits.h>
    
    int max(int a, int b) {
        return a > b ? a : b;
    }
    
    int min(int a, int b) {
        return a < b ? a : b;
    }
    
    int maxReliability(int S, int N, int components[][3], int total) {
        // 初始化每种类型的元器件
        int types[N][total][2];  // 最大支持的元器件数是 total
        int type_count[N];
        for (int i = 0; i < N; i++) {
            type_count[i] = 0;
        }
    
        // 将每个元器件根据其类型进行分类
        for (int i = 0; i < total; i++) {
            int t = components[i][0];  // 元器件类型
            int r = components[i][1];  // 元器件可靠性
            int p = components[i][2];  // 元器件价格
            types[t][type_count[t]][0] = r;
            types[t][type_count[t]][1] = p;
            type_count[t]++;
        }
    
        // 初始化 dp 数组，dp[i][j] 表示选择前i种类型的元器件，预算为j时的最大可靠性
        int dp[N + 1][S + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= S; j++) {
                dp[i][j] = -1;
            }
        }
        dp[0][0] = INT_MAX;  // dp[0][0] 初始化为无穷大
    
        // 对每种类型的元器件进行处理
        for (int i = 1; i <= N; i++) {
            // 遍历每种类型的所有元器件
            for (int k = 0; k < type_count[i - 1]; k++) {
                int r = types[i - 1][k][0];
                int p = types[i - 1][k][1];
                // 从后向前更新dp数组
                for (int budget = S; budget >= p; budget--) {
                    if (dp[i - 1][budget - p] != -1) {
                        dp[i][budget] = max(dp[i][budget], min(dp[i - 1][budget - p], r));
                    }
                }
            }
        }
    
        // 找到预算范围内的最大可靠性
        int result = -1;
        for (int i = 0; i <= S; i++) {
            if (dp[N][i] > result) {
                result = dp[N][i];
            }
        }
        return result;
    }
    
    int main() {
        int S, N, total;
        scanf("%d %d %d", &S, &N, &total);
    
        // 从输入获取元器件信息
        int components[total][3];
        for (int i = 0; i < total; i++) {
            scanf("%d %d %d", &components[i][0], &components[i][1], &components[i][2]);
        }
    
        // 计算并输出最大可靠性
        int result = maxReliability(S, N, components, total);
        printf("%d\n", result == -1 ? -1 : result);
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/627e7803ce517a5584911cb6670b5182.png)

## 完整用例

### 用例1

    
    
    1000 4
    8
    0 90 300
    0 80 200
    1 85 250
    1 75 200
    2 65 150
    2 70 170
    3 55 130
    3 60 160
    

### 用例2

    
    
    100 1
    1
    0 90 200
    

### 用例3

    
    
    300 2
    4
    0 30 100
    0 40 120
    1 20 100
    1 25 110
    

### 用例4

    
    
    1000 5
    10
    0 20 90
    1 20 80
    2 20 70
    3 20 60
    4 20 50
    0 21 95
    1 21 85
    2 21 75
    3 21 65
    4 21 55
    

### 用例5

    
    
    50 2
    3
    0 100 60
    1 90 50
    1 80 40
    

### 用例6

    
    
    200 2
    4
    0 30 120
    0 35 130
    1 25 70
    1 28 75
    

### 用例7

    
    
    600 3
    5
    0 100 200
    0 95 180
    1 90 190
    1 85 170
    2 80 160
    

### 用例8

    
    
    500 2
    4
    0 55 250
    0 60 260
    1 45 240
    1 50 250
    

### 用例9

    
    
    1200 4
    8
    0 99 300
    1 98 300
    2 97 300
    3 96 300
    0 95 290
    1 94 290
    2 93 290
    3 92 290
    

### 用例10

    
    
    900 3
    6
    0 95 310
    1 85 300
    2 75 290
    0 65 280
    1 55 270
    2 45 260
    

