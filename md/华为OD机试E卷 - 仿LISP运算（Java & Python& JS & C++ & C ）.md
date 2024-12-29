## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

LISP 语言唯一的语法就是括号要配对。

形如 (OP P1 P2 …)，括号内元素由单个空格分割。

其中第一个元素 OP 为操作符，后续元素均为其参数，参数个数取决于操作符类型。

注意：

参数 P1, P2 也有可能是另外一个嵌套的 (OP P1 P2 …) ，当前 OP 类型为 add / sub / mul /
div（全小写），分别代表整数的加减乘除法，简单起见，所有 OP 参数个数均为 2 。

举例：

  * 输入：(mul 3 -7)输出：-21
  * 输入：(add 1 2) 输出：3
  * 输入：(sub (mul 2 4) (div 9 3)) 输出 ：5
  * 输入：(div 1 0) 输出：error

题目涉及数字均为整数，可能为负；

不考虑 32 位溢出翻转，计算过程中也不会发生 32 位溢出翻转，

除零错误时，输出 “error”，

除法遇除不尽，向下取整，即 3/2 = 1

​

## 输入描述

输入为长度不超过512的字符串，用例保证了无语法错误

## 输出描述

输出计算结果或者“error”

## 示例1

输入

    
    
    (div 12 (sub 45 45))
    

输出

    
    
    error
    

说明

> ## 示例2

输入

    
    
    (add 1 (div -7 3))
    

输出

    
    
    -2
    

说明

>
>     输入：(mul 3 -7)
>     输出：-21
>     输入：(add 1 2)
>     输出：3
>     输入：(sub (mul 2 4) (div 9 3))
>     输出：5
>     输入：(div 1 0)
>     输出：error
>  

## 解题思路

## Java

    
    
    import java.util.Scanner;
    import java.util.Stack;
    
    public class Main {
    
        static Stack<Integer> numStack = new Stack<>();   // 数字栈
        static Stack<String> operaStack = new Stack<>();  // 操作符栈
    
        // 计算表达式(param1 op param2)的值
        public static void calc(int param1, int param2) {
            String op = operaStack.pop();   // 取出操作符
            if (op.equals("add")) {    // 如果是加法
                numStack.push(param1 + param2); // 将计算结果压入数字栈
            } else if (op.equals("sub")) {  // 如果是减法
                numStack.push(param1 - param2);
            } else if (op.equals("mul")) {  // 如果是乘法
                numStack.push(param1 * param2);
            } else {    // 如果是除法
                if (param2 == 0) {  // 如果除数为0
                    System.out.println("error");
                    System.exit(0);
                } else {
                    int res = param1 / param2;  // 计算商
                    if (param1 % param2 != 0) { // 如果有余数
                        if (res < 0) {  // 如果商为负数
                            res -= 1;   // 向下取整
                        } else {
                            res += 1;   // 向上取整
                        }
                    }
                    numStack.push(res); // 将计算结果压入数字栈
                }
            }
        }
    
    
        public static void main(String[] args) {
             // 处理输入
            Scanner sc = new Scanner(System.in);
            String exp = sc.nextLine(); // 读入表达式
    
            int mark = 0;   // 标记数字串的起始位置
            int param1 = 0;    // 参数1
            int param2 = 0;    // 参数2
    
            for (int i=0; i<exp.length(); i++) {
                String ch = exp.charAt(i) + ""; // 取出当前字符
                if (ch.equals("(")) {   // 如果是左括号
                    operaStack.push(exp.substring(i + 1, i + 4));    // 取出操作符并压入操作符栈
                    i += 4; // 跳过操作符
                    mark = i + 1;   // 标记数字串的起始位置
                } else if (ch.equals(")")) {   // 如果是右括号
                    if (mark < i) { // 如果有数字串
                        numStack.push(Integer.parseInt(exp.substring(mark, i))); // 将数字串转为整数并压入数字栈
                        i += 1; // 跳过右括号
                        mark = i + 1;   // 标记数字串的起始位置
                    }
                    param2 = numStack.pop();    // 取出数字栈顶元素作为参数2
                    param1 = numStack.pop();    // 取出数字栈顶元素作为参数1
                    calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
                } else {
                    if (ch.equals(" ")) {   // 如果是空格
                        if (mark < i) { // 如果有数字串
                            numStack.push(Integer.parseInt(exp.substring(mark, i))); // 将数字串转为整数并压入数字栈
                            mark = i + 1;   // 标记数字串的起始位置
                        }
                    }
                }
            }
    
            while (operaStack.size()!= 0) {    // 如果操作符栈非空
                param2 = numStack.pop();    // 取出数字栈顶元素作为参数2
                param1 = numStack.pop();    // 取出数字栈顶元素作为参数1
                calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
            }
    
            int ans =numStack.get(0);   // 取出数字栈顶元素作为表达式的值
            System.out.println(ans);
        }
    }
    
    

