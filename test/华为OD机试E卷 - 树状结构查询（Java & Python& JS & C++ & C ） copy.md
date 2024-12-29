## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

通常使用多行的节点、父节点表示一棵树，比如

西安 陕西  
陕西 中国  
江西 中国  
中国 亚洲  
泰国 亚洲

输入一个节点之后，请打印出来树中他的所有下层节点

## 输入描述

第一行输入行数，下面是多行数据，每行以空格区分节点和父节点

接着是查询节点

## 输出描述

输出查询节点的所有下层节点。以字典序排序

## 示例1

输入

    
    
    5
    b a
    c a
    d c
    e c
    f d
    c
    

输出

    
    
    d
    e
    f
    

说明

> ## 解题思路

这个题目描述了一棵树的结构，并要求我们找到一个给定节点的所有下层节点（即该节点的所有子节点及其后代节点）。

### 示例解释

**输入** ：

    
    
    5
    b a
    c a
    d c
    e c
    f d
    c
    

**解析** ：

  * 树结构的表示： 
    * `b` 的父节点是 `a`
    * `c` 的父节点是 `a`
    * `d` 的父节点是 `c`
    * `e` 的父节点是 `c`
    * `f` 的父节点是 `d`
  * 查询节点为 `c`，我们需要找出所有 `c` 的下层节点。

根据上述结构，我们可以构建以下树：

    
    
            a
           / \
          b   c
             / \
            d   e
           /
          f
    

**查询节点** ：`c`

**输出结果** ：

  * `c` 的直接下层节点是 `d` 和 `e`。
  * `d` 的下层节点是 `f`。
  * 因此，`c` 的所有下层节点为：`d, e, f`。

字典序排序后，输出结果为：

    
    
    d
    e
    f
    

  3. 

## Java

    
    
    import java.util.*;
    
    public class Main {
      public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        int n = sc.nextInt(); // 输入行数
    
        HashMap<String, HashSet<String>> tree = new HashMap<>(); // 创建一个HashMap用于存储树的关系
    
        // 读取输入的树的关系，并将子节点和父节点存入HashMap中
        for (int i = 0; i < n; i++) {
          String childNode = sc.next(); // 子节点
          String parentNode = sc.next(); // 父节点
    
          tree.computeIfAbsent(parentNode, k -> new HashSet<>()).add(childNode); // 将子节点添加到父节点的集合中
        }
    
        String targetNode = sc.next(); // 输入要查询的节点
    
        if (!tree.containsKey(targetNode)) { // 如果树中不包含要查询的节点，则输出空行并结束程序
          System.out.println("");
          return;
        }
    
        LinkedList<String> queue = new LinkedList<>(tree.get(targetNode)); // 创建一个队列，用于存储要遍历的节点
    
        ArrayList<String> result = new ArrayList<>(); // 创建一个ArrayList，用于存储查询节点的所有下层节点
    
        // 遍历队列，将节点添加到结果集中，并将该节点的子节点添加到队列中
        while (!queue.isEmpty()) {
          String node = queue.removeFirst(); // 从队列中取出节点
          result.add(node); // 将节点添加到结果集中
    
          if (tree.containsKey(node)) { // 如果节点在树中有子节点，则将子节点添加到队列中
            queue.addAll(tree.get(node));
          }
        }
    
        result.sort(String::compareTo); // 对结果集进行排序
    
        result.forEach(System.out::println); // 打印结果集中的每个节点
      }
    }
    
    

