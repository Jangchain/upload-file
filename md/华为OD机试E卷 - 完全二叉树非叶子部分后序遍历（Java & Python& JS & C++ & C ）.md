## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

给定一个以顺序储存结构存储整数值的完全二叉树序列（最多1000个整数），请找出此完全二叉树的所有非叶子节点部分，然后采用后序遍历方式将此部分树（不包含叶子）输出。

1、只有一个节点的树，此节点认定为根节点（非叶子）。

2、此完全二叉树并非满二叉树，可能存在倒数第二层出现叶子或者无右叶子的情况

其他说明：二叉树的后序遍历是基于根来说的，遍历顺序为：左-右-根

## 输入描述

一个通过空格分割的整数序列字符串

## 输出描述

非叶子部分树结构。备注：输出数字以空格分隔

## 示例1

输入

    
    
    1 2 3 4 5 6 7
    

输出

    
    
    2 3 1
    

说明

> 找到非叶子部分树结构，然后采用后序遍历输出。

> ## 解题思路

####

  1. **完全二叉树的数组表示** ：完全二叉树可以通过数组形式表示，其中父节点和子节点的关系通过索引确定：

     * 对于数组中的任一节点，其在数组中的索引为 ( i )： 
       * 左子节点的索引为 ( 2i + 1 )
       * 右子节点的索引为 ( 2i + 2 )
     * 反过来，任意节点的父节点索引可以通过 ( \frac{i-1}{2} ) 计算（向下取整）。
  2. **非叶子节点的确定** ：在完全二叉树中，只要节点至少有一个子节点，它就是一个非叶子节点。最后一个非叶子节点是最后一个节点的父节点。

  3. **后序遍历的要求** ：后序遍历的顺序是先访问左子树，然后访问右子树，最后访问根节点。对于非叶子节点的子树，也需要按照这一顺序遍历。

  4. **特殊情况** ：

     * **单节点树** ：如果树中只有一个节点，该节点同时是根节点和非叶子节点，直接输出。
     * **非满二叉树** ：在倒数第二层可能有叶子节点的情况，意味着最后一个节点可能没有子节点或只有一个子节点。

## Java

    
    
    import java.util.*;
    import java.io.*;
    
    public class Main {
        // 后序遍历函数
        public static void postorderTraversal(List<Integer> tree, int root, List<Integer> res) {
            int left = root * 2 + 1; // 左子节点的索引
            int right = root * 2 + 2; // 右子节点的索引
    
            if (left < tree.size()) { // 如果左子节点存在
                postorderTraversal(tree, left, res); // 递归遍历左子树
            }
            if (right < tree.size()) { // 如果右子节点存在
                postorderTraversal(tree, right, res); // 递归遍历右子树
            }
            if (left < tree.size() || right < tree.size()) { // 只有当当前节点有子节点时才是非叶子节点
                res.add(tree.get(root)); // 将非叶子根节点加入结果数组
            }
        }
    
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            String input = sc.nextLine(); // 读入一行数据
            String[] nums = input.split(" ");
            List<Integer> tree = new ArrayList<>();
            for (String num : nums) { // 逐个读入数字
                tree.add(Integer.parseInt(num)); // 将数字加入树的数组中
            }
    
            if (tree.size() == 1) { // 只有一个节点的情况
                System.out.println(tree.get(0)); // 直接输出该节点
                return;
            }
    
            List<Integer> res = new ArrayList<>();
            postorderTraversal(tree, 0, res); // 后序遍历
    
            StringBuilder sj = new StringBuilder();
            for (int i = 0; i < res.size(); i++) { // 将结果数组转换为字符串
                sj.append(res.get(i));
                if (i != res.size() - 1) sj.append(" ");
            }
    
            System.out.println(sj.toString()); // 输出结果字符串
        }
    }
    