## Python

    
    
    import math
    numStack = []   # 数字栈
    operaStack = []  # 操作符栈
    
    # 计算表达式(param1 op param2)的值
    def calc(param1, param2):
        global numStack, operaStack
        op = operaStack.pop()   # 取出操作符
        if op == "add":    # 如果是加法
            numStack.append(param1 + param2) # 将计算结果压入数字栈
        elif op == "sub":  # 如果是减法
            numStack.append(param1 - param2)
        elif op == "mul":  # 如果是乘法
            numStack.append(param1 * param2)
        else:    # 如果是除法
            if param2 == 0:  # 如果除数为0
                print("error")
                exit(0)
            else:
                res = param1 // param2  # 计算商
                numStack.append(res) # 将计算结果压入数字栈
    
    
    # 处理输入
    exp = input() # 读入表达式
    
    mark = 0   # 标记数字串的起始位置
    param1 = 0    # 参数1
    param2 = 0    # 参数2
    
    for i in range(len(exp)):
        ch = exp[i] # 取出当前字符
        if ch == "(":   # 如果是左括号
            operaStack.append(exp[i + 1:i + 4])    # 取出操作符并压入操作符栈
            i += 4  # 跳过操作符
            mark = i + 1   # 标记数字串的起始位置
        elif ch == ")":   # 如果是右括号
            if mark < i: # 如果有数字串
                numStack.append(int(exp[mark:i])) # 将数字串转为整数并压入数字栈
                i += 1 # 跳过右括号
                mark = i + 1   # 标记数字串的起始位置
            param2 = numStack.pop()    # 取出数字栈顶元素作为参数2
            param1 = numStack.pop()    # 取出数字栈顶元素作为参数1
            calc(param1, param2)   # 计算表达式的值并将结果压入数字栈
        else:
            if ch == " ":   # 如果是空格
                if mark < i: # 如果有数字串
                    numStack.append(int(exp[mark:i])) # 将数字串转为整数并压入数字栈
                    mark = i + 1   # 标记数字串的起始位置
    
    while len(operaStack) != 0:    # 如果操作符栈非空
        param2 = numStack.pop()    # 取出数字栈顶元素作为参数2
        param1 = numStack.pop()    # 取出数字栈顶元素作为参数1
        calc(param1, param2)   # 计算表达式的值并将结果压入数字栈
    
    ans = numStack[0]   # 取出数字栈顶元素作为表达式的值
    print(ans)
    
    
    

