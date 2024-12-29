## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

有一批箱子（形式为字符串，设为str），  
要求将这批箱子按从上到下以之字形的顺序摆放在宽度为 n 的空地，请输出箱子的摆放位置。  
例如：箱子ABCDEFG，空地宽度为3，摆放结果如图：

![image-20230306211836230](https://i-blog.csdnimg.cn/blog_migrate/b728c0294ef84c87ef399482022af62e.png)

则输出结果为：  
`AFG`  
`BE`  
`CD`

## 输入描述

输入一行字符串，通过空格分隔，前面部分为字母或数字组成的字符串str，表示箱子；  
后面部分为数字n，表示空地的宽度。例如：  
`ABCDEFG 3`

## 输出描述

输出只有一个整数，表示会影响或结果的交换方案个数。

箱子摆放结果，如题目示例所示

`AFG`  
`BE`  
`CD`

#### 备注

  1. 请不要在最后一行输出额外的空行
  2. str只包含字母和数字，1 <= len(str) <= 1000
  3. 1 <= n <= 1000

## 示例1

输入

    
    
    ABCDEFG 3
    

输出

    
    
    AFG
    BE
    CD
    

说明

> ## 解题思路

### 题意

有点像这道题：https://leetcode.cn/problems/zigzag-conversion/description/

  1. **题目背景** ：有一批箱子，用一个字符串 `str` 表示，每个字符代表一个箱子。将这些箱子以“之字形”的顺序放在一个宽度为 `n` 的空地中。

  2. **之字形摆放** ：在一个宽度为 `n` 的空地中，从上到下、从左到右，以“之字形”摆放箱子，摆放规则如下：

     * **第一列** ：从上到下摆放 `n` 个箱子。
     * **第二列** ：从下到上摆放 `n` 个箱子。
     * **第三列** ：再从上到下摆放，以此类推，每列摆放方向交替。
     * 每列在摆放时的位置会交替，因此称之为“之字形”摆放。
  3. **输出要求** ：按照每一列的结果从左到右依次输出。每行代表一列的箱子内容，**不要输出额外的空行** 。

### 摆放过程：

  * 第一列：从上到下摆放 `A`、`B`、`C`
  * 第二列：从下到上摆放 `D`、`E`、`F`
  * 第三列：从上到下摆放 `G`

摆放结构可以写成如下形式：

    
    
    AFG
    BE
    CD
    

### 解法1：数学推导

通过例子推导之字形摆放的规律及公式：

##### 例子：字符串 `ABCDEFG`，宽度 `n = 3`

摆放位置表如下：

字符| 行列位置| 字符| 行列位置| 字符| 行列位置  
---|---|---|---|---|---  
A| (0,0)| F| (0,1)| G| (0,2)  
B| (1,0)| E| (1,1)| |   
C| (2,0)| D| (2,1)| |   
  
##### 字符对应公式分析

  1. **第一列（正向放置）：**

     * A 第 0 个字符，位置 (0,0)，行数公式：`i % n = 0 % 3 = 0`
     * B 第 1 个字符，位置 (1,0)，行数公式：`i % n = 1 % 3 = 1`
     * C 第 2 个字符，位置 (2,0)，行数公式：`i % n = 2 % 3 = 2`
  2. **第二列（反向放置）：**

     * D 第 3 个字符，位置 (2,1)，行数公式：`n - 1 - (i % n) = 3 - 1 - (3 % 3) = 2`
     * E 第 4 个字符，位置 (1,1)，行数公式：`n - 1 - (i % n) = 3 - 1 - (4 % 3) = 1`
     * F 第 5 个字符，位置 (0,1)，行数公式：`n - 1 - (i % n) = 3 - 1 - (5 % 3) = 0`
  3. **第三列（正向放置）：**

     * G 第 6 个字符，位置 (0,2)，行数公式：`i % n = 6 % 3 = 0`

##### 总结规律

  1. **正向列** （从上到下放置）：`行数 = i % n`
  2. **反向列** （从下到上放置）：`行数 = n - 1 - (i % n)`

##### 最终公式

  * 初始时，**正向列公式** ：`行数 = i % n`
  * 当摆放方向切换时： 
    * **反向列公式** ：`行数 = n - 1 - (i % n)`
  * 按列顺序依次交替应用以上公式。

### 解法2 ： 模拟

#### 模拟之字形摆放

  * **行索引控制** ：使用 `current_row` 作为摆放行的指针，初始位置设为 0，指向第一行。
  * **方向控制** ：通过布尔变量 `is_ascending` 控制行索引的增减方向。初始值为 `True`，表示从上往下移动。

#### 遍历与摆放过程

  * **逐字符遍历** ：程序依次取出每个字符并放入 `placement_grid` 中，形成摆放过程的模拟。

    * 当 `is_ascending` 为 `True` 时，行索引增加，字符会逐行向下摆放；一旦达到底部（`current_row == width`），方向改变为 `False`，模拟反弹到顶部的效果。
    * 当 `is_ascending` 为 `False` 时，行索引减少，字符会逐行向上摆放；一旦到达顶部（`current_row == -1`），方向恢复为 `True`，模拟向下的循环效果。
  * **字符追加** ：将字符追加到 `current_row` 对应的行中，实现之字形效果。通过 `+=` 操作符将字符直接加入到对应行的字符串中。

  * 

#### 模拟示例

假设输入为 `ABCDEFG 3`，模拟过程如下：

  1. `placement_grid` 初始为 `["", "", ""]`
  2. 按照之字形摆放： 
     * `A` 放在第 0 行 → `["A", "", ""]`
     * `B` 放在第 1 行 → `["A", "B", ""]`
     * `C` 放在第 2 行 → `["A", "B", "C"]`
     * `D` 回到第 1 行 → `["A", "BD", "C"]`
     * `E` 回到第 0 行 → `["AE", "BD", "C"]`
     * `F` 到第 1 行 → `["AE", "BDF", "C"]`
     * `G` 到第 2 行 → `["AE", "BDF", "CG"]`

最终输出：

    
    
    AE
    BDF
    CG
    

#### 总结

从模拟角度来看，代码通过控制当前行指针和方向标志，模拟箱子字符的之字形摆放过程，实现字符在不同行之间的循环移动，形成题目描述的摆放效果。

## Java

    
    
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);  
            String str = scanner.next(); 
            int n = scanner.nextInt(); 
            int length = str.length();  
    
            // 初始化二维字符数组 matrix，用于存放箱子的摆放位置
            // 行数为 n（空地宽度），列数为 (length + n - 1) / n，确保能够容纳所有字符
            char[][] matrix = new char[n][(length + n - 1) / n];
            
            // 定义布尔变量 reverse 用于标记当前方向（之字形摆放）
            boolean reverse = false;
            int row = 0, col = 0; // 初始化当前行和列位置
    
            // 遍历每个字符，将其放入二维数组 matrix 中
            for (int i = 0; i < length; i++) {
                // 将当前字符放入 matrix 的指定位置
                matrix[row][col] = str.charAt(i);
    
                // 根据当前方向更新行索引 row 的位置
                if (reverse) {
                    row--; // 如果是反向，行位置减少
                } else {
                    row++; // 如果是正向，行位置增加
                }
    
                // 检查是否达到边界，如果是，则换行并反转方向
                if (row == n || row < 0) {
                    reverse = !reverse; // 反转方向
                    row = reverse ? n - 1 : 0; // 重置行索引：如果是反向则从底部开始，否则从顶部开始
                    col++; // 列索引增加一位，进入下一列
                }
            }
    
            // 遍历二维数组 matrix，输出摆放结果
            for (int i = 0; i < n; i++) { // 遍历每一行
                for (int j = 0; j < matrix[i].length; j++) { // 遍历每一列
                    if (matrix[i][j] != 0) { // 判断当前位置是否有字符
                        System.out.print(matrix[i][j]); // 输出字符
                    }
                }
                System.out.println(); // 每行输出完后换行
            }
        }
    }
    
    
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            String str = scanner.next(); // 读取箱子字符串
            int n = scanner.nextInt();   // 读取空地宽度
            int length = str.length();   // 获取箱子字符串长度
            
            // 初始化二维字符数组用于存储摆放结果
            char[][] matrix = new char[n][(length + n - 1) / n];
            
            boolean reverse = true; // 标记当前行的方向
            for (int i = 0; i < length; i++) {
                int k = i % n; // 计算行号
                if (k == 0) reverse = !reverse; // 每到新列改变方向
                if (reverse) k = n - 1 - k; // 如果当前是反向，则调整行号
    
                // 将当前字符放入对应的行列
                matrix[k][i / n] = str.charAt(i);
            }
    
            // 遍历并输出矩阵
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < matrix[i].length; j++) {
                    if (matrix[i][j] != 0) { // 检查是否有字符
                        System.out.print(matrix[i][j]);
                    }
                }
                System.out.println();
            }
        }
    }
    
    

