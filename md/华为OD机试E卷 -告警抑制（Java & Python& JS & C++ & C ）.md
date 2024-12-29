## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

告警抑制，是指高优先级告警抑制低优先级告警的规则。高优先级告警产生后，低优先级告警不再产生。请根据原始告警列表和告警抑制关系，给出实际产生的告警列表。

  * 不会出现循环抑制的情况。
  * 告警不会传递，比如A->B,B->C，这种情况下A不会直接抑制C。但被抑制的告警仍然可以抑制其他低优先级告警。

## 输入描述

第一行为数字N，表示告警抑制关系个数，0 ≤ N ≤ 120  
接下来N行，每行是由空格分隔的两个告警ID，例如: id1 id2，表示id1抑制id2，告警ID的格式为：

> 大写字母+0个或者1个数字

最后一行为告警产生列表，列表长度[1,100]

## 输出描述

真实产生的告警列表

##### 备注

告警ID之间以单个空格分隔

## 示例1

输入

    
    
    2
    A B
    B C
    A B C D E
    

输出

    
    
    A D E
    

说明

> A抑制了B，B抑制了C，最后实际的告警为A D E

## 示例2

输入

    
    
    4
    F G
    C B
    A G
    A0 A
    A B C D E
    

输出

    
    
    A C D E
    

说明

> 第一个告警A，能够抑制它的只有A0，而当前告警列表中没有A0，因此告警A可以正常发生  
>  第二个告警B，能够抑制它的只有C，而当前告警列表中有C，因此告警B被抑制，不可以发生  
>  第三个告警C，没有能抑制它的告警，因此正常发生  
>  第四个告警D，没有能抑制它的告警，因此正常发生  
>  第五个告警E，没有能抑制它的告警，因此正常发生

## 解题思路

#### 题意理解

  1. **告警抑制规则** ：我们有一组抑制规则，每个规则定义了一个“高优先级”告警和一个“低优先级”告警的关系。比如规则`A B`表示告警`A`会抑制告警`B`。

  2. **非循环抑制** ：题目中说明不会出现循环抑制，即不会出现`A`抑制`B`，`B`抑制`A`的情况。这样可以避免复杂的循环判断问题。

  3. **无传递抑制** ：例如，`A -> B`且`B -> C`的情况下，`A`不会直接抑制`C`。但是如果`B`因为`A`的存在被抑制了，`B`将不会再去抑制`C`。

  4. **原始告警列表** ：最后一行输入的是原始的告警列表，按照出现的顺序给出，这些告警可能会被抑制，产生实际的告警列表。

#### 解题步骤

  1. **构建抑制规则的映射关系** ：使用一个数据结构（如字典）记录每个告警的抑制关系，这样可以快速查询某个告警是否会被另一个告警抑制。

  2. **判断告警是否被抑制** ：遍历原始告警列表，对于每个告警，检查在抑制它的告警中是否有已经出现的高优先级告警。如果有，则当前告警被抑制，不加入最终结果；如果没有，则加入最终结果。

  3. **输出实际产生的告警列表** ：输出所有未被抑制的告警，按照原始告警列表中的顺序。

#### 示例分析

##### 示例1

输入：

    
    
    2
    A B
    B C
    A B C D E
    

  * 抑制关系为：

    * `A`抑制`B`
    * `B`抑制`C`
  * 过程分析：

    * `A`未被任何告警抑制，加入实际产生的告警列表。
    * `B`被`A`抑制，抑制生效，不加入实际产生的告警列表。
    * `C`被`B`抑制，由于`B`已被`A`抑制，因此`C`也不加入实际产生的告警列表。
    * `D`和`E`未被任何告警抑制，加入实际产生的告警列表。
  * 输出结果为：`A D E`

##### 示例2