## JavaScript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    class Stack {
      constructor() {
        this.items = [];
      }
    
      push(element) {
        this.items.push(element);
      }
    
      pop() {
        if (this.items.length == 0) return "Underflow";
        return this.items.pop();
      }
    
      peek() {
        return this.items[this.items.length - 1];
      }
    
      isEmpty() {
        return this.items.length == 0;
      }
    
      size() {
        return this.items.length;
      }
    }
    
    const numStack = new Stack();   // 数字栈
    const operaStack = new Stack();  // 操作符栈
    
    // 计算表达式(param1 op param2)的值
    function calc(param1, param2) {
      const op = operaStack.pop();   // 取出操作符
      if (op === "add") {    // 如果是加法
        numStack.push(param1 + param2); // 将计算结果压入数字栈
      } else if (op === "sub") {  // 如果是减法
        numStack.push(param1 - param2);
      } else if (op === "mul") {  // 如果是乘法
        numStack.push(param1 * param2);
      } else {    // 如果是除法
        if (param2 === 0) {  // 如果除数为0
          console.log("error");
          process.exit(0);
        } else {
          let res = Math.floor(param1 / param2);  // 计算商
          
          numStack.push(res); // 将计算结果压入数字栈
        }
      }
    }
    
    // 处理输入
    rl.on('line', (input) => {
      const exp = input;   // 读入表达式
    
      let mark = 0;   // 标记数字串的起始位置
      let param1 = 0;    // 参数1
      let param2 = 0;    // 参数2
    
      for (let i=0; i<exp.length; i++) {
        const ch = exp.charAt(i); // 取出当前字符
        if (ch === "(") {   // 如果是左括号
          operaStack.push(exp.substring(i + 1, i + 4));    // 取出操作符并压入操作符栈
          i += 4; // 跳过操作符
          mark = i + 1;   // 标记数字串的起始位置
        } else if (ch === ")") {   // 如果是右括号
          if (mark < i) { // 如果有数字串
            numStack.push(parseInt(exp.substring(mark, i))); // 将数字串转为整数并压入数字栈
            i += 1; // 跳过右括号
            mark = i + 1;   // 标记数字串的起始位置
          }
          param2 = numStack.pop();    // 取出数字栈顶元素作为参数2
          param1 = numStack.pop();    // 取出数字栈顶元素作为参数1
          calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
        } else {
          if (ch === " ") {   // 如果是空格
            if (mark < i) { // 如果有数字串
              numStack.push(parseInt(exp.substring(mark, i))); // 将数字串转为整数并压入数字栈
              mark = i + 1;   // 标记数字串的起始位置
            }
          }
        }
      }
    
      while (!operaStack.isEmpty()) {    // 如果操作符栈非空
        param2 = numStack.pop();    // 取出数字栈顶元素作为参数2
        param1 = numStack.pop();    // 取出数字栈顶元素作为参数1
        calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
      }
    
      const ans = numStack.peek();   // 取出数字栈顶元素作为表达式的值
      console.log(ans);
    
      rl.close();
    });
    
    
    

## C++

    
    
    #include <iostream>
    #include <stack>
    using namespace std;
    
    stack<int> numStack;   // 数字栈
    stack<string> operaStack;  // 操作符栈
    
    // 计算表达式(param1 op param2)的值
    void calc(int param1, int param2) {
        string op = operaStack.top();   // 取出操作符
        operaStack.pop();
        if (op == "add") {    // 如果是加法
            numStack.push(param1 + param2); // 将计算结果压入数字栈
        } else if (op == "sub") {  // 如果是减法
            numStack.push(param1 - param2);
        } else if (op == "mul") {  // 如果是乘法
            numStack.push(param1 * param2);
        } else {    // 如果是除法
            if (param2 == 0) {  // 如果除数为0
                cout << "error" << endl;
                exit(0);
            } else {
                int res = param1 / param2;  // 计算商
                if (param1 % param2 != 0) { // 如果有余数
                    if (res < 0) {  // 如果商为负数
                        res -= 1;   // 向下取整
                    } else {
                        res += 1;   // 向上取整
                    }
                }
                numStack.push(res); // 将计算结果压入数字栈
            }
        }
    }
    
    
    int main() {
        // 处理输入
        string exp;
        getline(cin, exp); // 读入表达式
    
        int mark = 0;   // 标记数字串的起始位置
        int param1 = 0;    // 参数1
        int param2 = 0;    // 参数2
    
        for (int i=0; i<exp.length(); i++) {
            string ch = exp.substr(i, 1); // 取出当前字符
            if (ch == "(") {   // 如果是左括号
                operaStack.push(exp.substr(i + 1, 3));    // 取出操作符并压入操作符栈
                i += 4; // 跳过操作符
                mark = i + 1;   // 标记数字串的起始位置
            } else if (ch == ")") {   // 如果是右括号
                if (mark < i) { // 如果有数字串
                    numStack.push(stoi(exp.substr(mark, i - mark)));//将数字串转为整数并压入数字栈
                    i += 1; // 跳过右括号
                    mark = i + 1;   // 标记数字串的起始位置
                }
                param2 = numStack.top();    // 取出数字栈顶元素作为参数2
                numStack.pop();
                param1 = numStack.top();    // 取出数字栈顶元素作为参数1
                numStack.pop();
                calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
            } else {
                if (ch == " ") {   // 如果是空格
                    if (mark < i) { // 如果有数字串
                        numStack.push(stoi(exp.substr(mark, i - mark)));//将数字串转为整数并压入数字栈
                        mark = i + 1;   // 标记数字串的起始位置
                    }
                }
            }
        }
    
        while (!operaStack.empty()) {    // 如果操作符栈非空
            param2 = numStack.top();    // 取出数字栈顶元素作为参数2
            numStack.pop();
            param1 = numStack.top();    // 取出数字栈顶元素作为参数1
            numStack.pop();
            calc(param1, param2);   // 计算表达式的值并将结果压入数字栈
        }
    
        int ans = numStack.top();   // 取出数字栈顶元素作为表达式的值
        cout << ans << endl;
        return 0;
    }
    
    

