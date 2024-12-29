## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

一个有N个选手参加比赛，选手编号为1~N（3<=N<=100），有M（3<=M<=10）个评委对选手进行打分。

打分规则为每个评委对选手打分，最高分10分，最低分1分。

请计算得分最多的3位选手的编号。

如果得分相同，则得分高分值最多的选手排名靠前

(10分数量相同，则比较9分的数量，以此类推，用例中不会出现多个选手得分完全相同的情况)。

​

## 输入描述

第一行为半角逗号分割的两个正整数，第一个数字表示M（3<=M<=10）个评委，第二个数字表示N（3<=N<=100）个选手。

第2到M+1行是半角逗号分割的整数序列，表示评委为每个选手的打分，0号下标数字表示1号选手分数，1号下标数字表示2号选手分数，依次类推。

## 输出描述

选手前3名的编号。

**注：**若输入为异常，输出-1，如M、N、打分不在范围内。

## 示例1

输入

    
    
    4,5
    10,6,9,7,6
    9,10,6,7,5
    8,10,6,5,10
    9,10,8,4,9
    

输出

    
    
    2,1,5
    

说明

> 第一行代表有4个评委，5个选手参加比赛
>
> 矩阵代表是4*5，每个数字是选手的编号，每一行代表一个评委对选手的打分排序，
>
> 2号选手得分36分排第1，1号选手36分排第2，5号选手30分(2号10分值有3个，1号10分值只有1个，所以2号排第一)

## 示例2

输入

    
    
    2,5
    7,3,5,4,2
    8,5,4,4,3
    

输出

    
    
    -1
    

说明

> 只有2个评委，要求最少为3个评委

## 示例3

输入

    
    
    4,2
    8,5
    5,6
    10,4
    8,9
    

输出

    
    
    -1
    

说明

> 只有2名选手参加，要求最少为3名

## 示例4

输入

    
    
    4,5
    11,6,9,7,8
    9,10,6,7,8
    8,10,6,9,7
    9,10,8,6,7
    

输出

    
    
    -1
    

说明

> 第一个评委给第一个选手打分11，无效分数

## 解题思路

#### 题目题意解析

题目要求我们从一组评委对多个选手的评分中，计算得分最高的三个选手的编号。具体规则如下：

  1. **选手和评委数量** ：

     * 有 **N个选手** ，编号为1到N，且N的范围在3到100之间。
     * 有 **M个评委** ，M的范围在3到10之间。
  2. **打分规则** ：

     * 每个评委给每个选手打分，分数为 **1到10** 的整数。
     * 每个选手最终得分是所有评委对他的评分之和。
  3. **排名规则** ：

     * 我们需要计算得分最多的3位选手的编号。
     * 如果有选手得分相同，优先比较高分（例如：10分的数量最多的选手排在前面；如果10分数量相同，则比较9分的数量，依此类推）。
     * 题目保证不存在完全相同的得分情况，即每个选手的分数分布不会完全相同。
  4. **异常情况** ：

     * 如果输入中的 **M** 或 **N** 不在题目要求的范围内，或者打分不是1到10之间的有效分数，则输出 `-1` 表示无效。

#### 示例解析

##### 示例 1:

输入：

    
    
    4,5
    10,6,9,7,6
    9,10,6,7,5
    8,10,6,5,10
    9,10,8,4,9
    

解析：

  * **第一行表示有4个评委，5个选手** 。
  * 各个评委对选手的打分矩阵是：
    
        10  6   9   7   6
     9  10  6   7   5
     8  10  6   5  10
     9  10  8   4   9
    

  * 计算每个选手的总分： 
    * 1号选手：10 + 9 + 8 + 9 = 36
    * 2号选手：6 + 10 + 10 + 10 = 36
    * 3号选手：9 + 6 + 6 + 8 = 29
    * 4号选手：7 + 7 + 5 + 4 = 23
    * 5号选手：6 + 5 + 10 + 9 = 30
  * 得分排名前3位的选手分别是：**2号、1号、5号** （2号选手的10分数量最多，因此排在1号前面）。

输出：

    
    
    2,1,5
    