## Python

    
    
    n = int(input())  # 输入行数
    
    tree = {}  # 创建一个字典用于存储树的关系
    
    # 读取输入的树的关系，并将子节点和父节点存入字典中
    for _ in range(n):
        childNode, parentNode = input().split()  # 子节点和父节点
    
        if parentNode not in tree:
            tree[parentNode] = set()  # 如果父节点不在字典中，则创建一个空集合
    
        tree[parentNode].add(childNode)  # 将子节点添加到父节点的集合中
    
    targetNode = input()  # 输入要查询的节点
    
    if targetNode not in tree:  # 如果字典中不包含要查询的节点，则输出空行并结束程序
        print("")
        exit()
    
    queue = list(tree[targetNode])  # 创建一个队列，用于存储要遍历的节点
    
    result = []  # 创建一个列表，用于存储查询节点的所有下层节点
    
    # 遍历队列，将节点添加到结果集中，并将该节点的子节点添加到队列中
    while queue:
        node = queue.pop(0)  # 从队列中取出节点
        result.append(node)  # 将节点添加到结果集中
    
        if node in tree:  # 如果节点在字典中有子节点，则将子节点添加到队列中
            queue.extend(tree[node])
    
    result.sort()  # 对结果集进行排序
    
    for node in result:  # 打印结果集中的每个节点
        print(node)
    
    

## JavaScript

    
    
    const readline = require("readline");
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
    
    const lines = []; // 存储输入的所有行数据
    let n; // 树的行数
    
    rl.on("line", (line) => { // 监听每一行的输入
      lines.push(line); // 将输入的行添加到lines数组中
    
      if (lines.length == 1) { // 如果lines数组中只有一行数据，表示树的行数
        n = parseInt(lines[0]); // 将树的行数转换为整数并赋值给n
      }
    
      if (n && lines.length === n + 2) { // 当树的行数和输入的行数匹配时，进行处理
        lines.shift(); // 移除第一行树的行数
        const target = lines.pop(); // 弹出最后一行作为查询的节点
    
        const tree = {}; // 存储树的结构，使用对象表示，key为父节点，value为子节点的集合
        for (let str of lines) { // 遍历除了树的行数和查询节点之外的行
          const [node, parent] = str.split(" "); // 将每一行以空格分割成节点和父节点
          if (!tree[parent]) tree[parent] = new Set(); // 如果父节点不存在于树结构中，则创建一个新的集合
          tree[parent].add(node); // 将节点添加到父节点的集合中
        }
    
        if (!tree[target]) return console.log(""); // 如果查询的节点不存在于树结构中，直接输出空字符串
    
        const queue = [...tree[target]]; // 将查询的节点的子节点集合放入队列中
    
        const result = []; // 存储查询节点的所有下层节点
        while (queue.length > 0) { // 当队列不为空时，进行循环
          const node = queue.shift(); // 弹出队列中的第一个节点
          result.push(node); // 将节点添加到结果数组中
    
          if (tree[node]) { // 如果节点存在子节点
            queue.push(...tree[node]); // 将子节点添加到队列中
          }
        }
    
        result.sort().forEach((v) => console.log(v)); // 对结果数组进行字典序排序，并逐行输出
    
       }
    });
    
    

## C++

    
    
    #include <iostream>
    #include <unordered_map>
    #include <unordered_set>
    #include <queue>
    #include <vector>
    #include <algorithm>
    using namespace std;
    
    int main() {
      int n;
      cin >> n; // 输入行数
    
      unordered_map<string, unordered_set<string>> tree; // 创建一个unordered_map用于存储树的关系
    
      // 读取输入的树的关系，并将子节点和父节点存入unordered_map中
      for (int i = 0; i < n; i++) {
        string childNode, parentNode;
        cin >> childNode >> parentNode; // 子节点和父节点
    
        tree[parentNode].insert(childNode); // 将子节点添加到父节点的集合中
      }
    
      string targetNode;
      cin >> targetNode; // 输入要查询的节点
    
      if (tree.find(targetNode) == tree.end()) { // 如果树中不包含要查询的节点，则输出空行并结束程序
        cout << endl;
        return 0;
      }
    
      queue<string> q;
      for (const string& node : tree[targetNode]) {
        q.push(node); // 将要遍历的节点添加到队列中
      }
    
      vector<string> result; // 创建一个vector，用于存储查询节点的所有下层节点
    
      // 遍历队列，将节点添加到结果集中，并将该节点的子节点添加到队列中
      while (!q.empty()) {
        string node = q.front(); // 从队列中取出节点
        q.pop();
    
        result.push_back(node); // 将节点添加到结果集中
    
        if (tree.find(node) != tree.end()) { // 如果节点在树中有子节点，则将子节点添加到队列中
          for (const string& child : tree[node]) {
            q.push(child);
          }
        }
      }
    
      sort(result.begin(), result.end()); // 对结果集进行排序
    
      for (const string& node : result) {
        cout << node << endl; // 打印结果集中的每个节点
      }
    
      return 0;
    }
    
    
    

