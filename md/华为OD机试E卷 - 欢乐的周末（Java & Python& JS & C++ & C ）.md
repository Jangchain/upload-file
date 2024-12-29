## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

小华和小为是很要好的朋友，他们约定周末一起吃饭。

通过手机交流，他们在地图上选择了多个聚餐地点（由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能到达的聚餐地点有多少个？

## 输入描述

第一行输入m和n，m代表地图的长度，n代表地图的宽度。

第二行开始具体输入地图信息，地图信息包含：

0 为通畅的道路

1 为障碍物（且仅1为障碍物）

2 为小华或者小为，地图中必定有且仅有2个 （非障碍物）

3 为被选中的聚餐地点（非障碍物）

## 备注：

地图的长宽为m和n，其中：

  * 4 <= m <= 100
  * 4 <= n <= 100

聚餐的地点数量为 k，则

  * 1< k <= 100

## 输出描述

可以被两方都到达的聚餐地点数量，行末无空格。

## 示例1

输入

    
    
    4 4
    2 1 0 3
    0 1 2 1
    0 3 0 0
    0 0 0 0
    

输出

    
    
    2
    

说明

> 第一行输入地图的长宽为3和4。  
>  第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。  
>  此时两者能都能到达的聚餐位置有2处

## 示例2

输入

    
    
    4 4
    2 1 2 3
    0 1 0 0
    0 1 0 0
    0 1 0 0
    

输出

    
    
    0
    

说明

> 第一行输入地图的长宽为4和4。  
>  第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。  
>  由于图中小华和小为之间有个阻隔，此时，没有两人都能到达的聚餐地址，故而返回0。

## 解题思路

典型的图类型题目，可以使用图算法（如 BFS 或 DFS）从两人的起始位置出发，记录可到达的聚餐地点，最后统计共同的地点数量。

  * 地图用一个 `m x n` 的矩阵表示。
  * 不同的数字代表不同的状态： 
    * `0` 表示可通行的道路。
    * `1` 表示障碍物，无法通行。
    * `2` 表示小华或小为的位置，地图中会有两个这样的数字。
    * `3` 表示被选中的聚餐地点，可以有多个。

## 示例解释

### 示例 1

输入：

    
    
    4 4
    2 1 0 3
    0 1 2 1
    0 3 0 0
    0 0 0 0
    

  * 地图长宽为 4 和 4，地图内容如下：
    
        [2, 1, 0, 3]
    [0, 1, 2, 1]
    [0, 3, 0, 0]
    [0, 0, 0, 0]
    

  * 小华和小为分别在 `(0, 0)` 和 `(1, 2)`。
  * 聚餐地点在 `(0, 3)` 和 `(2, 1)`。
  * 可以通过算法（如深度优先搜索 DFS 或广度优先搜索 BFS）查找从小华和小为的位置出发，能够到达的所有聚餐地点，最终发现有 2 个地点可以同时到达。

### 示例 2

输入：

    
    
    4 4
    2 1 2 3
    0 1 0 0
    0 1 0 0
    0 1 0 0
    

  * 地图内容：
    
        [2, 1, 2, 3]
    [0, 1, 0, 0]
    [0, 1, 0, 0]
    [0, 1, 0, 0]
    

  * 小华在 `(0, 0)`，小为在 `(0, 2)`，两者之间有障碍物（`1`），因此不能互通，结果为 0。