输入：

    
    
    4
    F G
    C B
    A G
    A0 A
    A B C D E
    

  * 抑制关系为：

    * `F`抑制`G`
    * `C`抑制`B`
    * `A`抑制`G`
    * `A0`抑制`A`
  * 过程分析：

    * `A`未被`A0`抑制（`A0`不在告警列表中），因此`A`加入实际产生的告警列表。
    * `B`被`C`抑制，而`C`在告警列表中，因此`B`不加入实际产生的告警列表。
    * `C`未被任何告警抑制，加入实际产生的告警列表。
    * `D`和`E`未被任何告警抑制，加入实际产生的告警列表。
  * 输出结果为：`A C D E`

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            // 输入告警抑制关系的数量
            int ruleCount = Integer.parseInt(sc.nextLine());
    
            // 构建抑制关系图，用于记录每个告警抑制的其他告警
            HashMap<String, HashSet<String>> suppressMap = new HashMap<>();
            for (int i = 0; i < ruleCount; i++) {
                // 读取一条抑制规则，格式为"抑制告警 被抑制告警"
                String[] rule = sc.nextLine().split(" ");
                String suppressor = rule[0]; // 抑制告警
                String suppressed = rule[1]; // 被抑制告警
    
                // 将抑制关系加入到抑制关系图中
                suppressMap.computeIfAbsent(suppressor, k -> new HashSet<>()).add(suppressed);
            }
    
            // 读取告警产生列表
            String[] alerts = sc.nextLine().split(" ");
    
            // 转换告警列表为Set，方便快速查找某告警是否产生
            HashSet<String> activeAlerts = new HashSet<>(Arrays.asList(alerts));
    
            // 存储被抑制的告警ID
            HashSet<String> suppressedAlerts = new HashSet<>();
            for (String alert : alerts) {
                // 检查当前告警是否抑制其他告警
                if (suppressMap.containsKey(alert)) {
                    // 遍历被该告警抑制的所有告警
                    for (String suppressed : suppressMap.get(alert)) {
                        // 如果被抑制的告警在产生列表中，则标记为被抑制
                        if (activeAlerts.contains(suppressed)) {
                            suppressedAlerts.add(suppressed);
                        }
                    }
                }
            }
    
            // 构建实际产生的告警列表
            List<String> finalAlerts = new ArrayList<>();
            for (String alert : alerts) {
                // 如果该告警未被抑制，则加入结果列表
                if (!suppressedAlerts.contains(alert)) {
                    finalAlerts.add(alert);
                }
            }
    
            // 输出最终实际产生的告警列表，按空格分隔
            System.out.println(String.join(" ", finalAlerts));
        }
    }
    
    

## Python

    
    
    # 导入必要的模块
    import sys
    
    # 从标准输入读取数据
    input = sys.stdin.read
    data = input().splitlines()
    
    # 输入告警抑制关系的数量
    rule_count = int(data[0])
    
    # 构建抑制关系字典，用于记录每个告警抑制的其他告警
    suppress_map = {}
    for i in range(1, rule_count + 1):
        # 读取一条抑制规则，格式为"抑制告警 被抑制告警"
        suppressor, suppressed = data[i].split()
        
        # 将抑制关系加入到抑制关系字典中
        if suppressor not in suppress_map:
            suppress_map[suppressor] = set()
        suppress_map[suppressor].add(suppressed)
    
    # 读取告警产生列表
    alerts = data[rule_count + 1].split()
    
    # 转换告警列表为集合，方便快速查找某告警是否产生
    active_alerts = set(alerts)
    
    # 存储被抑制的告警ID
    suppressed_alerts = set()
    for alert in alerts:
        # 检查当前告警是否抑制其他告警
        if alert in suppress_map:
            # 遍历被该告警抑制的所有告警
            for suppressed in suppress_map[alert]:
                # 如果被抑制的告警在产生列表中，则标记为被抑制
                if suppressed in active_alerts:
                    suppressed_alerts.add(suppressed)
    
    # 构建实际产生的告警列表
    final_alerts = [alert for alert in alerts if alert not in suppressed_alerts]
    
    # 输出最终实际产生的告警列表，按空格分隔
    print(" ".join(final_alerts))
    
    

## JavaScript

    
    
    const readline = require("readline");
    
    // 创建接口以读取输入
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    let input = [];
    rl.on("line", (line) => input.push(line));
    
    rl.on("close", () => {
      // 输入告警抑制关系的数量
      const ruleCount = parseInt(input[0]);
    
      // 构建抑制关系图，用于记录每个告警抑制的其他告警
      const suppressMap = {};
      for (let i = 1; i <= ruleCount; i++) {
        // 读取一条抑制规则，格式为"抑制告警 被抑制告警"
        const [suppressor, suppressed] = input[i].split(" ");
    
        // 将抑制关系加入到抑制关系图中
        if (!suppressMap[suppressor]) {
          suppressMap[suppressor] = new Set();
        }
        suppressMap[suppressor].add(suppressed);
      }
    
      // 读取告警产生列表
      const alerts = input[ruleCount + 1].split(" ");
    
      // 转换告警列表为Set，方便快速查找某告警是否产生
      const activeAlerts = new Set(alerts);
    
      // 存储被抑制的告警ID
      const suppressedAlerts = new Set();
      for (const alert of alerts) {
        // 检查当前告警是否抑制其他告警
        if (suppressMap[alert]) {
          for (const suppressed of suppressMap[alert]) {
            if (activeAlerts.has(suppressed)) {
              suppressedAlerts.add(suppressed);
            }
          }
        }
      }
    
      // 构建实际产生的告警列表
      const finalAlerts = alerts.filter((alert) => !suppressedAlerts.has(alert));
    
      // 输出最终实际产生的告警列表，按空格分隔
      console.log(finalAlerts.join(" "));
    });
    
    