## Python

    
    
    def postorder_traversal(tree, root, res):
        # 计算左右子节点的索引
        left = root * 2 + 1
        right = root * 2 + 2
    
        # 如果左子节点存在，递归遍历左子树
        if left < len(tree):
            postorder_traversal(tree, left, res)
        # 如果右子节点存在，递归遍历右子树
        if right < len(tree):
            postorder_traversal(tree, right, res)
        # 判断当前节点是否为非叶子节点
        if left < len(tree) or right < len(tree):
            res.append(tree[root])
    
    def main():
        # 读取输入的整数序列
        tree = list(map(int, input().split()))
        if len(tree) == 1:  # 如果只有一个节点
            print(tree[0])
            return
        
        res = []
        postorder_traversal(tree, 0, res)  # 后序遍历
        print(" ".join(map(str, res)))
    
    if __name__ == "__main__":
        main()
    

## JavaScript

    
    
    function postorderTraversal(tree, root, res) {
        const left = root * 2 + 1;  // 左子节点索引
        const right = root * 2 + 2; // 右子节点索引
    
        // 递归遍历左右子树
        if (left < tree.length) postorderTraversal(tree, left, res);
        if (right < tree.length) postorderTraversal(tree, right, res);
        // 只有非叶子节点才加入结果
        if (left < tree.length || right < tree.length) res.push(tree[root]);
    }
    
    
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    readline.on('line', input => {
        const tree = input.split(' ').map(Number);
        if (tree.length === 1) {
            console.log(tree[0]);
            return;
        }
    
        const res = [];
        postorderTraversal(tree, 0, res);
        console.log(res.join(' '));
        readline.close();
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <string>
    #include <sstream>
    using namespace std;
    
    void postorderTraversal(const vector<int>& tree, int root, vector<int>& res) {
        int left = root * 2 + 1;
        int right = root * 2 + 2;
    
        // 递归左右子树
        if (left < tree.size()) postorderTraversal(tree, left, res);
        if (right < tree.size()) postorderTraversal(tree, right, res);
        if (left < tree.size() || right < tree.size()) res.push_back(tree[root]);
    }
    
    int main() {
        string input;
        getline(cin, input);
        istringstream iss(input);
        vector<int> tree;
        int num;
        while (iss >> num) tree.push_back(num);
        if (tree.size() == 1) {
            cout << tree[0] << endl;
            return 0;
        }
    
        vector<int> res;
        postorderTraversal(tree, 0, res);
        for (int i = 0; i < res.size(); i++) {
            cout << res[i] << (i < res.size() - 1 ? " " : "");
        }
        cout << endl;
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    void postorderTraversal(int* tree, int root, int size, int* res, int* index) {
        int left = root * 2 + 1;
        int right = root * 2 + 2;
    
        // 递归遍历子树
        if (left < size) postorderTraversal(tree, left, size, res, index);
        if (right < size) postorderTraversal(tree, right, size, res, index);
        if (left < size || right < size) res[(*index)++] = tree[root];
    }
    
    int main() {
        char input[4000];
        fgets(input, 4000, stdin);
        int* tree = malloc(1000 * sizeof(int));
        int size = 0;
        char* token = strtok(input, " ");
        while (token) {
            tree[size++] = atoi(token);
            token = strtok(NULL, " ");
        }
        if (size == 1) {
            printf("%d\n", tree[0]);
            free(tree);
            return 0;
        }
    
        int* res = malloc(size * sizeof(int));
        int index = 0;
        postorderTraversal(tree, 0, size, res, &index);
        for (int i = 0; i < index; i++) {
            printf("%d%c", res[i], i < index - 1 ? ' ' : '\n');
        }
        free(tree);
        free(res);
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/1d2f33ed8cf2fb1b9a4fe09513f7aa94.png)

## 完整用例

### 用例1

    
    
    50 30 70 20 40 60
    

### 用例2

    
    
    1 2 3 4 5 6 7 8 9 10 11
    

### 用例3

    
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14
    

### 用例4

    
    
    10 20 30 40 50 60 70
    

### 用例5

    
    
    1 2 3 4 5 6 7 8
    

### 用例6

    
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    

### 用例7

    
    
    1 2 4 8
    

### 用例8

    
    
    1
    

### 用例9

    
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14
    

### 用例10

    
    
    1 2
    