## Python

    
    
    # 导入标准输入模块
    def main():
        # 读取输入字符串和空地宽度
        inputs = input().split()
        str_val = inputs[0]  # 第一个输入为字符串
        n = int(inputs[1])   # 第二个输入为宽度n
        length = len(str_val)  # 字符串长度
    
        # 初始化二维字符数组，行数为n，列数根据字符串长度计算
        matrix = [[''] * ((length + n - 1) // n) for _ in range(n)]
        
        reverse = False  # 定义方向标志，False表示向下，True表示向上
        row, col = 0, 0  # 初始化行、列索引
    
        # 遍历字符串，将字符存入二维数组
        for i in range(length):
            matrix[row][col] = str_val[i]  # 将当前字符放入相应位置
            
            # 更新行索引，根据方向变化
            if reverse:
                row -= 1
            else:
                row += 1
            
            # 到达边界时调整方向并移动列
            if row == n or row < 0:
                reverse = not reverse  # 反转方向
                row = n - 1 if reverse else 0  # 根据方向重置行索引
                col += 1  # 移动到下一列
    
        # 输出二维数组中的字符
        for row in matrix:
            print("".join(char for char in row if char))  # 过滤空白字符
    
    if __name__ == "__main__":
        main()
        
    def main():
        # 读取输入的字符串和宽度
        str_val = input().split()
        box_str = str_val[0]  # 获取箱子字符串
        n = int(str_val[1])   # 获取空地宽度
        length = len(box_str) # 获取字符串长度
    
        # 初始化二维数组，用于存放字符
        matrix = [[''] * ((length + n - 1) // n) for _ in range(n)]
    
        reverse = True  # 定义方向标记
        for i in range(length):
            k = i % n  # 计算行号
            if k == 0:
                reverse = not reverse  # 每到新列时改变方向
            if reverse:
                k = n - 1 - k  # 如果反向，调整行号
    
            # 将当前字符放入二维数组中的指定位置
            matrix[k][i // n] = box_str[i]
    
        # 输出结果
        for row in matrix:
            print("".join(char for char in row if char))  # 过滤掉空白字符
    
    if __name__ == "__main__":
        main()
    
    

## JavaScript

    
    
    // 读取输入并处理字符串及宽度
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on('line', (input) => {
      const inputs = input.split(' ');
      const strVal = inputs[0]; // 第一个输入是字符串
      const n = parseInt(inputs[1]); // 第二个输入是宽度n
      const length = strVal.length;  // 字符串长度
    
      // 初始化二维数组
     const matrix = new Array(parseInt(n)).fill().map(() => []);
    
      let reverse = false; // 方向标志
      let row = 0, col = 0; // 初始化行、列索引
    
      // 遍历字符串，将字符存入二维数组
      for (let i = 0; i < length; i++) {
        matrix[row][col] = strVal[i];
        
        if (reverse) {
          row--;
        } else {
          row++;
        }
    
        if (row === n || row < 0) {
          reverse = !reverse; // 反转方向
          row = reverse ? n - 1 : 0; 
          col++; // 进入下一列
        }
      }
    
      // 输出结果
      for (let i = 0; i < n; i++) {
        console.log(matrix[i].filter(char => char).join('')); // 输出每行字符
      }
    
      rl.close();
    });
    
    
    // Node.js 版本，读取输入并处理箱子字符串和宽度
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    rl.on("line", (input) => {
      const [boxStr, nStr] = input.split(" ");
      const n = parseInt(nStr);
      const length = boxStr.length;
    
      // 初始化二维数组
      const matrix = new Array(parseInt(n)).fill().map(() => []);
    
      let reverse = true; // 定义方向标记
      for (let i = 0; i < length; i++) {
        let k = i % n; // 计算行号
        if (k === 0) reverse = !reverse; // 新列时改变方向
        if (reverse) k = n - 1 - k; // 如果反向，则调整行号
    
        // 将字符放入矩阵
        matrix[k][Math.floor(i / n)] = boxStr[i];
      }
    
      // 输出矩阵
      matrix.forEach(row => {
        console.log(row.filter(char => char).join('')); // 过滤空白字符
      });
    
      rl.close();
    });
    
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <string>
    
    using namespace std;
    
    int main() {
        string str;
        int n;
        cin >> str >> n;
    
        int length = str.length();  // 获取字符串长度
    
        // 初始化二维字符数组
        vector<vector<char>> matrix(n, vector<char>((length + n - 1) / n, '\0'));
    
        bool reverse = false; // 方向标志
        int row = 0, col = 0; // 初始化行、列位置
    
        // 将字符按照规则存入二维数组
        for (int i = 0; i < length; i++) {
            matrix[row][col] = str[i];
    
            if (reverse) {
                row--; // 反向摆放
            } else {
                row++; // 正向摆放
            }
    
            if (row == n || row < 0) {
                reverse = !reverse; // 反转方向
                row = reverse ? n - 1 : 0; 
                col++; // 换到下一列
            }
        }
    
        // 输出结果
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] != '\0') { // 跳过空字符
                    cout << matrix[i][j];
                }
            }
            cout << endl; // 换行
        }
    
        return 0;
    }
    #include <iostream>
    #include <vector>
    #include <string>
    
    using namespace std;
    
    int main() {
        string str;
        int n;
         cin >> str >> n;
        int length = str.length();
    
        // 初始化二维数组
        vector<vector<char>> matrix(n, vector<char>((length + n - 1) / n, '\0'));
    
        bool reverse = true; // 定义方向标记
        for (int i = 0; i < length; i++) {
            int k = i % n; // 计算行号
            if (k == 0) reverse = !reverse; // 每列改变方向
            if (reverse) k = n - 1 - k; // 若反向则调整行号
    
            // 将字符存入矩阵
            matrix[k][i / n] = str[i];
        }
    
        // 输出矩阵
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < matrix[i].size(); j++) {
                if (matrix[i][j] != '\0') { // 过滤空白字符
                    cout << matrix[i][j];
                }
            }
            cout << endl;
        }
    
        return 0;
    }
    
    