## Java

    
    
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Scanner;
    import java.util.StringJoiner;
    import java.util.stream.Stream;
    
    public class Main {
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in).useDelimiter("[,\n]");
        int m = sc.nextInt(); // 评委数量
        int n = sc.nextInt(); // 选手数量
        if (m < 3 || m > 10 || n < 3 || n > 100) { // 判断输入是否合法
          System.out.println("-1");
          return;
        }
        int[][] scores = new int[m][n]; // 评委打分
        for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
            scores[i][j] = sc.nextInt();
            if (scores[i][j] > 10 || scores[i][j] < 1) { // 判断队员得分是否合法
              System.out.println("-1");
              return;
            }
          }
        }
        HashMap<Integer, Integer[]> players = new HashMap<>(); // 选手编号和得分
        for (int j = 0; j < n; j++) {
          Integer[] playerScores = new Integer[m];
          for (int i = 0; i < m; i++) {
            playerScores[i] = scores[i][j];
          }
          Arrays.sort(playerScores, (a, b) -> b - a); // 将每个队员的得分降序排序
          players.put(j, playerScores);
        }
        StringJoiner sj = new StringJoiner(",");
        players.entrySet().stream()
            .sorted(
                (a, b) -> {
                  Integer[] playerA = a.getValue(); // 选手A的得分
                  Integer[] playerB = b.getValue(); // 选手B的得分
                  int sumA = Stream.of(playerA).mapToInt(Integer::intValue).sum(); // 计算总分
                  int sumB = Stream.of(playerB).mapToInt(Integer::intValue).sum();
                  if (sumA != sumB) { // 按总分降序排列
                    return sumB - sumA;
                  }
                  for (int i = 0; i < m; i++) {
                    if (playerA[i] == playerB[i]) continue;
                    return playerB[i] - playerA[i]; // 按最高分降序排列
                  }
                  return 0;
                })
            .limit(3)
            .forEach(p -> sj.add(p.getKey() + 1 + "")); // 将前三名的选手编号加入StringJoiner
        System.out.println(sj.toString()); // 输出前三名的选手编号
      }
    }
    
    
    

## Python

    
    
    import sys
    
    m, n = map(int, input().split(","))
    scores = [list(map(int, input().split(","))) for _ in range(m)]
    if m < 3 or m > 10 or n < 3 or n > 100:
        print("-1")
        sys.exit()
        
    for i in range(m):
        for j in range(n):
            if scores[i][j] > 10 or scores[i][j] < 1:
                print("-1")
                sys.exit()
                
    players = {}
                
    for j in range(n):
        playerScores = [row[j] for row in scores]
        playerScores.sort(reverse=True)
        players[j] = playerScores
        
    result = sorted(players.items(), key=lambda x: (sum(x[1]), x[1]), reverse=True)[:3]
    result = [p[0]+1 for p in result]
    result = ','.join(map(str, result))
    
    print(result)
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
     
    
    let m, n;
    let scores = [];
    
    rl.on('line', (line) => {
      if (!m && !n) {
        [m, n] = line.split(',').map(Number);
      } else {
        scores.push(line.split(',').map(Number));
      }
    }).on('close', () => {
     
    
    if (m < 3 || m > 10 || n < 3 || n > 100) {
        console.log("-1");
        rl.close();
        return;
      }
      
      
       for (let i = 0; i < m; i++) {
           
          for (let j = 0; j < n; j++) {
            if (scores[i][j] > 10 || scores[i][j] < 1) {
              console.log("-1");
              rl.close();
              return;
            }
          }
        }
        
        let players = new Map();
        
        for (let j = 0; j < n; j++) {
          let playerScores = scores.map(row => row[j]);
          playerScores.sort((a, b) => b - a);
          players.set(j, playerScores);
        }
        
        let result = Array.from(players.entries())
          .sort((a, b) => {
            let playerA = a[1];
            let playerB = b[1];
            
            let sumA = playerA.reduce((sum, score) => sum + score, 0);
            let sumB = playerB.reduce((sum, score) => sum + score, 0);
            
            if (sumA !== sumB) {
              return sumB - sumA;
            }
            
            for (let i = 0; i < m; i++) {
              if (playerA[i] === playerB[i]) continue;
              return playerB[i] - playerA[i];
            }
            
            return 0;
          })
          .slice(0, 3)
          .map(p => p[0] + 1)
          .join(',');
          
        console.log(result);
    });
    
    
    
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <map>
    #include <algorithm>
    using namespace std;
    
    int main() {
        int m = 0, n = 0;
        vector<vector<int>> scores;
    
        string line;
        while (getline(cin, line)) {
            if (m == 0 && n == 0) {
                string delimiter = ",";
                size_t pos = 0;
                string token;
                while ((pos = line.find(delimiter)) != string::npos) {
                    token = line.substr(0, pos);
                    m = stoi(token);
                    line.erase(0, pos + delimiter.length());
                }
                n = stoi(line);
            } else {
                vector<int> row;
                string delimiter = ",";
                size_t pos = 0;
                string token;
                while ((pos = line.find(delimiter)) != string::npos) {
                    token = line.substr(0, pos);
                    row.push_back(stoi(token));
                    line.erase(0, pos + delimiter.length());
                }
                row.push_back(stoi(line));
                scores.push_back(row);
            }
        }
    
        if (m < 3 || m > 10 || n < 3 || n > 100) {
            cout << "-1" << endl;
            return 0;
        }
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (scores[i][j] > 10 || scores[i][j] < 1) {
                    cout << "-1" << endl;
                    return 0;
                }
            }
        }
    
        map<int, vector<int>> players;
    
        for (int j = 0; j < n; j++) {
            vector<int> playerScores;
            for (int i = 0; i < m; i++) {
                playerScores.push_back(scores[i][j]);
            }
            sort(playerScores.begin(), playerScores.end(), greater<int>());
            players[j] = playerScores;
        }
    
        vector<pair<int, vector<int>>> result;
        for (auto it = players.begin(); it != players.end(); it++) {
            result.push_back(*it);
        }
    
        sort(result.begin(), result.end(), [](const pair<int, vector<int>>& a, const pair<int, vector<int>>& b) {
            int sumA = 0, sumB = 0;
            for (int i = 0; i < a.second.size(); i++) {
                sumA += a.second[i];
                sumB += b.second[i];
            }
            if (sumA != sumB) {
                return sumB < sumA;
            }
            for (int i = 0; i < a.second.size(); i++) {
                if (a.second[i] != b.second[i]) {
                    return b.second[i] < a.second[i];
                }
            }
            return false;
        });
    
        vector<int> topPlayers;
        for (int i = 0; i < 3; i++) {
            topPlayers.push_back(result[i].first + 1);
        }
    
        for (int i = 0; i < topPlayers.size(); i++) {
            cout << topPlayers[i];
            if (i != topPlayers.size() - 1) {
                cout << ",";
            }
        }
        cout << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    
    #define MAX_M 10
    #define MAX_N 100
    
    int m, n;
    int scores[MAX_M][MAX_N];
    
    // 比较函数，用于排序
    int compare(const void *a, const void *b) {
        return (*(int *)b - *(int *)a);
    }
    
    // 比较两个选手的得分情况，按照总分和每一分值逐级比较
    int compare_players(const void *a, const void *b) {
        int idx_a = *(int *)a;
        int idx_b = *(int *)b;
        
        int sum_a = 0, sum_b = 0;
        for (int i = 0; i < m; i++) {
            sum_a += scores[i][idx_a];
            sum_b += scores[i][idx_b];
        }
        
        if (sum_a != sum_b) return sum_b - sum_a; // 先按总分排序
        
        // 如果总分相同，按从高到低逐级分数排序
        int sorted_a[MAX_M], sorted_b[MAX_M];
        for (int i = 0; i < m; i++) {
            sorted_a[i] = scores[i][idx_a];
            sorted_b[i] = scores[i][idx_b];
        }
        qsort(sorted_a, m, sizeof(int), compare);
        qsort(sorted_b, m, sizeof(int), compare);
        
        for (int i = 0; i < m; i++) {
            if (sorted_a[i] != sorted_b[i]) {
                return sorted_b[i] - sorted_a[i];
            }
        }
        
        return 0;
    }
    
    // 主函数
    int main() {
        // 读取M和N
        if (scanf("%d,%d", &m, &n) != 2 || m < 3 || m > 10 || n < 3 || n > 100) {
            printf("-1\n");
            return 0;
        }
        
        // 读取评分
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (scanf("%d", &scores[i][j]) != 1 || scores[i][j] < 1 || scores[i][j] > 10) {
                    printf("-1\n");
                    return 0;
                }
                if (j < n - 1) {
                    getchar(); // 处理逗号
                }
            }
        }
        
        // 存储选手编号，准备排序
        int players[MAX_N];
        for (int i = 0; i < n; i++) {
            players[i] = i;
        }
        
        // 对选手进行排序
        qsort(players, n, sizeof(int), compare_players);
        
        // 输出前3名选手编号（从1开始）
        for (int i = 0; i < 3; i++) {
            if (i > 0) printf(",");
            printf("%d", players[i] + 1);
        }
        printf("\n");
        
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

