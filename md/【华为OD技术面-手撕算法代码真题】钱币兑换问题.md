## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 输入描述
  * 输出描述
  * 用例1
  * 用例2
  * C++
  * Java
  * javaScript
  * Python

## 题目描述

在一个国家仅有1分，2分，3分硬币，将钱N兑换成硬币有很多种兑法。请你编程序计算出共有多少种兑法。

## 输入描述

每行只有一个正整数N，N小于32768。

## 输出描述

对应每个输入，输出兑换方法数。

## 用例1

输入

    
    
    2934
    

输出

    
    
    718831
    

## 用例2

输入

    
    
    12553
    

输出

    
    
    13137761
    

## C++

    
    
    #include<iostream>
    
    using namespace std;
    
    int main()
    {
        // 定义四个整数变量：a、b、n和sign。其中，sign初始值为1
        int a,b,n,sign=1;
        cin >> n;
           // 计算n除以3的商，赋值给a
        a = n / 3;
        // 将a加到sign上
        sign += a;
        // 使用for循环，循环次数为n除以3的商加1
        for (int i = 0; i <= n / 3; i++)
        {
            // 在每次循环中，计算(n - 3 * i)除以2的商，赋值给b
            b = (n - 3 * i) / 2;
            // 将b加到sign上
            sign += b;
        }
        // 输出sign的值
        cout << sign << endl;
        // 将sign重置为1，为处理下一个输入做准备
        sign = 1;
        // 程序正常结束，返回0
        return 0;
    }
    

## Java

    
    
    import java.util.Scanner;
    
    public class Main {
        public static void main(String[] args) {
            // 创建一个Scanner对象，用于读取用户输入
            Scanner scanner = new Scanner(System.in);
            // 读取用户输入的整数n
            int n = scanner.nextInt();
            // 定义四个整数变量：a、b和sign。其中，sign初始值为1
            int a, b, sign = 1;
            // 计算n除以3的商，赋值给a
            a = n / 3;
            // 将a加到sign上
            sign += a;
            // 使用for循环，循环次数为n除以3的商加1
            for (int i = 0; i <= n / 3; i++) {
                // 在每次循环中，计算(n - 3 * i)除以2的商，赋值给b
                b = (n - 3 * i) / 2;
                // 将b加到sign上
                sign += b;
            }
            // 输出sign的值
            System.out.println(sign);
            // 将sign重置为1，为处理下一个输入做准备
            sign = 1;
        }
    }
    

## javaScript

    
    
    // 引入readline模块，用于读取用户输入
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    // 读取用户输入的整数n
    rl.on('line', (n) => {
        // 定义四个整数变量：a、b和sign。其中，sign初始值为1
        let a, b, sign = 1;
        // 计算n除以3的商，赋值给a
        a = Math.floor(n / 3);
        // 将a加到sign上
        sign += a;
        // 使用for循环，循环次数为n除以3的商加1
        for (let i = 0; i <= n / 3; i++) {
            // 在每次循环中，计算(n - 3 * i)除以2的商，赋值给b
            b = Math.floor((n - 3 * i) / 2);
            // 将b加到sign上
            sign += b;
        }
        // 输出sign的值
        console.log(sign);
        // 将sign重置为1，为处理下一个输入做准备
        sign = 1;
        rl.close();
    });
    

## Python

    
    
    # 读取用户输入的整数n
    n = int(input(""))
    # 定义四个整数变量：a、b和sign。其中，sign初始值为1
    a, b, sign = 0, 0, 1
    # 计算n除以3的商，赋值给a
    a = n // 3
    # 将a加到sign上
    sign += a
    # 使用for循环，循环次数为n除以3的商加1
    for i in range(n // 3 + 1):
        # 在每次循环中，计算(n - 3 * i)除以2的商，赋值给b
        b = (n - 3 * i) // 2
        # 将b加到sign上
        sign += b
    # 输出sign的值
    print(sign)
    # 将sign重置为1，为处理下一个输入做准备
    sign = 1
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 输入描述
  * 输出描述
  * 用例1
  * 用例2
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/2ae808fdb26022cc99ad3fd13742a4bf.png)