## C语言

    
    
    #include <stdio.h>
    #include <string.h>
    
    int main() {
        char str[1001]; // 假设最大长度为1000
        int n;
    
        // 读取字符串和宽度
        scanf("%s %d", str, &n);
        int length = strlen(str); // 计算字符串长度
    
        // 初始化二维数组
        char matrix[n][(length + n - 1) / n];
        memset(matrix, 0, sizeof(matrix)); // 初始化为0
    
        int reverse = 0; // 方向标志，0表示向下，1表示向上
        int row = 0, col = 0; // 初始化行、列索引
    
        // 遍历字符串
        for (int i = 0; i < length; i++) {
            matrix[row][col] = str[i]; // 将字符存入矩阵
    
            if (reverse) {
                row--; // 向上移动
            } else {
                row++; // 向下移动
            }
    
            if (row == n || row < 0) {
                reverse = !reverse; // 改变方向
                row = reverse ? n - 1 : 0;
                col++; // 进入下一列
            }
        }
    
        // 输出二维数组的字符
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (length + n - 1) / n; j++) {
                if (matrix[i][j] != 0) {
                    putchar(matrix[i][j]);
                }
            }
            putchar('\n'); // 每行输出后换行
        }
    
        return 0;
    }
    #include <stdio.h>
    #include <string.h>
    
    int main() {
        char str[1001]; // 假设最大字符串长度为1000
        int n;
        
        
        scanf("%s %d", str, &n);
        int length = strlen(str);
    
        // 初始化二维数组，行数为n，列数根据字符串长度确定
        char matrix[n][(length + n - 1) / n];
        memset(matrix, 0, sizeof(matrix)); // 初始化为0
    
        int reverse = 1; // 定义方向标记，1表示当前为反向
        for (int i = 0; i < length; i++) {
            int k = i % n; // 计算行号
            if (k == 0) reverse = !reverse; // 每到新列改变方向
            if (reverse) k = n - 1 - k; // 如果反向，则调整行号
    
            // 将字符放入矩阵指定位置
            matrix[k][i / n] = str[i];
        }
    
        // 输出矩阵内容
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < (length + n - 1) / n; j++) {
                if (matrix[i][j] != 0) { // 检查是否有字符
                    putchar(matrix[i][j]);
                }
            }
            putchar('\n'); // 每行结束后换行
        }
    
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

### 完整用例

### 用例1

    
    
    ABCDEFG 3
    

### 用例2

    
    
    123456789 4
    

### 用例3

    
    
    ABCDEFGHIJKL 2
    

### 用例4

    
    
    12345 5
    

### 用例5

    
    
    ABCDEFGHIJ 9
    

### 用例6

    
    
    ZYXWVUTSRQPONMLKJIHGFEDCBA 6
    

### 用例7

    
    
    ABCDEFGHIJKLMNOPQRSTUVWX 4
    

### 用例8

    
    
    987654321 3
    

### 用例9

    
    
    ABCDEFGHIJKLMNO 7
    

### 用例10

    
    
    AB2CD2E3FG1HIJ5K5LM6NO 7
    