## Java

    
    
    import java.util.Scanner;
    import java.util.ArrayList;
    import java.util.List;
    
    public class Main {
        // 定义四个方向的偏移量（上、下、左、右）
        private static int[][] dirs = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
        // 深度优先搜索函数
        private static boolean dfs(int currX, int currY, int targetX, int targetY, int[][] map, boolean[][][] visited, int person) {
            // 如果当前位置就是目标位置，返回true
            if (currX == targetX && currY == targetY) {
                return true;
            }
    
            // 遍历四个方向
            for (int[] dir : dirs) {
                int nextX = currX + dir[0], nextY = currY + dir[1];
                // 如果下一个位置超出地图范围，或者是障碍物，或者已经访问过，跳过
                if (nextX < 0 || nextY < 0 || nextX >= map.length || nextY >= map[0].length || map[nextX][nextY] == 1 || visited[nextX][nextY][person]) {
                    continue;
                }
    
                // 标记下一个位置为已访问
                visited[nextX][nextY][person] = true;
                // 递归搜索下一个位置
                if (dfs(nextX, nextY, targetX, targetY, map, visited, person)) {
                    return true;
                }
            }
    
            return false;
        }
    
        public static void main(String[] args) {
            // 输入初始化
            Scanner scanner = new Scanner(System.in);
            int m = scanner.nextInt();
            int n = scanner.nextInt();
            int[][] map = new int[m][n];
            // 使用三维数组visited来记录每个人访问过的位置
            boolean[][][] visited = new boolean[m][n][2];
            List<int[]> persons = new ArrayList<>();
            List<int[]> targets = new ArrayList<>();
            // 读取地图信息，并记录小华和小为的位置以及聚餐地点
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    map[i][j] = scanner.nextInt();
                    if (map[i][j] == 2) {
                        persons.add(new int[]{i, j});
                    } else if (map[i][j] == 3) {
                        targets.add(new int[]{i, j});
                    }
                }
            }
    
            // 获取小华和小为的位置
            int[] xiaohua = persons.get(0);
            int[] xiaowei = persons.get(1);
            int res = 0;
            // 遍历所有聚餐地点
            for (int[] target : targets) {
                // 重置visited数组
                visited = new boolean[m][n][2];
                // 判断小华是否能到达目标位置
                if (dfs(xiaohua[0], xiaohua[1], target[0], target[1], map, visited, 0)) {
                    // 重置visited数组
                    visited = new boolean[m][n][2];
                    // 判断小为是否能到达目标位置
                    if (dfs(xiaowei[0], xiaowei[1], target[0], target[1], map, visited, 1)) {
                        // 如果两个人都能到达目标位置，结果加1
                        res++;
                    }
                }
            }
            // 输出可以被两人都到达的聚餐地点数量
            System.out.println(res);
    
            scanner.close();
        }
    }
    
    