## C语言

    
    
    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>
    
    #define MAX_NODES 100
    #define MAX_NAME_LEN 100
    
    // 定义一个结构体来表示树的关系，每个父节点及其子节点
    struct Tree {
        char parent[MAX_NAME_LEN];  // 父节点名称
        char child[MAX_NAME_LEN];   // 子节点名称
    };
    
    // 定义一个二维数组来存储每个节点的子节点
    char children[MAX_NODES][MAX_NAME_LEN][MAX_NAME_LEN]; // 每个节点的子节点
    int children_count[MAX_NODES];  // 记录每个节点有多少个子节点
    
    // 存储所有节点的名称，避免查找时每次都从输入的字符中查找
    char nodes[MAX_NODES][MAX_NAME_LEN]; 
    int node_count = 0;  // 节点总数
    
    // 存储查询结果的数组
    char result[MAX_NODES][MAX_NAME_LEN];
    int result_count = 0;  // 记录结果集中节点的个数
    
    // 查找节点名称是否存在，如果存在返回索引，不存在则添加新节点并返回新索引
    int find_or_add_node(char *name) {
        for (int i = 0; i < node_count; i++) {
            if (strcmp(nodes[i], name) == 0) {
                return i;  // 如果找到了，返回该节点的索引
            }
        }
        strcpy(nodes[node_count], name);  // 如果没有找到，添加新节点
        return node_count++;  // 返回新节点的索引，并增加节点总数
    }
    
    // 使用深度优先搜索（DFS）遍历树，收集目标节点的所有子节点
    void dfs(int index) {
        for (int i = 0; i < children_count[index]; i++) {
            int child_index = find_or_add_node(children[index][i]);
            // 将子节点添加到结果集中
            strcpy(result[result_count++], nodes[child_index]);
            // 递归遍历子节点的子节点
            dfs(child_index);
        }
    }
    
    // 比较函数，用于qsort的字典序排序
    int compare(const void *a, const void *b) {
        return strcmp((char *)a, (char *)b);
    }
    
    // 主函数
    int main() {
        int n;  // 输入的行数
        scanf("%d", &n);  // 读取行数
    
        struct Tree tree[MAX_NODES];  // 存储树的父子节点关系
    
        // 读取输入的节点关系
        for (int i = 0; i < n; i++) {
            scanf("%s %s", tree[i].child, tree[i].parent);  // 读取子节点和父节点
        }
    
        // 建立节点关系
        for (int i = 0; i < n; i++) {
            // 获取父节点和子节点的索引
            int parent_index = find_or_add_node(tree[i].parent);
            int child_index = find_or_add_node(tree[i].child);
            // 将子节点加入父节点的子节点列表
            strcpy(children[parent_index][children_count[parent_index]++], tree[i].child);
        }
    
        char target_node[MAX_NAME_LEN];  // 目标节点
        scanf("%s", target_node);  // 读取查询的目标节点
    
        int target_index = find_or_add_node(target_node);  // 找到目标节点的索引
    
        // 使用DFS收集所有下层节点
        dfs(target_index);
    
        // 对结果集中收集的节点进行字典序排序
        qsort(result, result_count, MAX_NAME_LEN, compare);
    
        // 输出排序后的所有下层节点
        for (int i = 0; i < result_count; i++) {
            printf("%s\n", result[i]);
        }
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

#####