## C++

    
    
    #include <iostream>
    #include <unordered_map>
    #include <unordered_set>
    #include <vector>
    #include <sstream>
    using namespace std;
    
    int main() {
        int ruleCount;
        cin >> ruleCount;
        cin.ignore();
    
        // 构建抑制关系图，用于记录每个告警抑制的其他告警
        unordered_map<string, unordered_set<string>> suppressMap;
        for (int i = 0; i < ruleCount; i++) {
            string suppressor, suppressed;
            cin >> suppressor >> suppressed;
            suppressMap[suppressor].insert(suppressed);
        }
        cin.ignore();
    
        // 读取告警产生列表
        string line;
        getline(cin, line);
        istringstream iss(line);
        vector<string> alerts;
        string alert;
        while (iss >> alert) {
            alerts.push_back(alert);
        }
    
        // 转换告警列表为Set，方便快速查找某告警是否产生
        unordered_set<string> activeAlerts(alerts.begin(), alerts.end());
    
        // 存储被抑制的告警ID
        unordered_set<string> suppressedAlerts;
        for (const auto& alert : alerts) {
            if (suppressMap.count(alert)) {
                for (const auto& suppressed : suppressMap[alert]) {
                    if (activeAlerts.count(suppressed)) {
                        suppressedAlerts.insert(suppressed);
                    }
                }
            }
        }
    
        // 构建实际产生的告警列表
        vector<string> finalAlerts;
        for (const auto& alert : alerts) {
            if (!suppressedAlerts.count(alert)) {
                finalAlerts.push_back(alert);
            }
        }
    
        // 输出最终实际产生的告警列表，按空格分隔
        for (size_t i = 0; i < finalAlerts.size(); i++) {
            if (i > 0) cout << " ";
            cout << finalAlerts[i];
        }
        cout << endl;
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <string.h>
    
    #define MAX_RULES 100         // 最大抑制规则数量
    #define MAX_ALERTS 100        // 最大告警数量
    #define MAX_NAME_LEN 50       // 最大告警名称长度
    
    // 定义抑制规则的存储结构
    char suppressors[MAX_RULES][MAX_NAME_LEN];  // 存储每个抑制告警
    char suppressed[MAX_RULES][MAX_NAME_LEN];   // 存储每个被抑制告警
    int ruleCount = 0;                          // 记录抑制规则的实际数量
    
    // 存储告警列表及其数量
    char alerts[MAX_ALERTS][MAX_NAME_LEN];      // 存储输入的告警列表
    int alertCount = 0;                         // 实际告警数量
    
    // 读取一个抑制规则并存储到 suppressors 和 suppressed 数组中
    void addSuppressionRule(char *suppressor, char *suppressedAlert) {
        strcpy(suppressors[ruleCount], suppressor);
        strcpy(suppressed[ruleCount], suppressedAlert);
        ruleCount++;
    }
    
    // 检查某个告警是否被另一个告警抑制
    int isSuppressed(char *alert) {
        for (int i = 0; i < ruleCount; i++) {
            // 如果 alert 被 suppressors[i] 抑制并且 suppressors[i] 在告警列表中
            for (int j = 0; j < alertCount; j++) {
                if (strcmp(suppressors[i], alerts[j]) == 0 && strcmp(suppressed[i], alert) == 0) {
                    return 1;  // 被抑制
                }
            }
        }
        return 0;  // 未被抑制
    }
    
    int main() {
        int ruleCountInput;
        
        // 输入抑制规则数量
        scanf("%d", &ruleCountInput);
        getchar();  // 读取换行符
    
        // 逐行读取每个抑制规则
        for (int i = 0; i < ruleCountInput; i++) {
            char suppressor[MAX_NAME_LEN], suppressedAlert[MAX_NAME_LEN];
            scanf("%s %s", suppressor, suppressedAlert);
            addSuppressionRule(suppressor, suppressedAlert);  // 存储抑制规则
        }
    
        // 读取告警产生列表，按空格分隔
        char inputLine[1000];
        getchar();  // 清除上一个输入后的换行符
        fgets(inputLine, sizeof(inputLine), stdin);
        
        // 将告警列表拆分并存储到 alerts 数组中
        char *token = strtok(inputLine, " \n");
        while (token != NULL) {
            strcpy(alerts[alertCount++], token);
            token = strtok(NULL, " \n");
        }
    
        // 输出未被抑制的告警列表
        int first = 1;
        for (int i = 0; i < alertCount; i++) {
            if (!isSuppressed(alerts[i])) {  // 检查告警是否被抑制
                if (!first) printf(" ");
                printf("%s", alerts[i]);
                first = 0;
            }
        }
        printf("\n");
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

#### 完整用例

##### 用例1

    
    
    2
    A B
    B C
    A B C D E
    

##### 用例2

    
    
    4
    A B
    B C
    C D
    E F
    A B C D E F
    

##### 用例3

    
    
    4
    A B
    B C
    D E
    E F
    A B C D E
    

##### 用例4

    
    
    4
    A B
    B C
    C D
    D E
    A B C D E
    

##### 用例5

    
    
    2
    A B
    C D
    A B C D E
    

##### 用例6

    
    
    1
    A B
    B C D E
    

##### 用例7

    
    
    3
    A B
    B C
    C D
    A B C D E
    

##### 用例8

    
    
    4
    A B
    B C
    C D
    D E
    A B C D E
    

##### 用例9

    
    
    5
    A B
    B C
    C D
    D E
    E F
    A B C D E F
    

##### 用例10

    
    
    2
    A B
    C D
    A C D
    