## Python

    
    
    # 定义四个方向的偏移量（上、下、左、右）
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    
    # 深度优先搜索函数
    def dfs(currX, currY, targetX, targetY, map, visited, person):
        # 如果当前位置就是目标位置，返回True
        if currX == targetX and currY == targetY:
            return True
    
        # 遍历四个方向
        for dir in dirs:
            nextX, nextY = currX + dir[0], currY + dir[1]
            # 如果下一个位置超出地图范围，或者是障碍物，或者已经访问过，跳过
            if nextX < 0 or nextY < 0 or nextX >= len(map) or nextY >= len(map[0]) or map[nextX][nextY] == 1 or visited[nextX][nextY][person]:
                continue
    
            # 标记下一个位置为已访问
            visited[nextX][nextY][person] = True
            # 递归搜索下一个位置
            if dfs(nextX, nextY, targetX, targetY, map, visited, person):
                return True
    
        return False
    
    # 输入初始化
    m, n = map(int, input().split())
    map = [list(map(int, input().split())) for _ in range(m)]
    # 使用三维数组visited来记录每个人访问过的位置
    visited = [[[False, False] for _ in range(n)] for _ in range(m)]
    persons = []
    targets = []
    
    # 读取地图信息，并记录小华和小为的位置以及聚餐地点
    for i in range(m):
        for j in range(n):
            if map[i][j] == 2:
                persons.append([i, j])
            elif map[i][j] == 3:
                targets.append([i, j])
    
    # 获取小华和小为的位置
    xiaohua = persons[0]
    xiaowei = persons[1]
    res = 0
    
    # 遍历所有聚餐地点
    for target in targets:
        # 重置visited数组
        visited = [[[False, False] for _ in range(n)] for _ in range(m)]
        # 判断小华是否能到达目标位置
        if dfs(xiaohua[0], xiaohua[1], target[0], target[1], map, visited, 0):
            # 重置visited数组
            visited = [[[False, False] for _ in range(n)] for _ in range(m)]
            # 判断小为是否能到达目标位置
            if dfs(xiaowei[0], xiaowei[1], target[0], target[1], map, visited, 1):
                # 如果两个人都能到达目标位置，结果加1
                res += 1
    
    # 输出可以被两人都到达的聚餐地点数量
    print(res)
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    // 定义四个方向的偏移量（上、下、左、右）
    const dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    
    // 深度优先搜索函数
    function dfs(currX, currY, targetX, targetY, map, visited, person) {
        // 如果当前位置就是目标位置，返回true
        if (currX === targetX && currY === targetY) {
            return true;
        }
    
        // 遍历四个方向
        for (const dir of dirs) {
            const nextX = currX + dir[0], nextY = currY + dir[1];
            // 如果下一个位置超出地图范围，或者是障碍物，或者已经访问过，跳过
            if (nextX < 0 || nextY < 0 || nextX >= map.length || nextY >= map[0].length || map[nextX][nextY] === 1 || visited[nextX][nextY][person]) {
                continue;
            }
    
            // 标记下一个位置为已访问
            visited[nextX][nextY][person] = true;
            // 递归搜索下一个位置
            if (dfs(nextX, nextY, targetX, targetY, map, visited, person)) {
                return true;
            }
        }
    
        return false;
    }
    
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    const input = [];
    
    rl.on('line', (line) => {
        input.push(line);
    }).on('close', () => {
        // 输入初始化
        const [m, n] = input.shift().split(' ').map(Number);
        const map = input.splice(0, m).map(row => row.split(' ').map(Number));
        const visited = Array.from({ length: m }, () => Array.from({ length: n }, () => Array(2).fill(false)));
        const persons = [];
        const targets = [];
    
        // 读取地图信息，并记录小华和小为的位置以及聚餐地点
        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (map[i][j] === 2) {
                    persons.push([i, j]);
                } else if (map[i][j] === 3) {
                    targets.push([i, j]);
                }
            }
        }
    
        // 获取小华和小为的位置
        const xiaohua = persons[0];
        const xiaowei = persons[1];
        let res = 0;
    
        // 遍历所有聚餐地点
        for (const target of targets) {
            // 重置visited数组
            visited.forEach(row => row.forEach(cell => cell.fill(false)));
            // 判断小华是否能到达目标位置
            if (dfs(xiaohua[0], xiaohua[1], target[0], target[1], map, visited, 0)) {
                // 重置visited数组
                visited.forEach(row => row.forEach(cell => cell.fill(false)));
                // 判断小为是否能到达目标位置
                if (dfs(xiaowei[0], xiaowei[1], target[0], target[1], map, visited, 1)) {
                    // 如果两个人都能到达目标位置，结果加1
                    res++;
                }
            }
        }
    
        // 输出可以被两人都到达的聚餐地点数量
        console.log(res);
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    
    using namespace std;
    
    // 定义四个方向的偏移量（上、下、左、右）
    const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
    // 深度优先搜索函数
    bool dfs(int currX, int currY, int targetX, int targetY, vector<vector<int>>& map, vector<vector<vector<bool>>>& visited, int person) {
        // 如果当前位置就是目标位置，返回true
        if (currX == targetX && currY == targetY) {
            return true;
        }
    
        // 遍历四个方向
        for (int i = 0; i < 4; ++i) {
            int nextX = currX + dirs[i][0], nextY = currY + dirs[i][1];
            // 如果下一个位置超出地图范围，或者是障碍物，或者已经访问过，跳过
            if (nextX < 0 || nextY < 0 || nextX >= map.size() || nextY >= map[0].size() || map[nextX][nextY] == 1 || visited[nextX][nextY][person]) {
                continue;
            }
    
            // 标记下一个位置为已访问
            visited[nextX][nextY][person] = true;
            // 递归搜索下一个位置
            if (dfs(nextX, nextY, targetX, targetY, map, visited, person)) {
                return true;
            }
        }
    
        return false;
    }
    
    int main() {
        // 输入初始化
        int m, n;
        cin >> m >> n;
        vector<vector<int>> map(m, vector<int>(n));
        // 使用三维数组visited来记录每个人访问过的位置
        vector<vector<vector<bool>>> visited(m, vector<vector<bool>>(n, vector<bool>(2)));
        vector<pair<int, int>> persons, targets;
    
        // 读取地图信息，并记录小华和小为的位置以及聚餐地点
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> map[i][j];
                if (map[i][j] == 2) {
                    persons.emplace_back(i, j);
                } else if (map[i][j] == 3) {
                    targets.emplace_back(i, j);
                }
            }
        }
    
        // 获取小华和小为的位置
        auto xiaohua = persons[0];
        auto xiaowei = persons[1];
        int res = 0;
    
        // 遍历所有聚餐地点
        for (const auto& target : targets) {
            // 重置visited数组
            visited = vector<vector<vector<bool>>>(m, vector<vector<bool>>(n, vector<bool>(2)));
            // 判断小华是否能到达目标位置
            if (dfs(xiaohua.first, xiaohua.second, target.first, target.second, map, visited, 0)) {
                // 重置visited数组
                visited = vector<vector<vector<bool>>>(m, vector<vector<bool>>(n, vector<bool>(2)));
                // 判断小为是否能到达目标位置
                if (dfs(xiaowei.first, xiaowei.second, target.first, target.second, map, visited, 1)) {
                    // 如果两个人都能到达目标位置，结果加1
                    res++;
                }
            }
        }
    
        // 输出可以被两人都到达的聚餐地点数量
        cout << res << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <stdbool.h>
    
    #define MAX 100
    
    // 定义四个方向的偏移量（上、下、左、右）
    const int dirs[4][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
    // 深度优先搜索函数
    bool dfs(int currX, int currY, int targetX, int targetY, int map[MAX][MAX], bool visited[MAX][MAX][2], int person, int m, int n) {
        // 如果当前位置就是目标位置，返回true
        if (currX == targetX && currY == targetY) {
            return true;
        }
    
        // 遍历四个方向
        for (int i = 0; i < 4; ++i) {
            int nextX = currX + dirs[i][0], nextY = currY + dirs[i][1];
            // 如果下一个位置超出地图范围，或者是障碍物，或者已经访问过，跳过
            if (nextX < 0 || nextY < 0 || nextX >= m || nextY >= n || map[nextX][nextY] == 1 || visited[nextX][nextY][person]) {
                continue;
            }
    
            // 标记下一个位置为已访问
            visited[nextX][nextY][person] = true;
            // 递归搜索下一个位置
            if (dfs(nextX, nextY, targetX, targetY, map, visited, person, m, n)) {
                return true;
            }
        }
    
        return false;
    }
    
    int main() {
        // 输入初始化
        int m, n;
        scanf("%d %d", &m, &n);
        int map[MAX][MAX];
        // 使用三维数组visited来记录每个人访问过的位置
        bool visited[MAX][MAX][2] = {{{false}}};
        int persons[2][2]; // 记录小华和小为的位置
        int targetCount = 0;
        int targets[MAX][2]; // 记录聚餐地点
    
        // 读取地图信息，并记录小华和小为的位置以及聚餐地点
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                scanf("%d", &map[i][j]);
                if (map[i][j] == 2) {
                    persons[targetCount][0] = i; // x 坐标
                    persons[targetCount][1] = j; // y 坐标
                    targetCount++;
                } else if (map[i][j] == 3) {
                    targets[targetCount][0] = i; // x 坐标
                    targets[targetCount][1] = j; // y 坐标
                }
            }
        }
    
        int res = 0;
    
        // 遍历所有聚餐地点
        for (int k = 0; k < targetCount; ++k) {
            // 重置visited数组
            memset(visited, false, sizeof(visited));
            // 判断小华是否能到达目标位置
            if (dfs(persons[0][0], persons[0][1], targets[k][0], targets[k][1], map, visited, 0, m, n)) {
                // 重置visited数组
                memset(visited, false, sizeof(visited));
                // 判断小为是否能到达目标位置
                if (dfs(persons[1][0], persons[1][1], targets[k][0], targets[k][1], map, visited, 1, m, n)) {
                    // 如果两个人都能到达目标位置，结果加1
                    res++;
                }
            }
        }
    
        // 输出可以被两人都到达的聚餐地点数量
        printf("%d\n", res);
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/ae0dd6343a5b509bb9514b67516f36da.png)