#### 完整用例

##### 用例1

    
    
    4,5
    10,6,9,7,6
    9,10,6,7,5
    8,10,6,5,10
    9,10,8,4,9
    

##### 用例2

    
    
    2,5
    7,3,5,4,2
    8,5,4,4,3
    

##### 用例3

    
    
    4,2
    8,5
    5,6
    10,4
    8,9
    

##### 用例4

    
    
    4,5
    11,6,9,7,8
    9,10,6,7,8
    8,10,6,9,7
    9,10,8,6,7
    

##### 用例5

    
    
    3,4
    10,9,8,7
    6,5,4,3
    2,1,10,9
    

##### 用例6

    
    
    5,6
    8,9,10,7,6,5
    9,8,7,6,5,4
    6,7,8,9,10,5
    5,6,7,8,9,10
    4,5,6,7,8,9
    

##### 用例7

    
    
    4,8
    10,10,10,10,10,10,10,10
    9,9,9,9,9,9,9,9
    8,8,8,8,8,8,8,8
    7,7,7,7,7,7,7,7
    

##### 用例8

    
    
    6,5
    10,10,10,10,10
    9,9,9,9,9
    8,8,8,8,8
    7,7,7,7,7
    6,6,6,6,6
    5,5,5,5,5
    

##### 用例9

    
    
    4,5
    -1,10,9,7,6
    9,10,6,7,5
    8,10,6,5,10
    9,10,8,4,9
    

##### 用例10

    
    
    2,3
    10,10,10
    9,9,9
    