## C语言

    
    
     #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    #define MAX_STACK_SIZE 512
    
    // 数字栈和操作符栈
    int numStack[MAX_STACK_SIZE];
    char operaStack[MAX_STACK_SIZE][4];
    int numTop = -1, operaTop = -1;
    
    // 压入数字栈
    void pushNum(int value) {
        numStack[++numTop] = value;
    }
    
    // 弹出数字栈
    int popNum() {
        return numStack[numTop--];
    }
    
    // 压入操作符栈
    void pushOpera(const char* value) {
        strcpy(operaStack[++operaTop], value);
    }
    
    // 弹出操作符栈
    void popOpera(char* result) {
        strcpy(result, operaStack[operaTop--]);
    }
    
    // 计算表达式
    void calc(int param1, int param2) {
        char op[4];
        popOpera(op);
    
        if (strcmp(op, "add") == 0) {
            pushNum(param1 + param2);
        } else if (strcmp(op, "sub") == 0) {
            pushNum(param1 - param2);
        } else if (strcmp(op, "mul") == 0) {
            pushNum(param1 * param2);
        } else if (strcmp(op, "div") == 0) {
            if (param2 == 0) {
                printf("error\n");
                exit(0);
            }
            int res = param1 / param2;
            pushNum(res);
        }
    }
    
    int main() {
        char exp[512];
        fgets(exp, 512, stdin); // 读取表达式
        exp[strcspn(exp, "\n")] = '\0'; // 去掉换行符
    
        int mark = 0; // 数字串起始位置
        int param1 = 0, param2 = 0;
    
        for (int i = 0; i < strlen(exp); i++) {
            char ch = exp[i];
    
            if (ch == '(') { // 左括号
                char op[4];
                strncpy(op, exp + i + 1, 3);
                op[3] = '\0';
                pushOpera(op);
                i += 4; // 跳过操作符
                mark = i + 1;
            } else if (ch == ')') { // 右括号
                if (mark < i) {
                    char numStr[12];
                    strncpy(numStr, exp + mark, i - mark);
                    numStr[i - mark] = '\0';
                    pushNum(atoi(numStr)); // 将数字压入数字栈
                }
                param2 = popNum();
                param1 = popNum();
                calc(param1, param2); // 计算表达式
                mark = i + 1;
            } else if (ch == ' ') { // 空格
                if (mark < i) {
                    char numStr[12];
                    strncpy(numStr, exp + mark, i - mark);
                    numStr[i - mark] = '\0';
                    pushNum(atoi(numStr)); // 将数字压入数字栈
                    mark = i + 1;
                }
            }
        }
    
        // 处理剩余操作符栈
        while (operaTop >= 0) {
            param2 = popNum();
            param1 = popNum();
            calc(param1, param2);
        }
    
        printf("%d\n", numStack[numTop]); // 输出结果
        return 0;
    }
    
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/b98429f56d7b21e9abb6e238d4c69d08.png)

## 完整用例

### 用例1

    
    
    (add 5 3)
    

### 用例2

    
    
    (sub 10 4)
    

### 用例3

    
    
    (mul 4 6)
    

### 用例4

    
    
    (div 8 2)
    

### 用例5

    
    
    (div 7 0)
    

### 用例6

    
    
    (add (mul 2 3) (div 12 4))
    

### 用例7

    
    
    (sub (add 5 3) (mul 2 2))
    

### 用例8

    
    
    (mul (sub 5 3) (div 6 2))
    

### 用例9

    
    
    (div (add 10 5) (sub 7 2))
    

### 用例10

    
    
    (mul (div 12 3) (add 2 1))
    