## 完整用例

### 用例1

    
    
    4 4
    2 1 0 3
    0 1 2 1
    0 3 0 0
    0 0 0 0
    

### 用例2

    
    
    4 4
    2 1 2 3
    0 1 0 0
    0 1 0 0
    0 1 0 0
    

### 用例3

    
    
    3 3
    2 1 0
    0 1 3
    0 0 2
    

### 用例4

    
    
    3 3
    2 0 0
    1 1 0
    0 0 2
    

### 用例5

    
    
    5 5
    2 1 0 0 3
    0 1 2 1 0
    0 3 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    

### 用例6

    
    
    3 4
    2 1 0 3
    0 1 2 1
    0 3 0 0
    

### 用例7

    
    
    5 4
    2 1 0 0
    0 1 2 1
    0 3 0 0
    0 0 0 0
    3 0 0 0
    

### 用例8

    
    
    5 4
    2 1 0 0
    0 1 2 1
    0 3 0 0
    1 1 1 1
    3 0 0 0
    

### 用例9

    
    
    5 5
    2 1 0 0 3
    0 1 2 1 0
    0 3 0 0 0
    0 0 0 0 0
    0 0 0 0 0
    

### 用例10

    
    
    6 6
    2 1 0 0 0 3
    0 1 2 1 0 0
    0 3 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    3 0 0 0 0 0
    

