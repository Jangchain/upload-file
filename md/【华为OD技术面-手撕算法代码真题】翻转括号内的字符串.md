## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * **示例 1：**
  * **示例 2：**
  * **示例 3：**
  * **示例 4：**
  * **提示：**
  * C++
  * Java
  * javaScript
  * Python

## 题目描述

给出一个字符串 `s`（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 **不应** 包含任何括号。

## **示例 1：**

    
    
    输入：s = "(abcd)"
    输出："dcba"
    

## **示例 2：**

    
    
    输入：s = "(u(love)i)"
    输出："iloveu"
    解释：先反转子字符串 "love" ，然后反转整个字符串。
    

## **示例 3：**

    
    
    输入：s = "(ed(et(oc))el)"
    输出："leetcode"
    解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。
    

## **示例 4：**

    
    
    输入：s = "a(bcdefghijkl(mno)p)q"
    输出："apmnolkjihgfedcbq"
    

## **提示：**

  * `1 <= s.length <= 2000`
  * `s` 中只有小写英文字母和括号
  * 题目测试用例确保所有括号都是成对出现的

## C++

    
    
    #include <iostream>
    #include <string>
    #include <deque>
    
    using namespace std;
    
    class Main {
    public:
        deque<char> deq; // Renamed variable to avoid conflict with std::deque
        char path[2009];
    
        string reverseParentheses(string s) {
            int n = s.length();
            for (int i = 0; i < n; i++) {
                char c = s[i];
                if (c == ')') {
                    int idx = 0;
                    while (!deq.empty()) {
                        if (deq.back() == '(') {
                            deq.pop_back();
                            for (int j = 0; j < idx; j++) {
                                deq.push_back(path[j]);
                            }
                            break;
                        } else {
                            path[idx++] = deq.back();
                            deq.pop_back();
                        }
                    }
                } else {
                    deq.push_back(c);
                }
            }
            string result = "";
            while (!deq.empty()) {
                result += deq.front();
                deq.pop_front();
            }
            return result;
        }
    };
    
    int main() {
        string s;
        getline(cin, s);
        Main main;
        cout << main.reverseParentheses(s) << endl;
        return 0;
    }
    

## Java

    
    
    import java.util.Scanner;
    
    public class Main {
        // 初始化一个字符数组 deque 作为双端队列，用于存储输入字符串中的字符
        char[] deque = new char[2009];
        // 初始化头指针 head 和尾指针 tail
        int head = 0, tail = -1;
        // 初始化一个字符数组 path，用于临时存储需要反转的子字符串
        char[] path = new char[2009];
    
        public static void main(String[] args) {
            // 创建一个 Scanner 对象，用于从控制台读取输入
            Scanner scanner = new Scanner(System.in);
            // 读取输入的字符串
            String s = scanner.nextLine();
            // 创建一个 Main 对象
            Main main = new Main();
            // 调用 reverseParentheses 方法处理输入字符串，并输出结果
            System.out.println(main.reverseParentheses(s));
        }
    
        public String reverseParentheses(String s) {
            // 获取输入字符串的长度
            int n = s.length();
            // 将输入字符串转换为字符数组
            char[] cs = s.toCharArray();
            // 遍历输入字符串中的每个字符
            for (int i = 0; i < n; i++) {
                char c = cs[i];
                // 如果当前字符是右括号
                if (c == ')') {
                    // 初始化一个索引变量 idx，用于记录需要反转的子字符串的长度
                    int idx = 0;
                    // 当尾指针大于等于头指针时，执行循环
                    while (tail >= head) {
                        // 如果当前队尾字符是左括号
                        if (deque[tail] == '(') {
                            // 将尾指针向前移动一位
                            tail--;
                            // 将 path 中的字符按顺序添加到 deque 的队尾
                            for (int j = 0; j < idx; j++) {
                                deque[++tail] = path[j];
                            }
                            // 跳出循环
                            break;
                        } else {
                            // 如果当前队尾字符不是左括号，将其添加到 path 中，并将尾指针向前移动一位
                            path[idx++] = deque[tail--];
                        }
                    }
                } else {
                    // 如果当前字符不是右括号，将其添加到 deque 的队尾
                    deque[++tail] = c;
                }
            }
            // 创建一个 StringBuilder 对象，用于存储最终结果
            StringBuilder sb = new StringBuilder();
            // 当尾指针大于等于头指针时，将 deque 中的字符添加到 StringBuilder 对象中
            while (tail >= head) sb.append(deque[head++]);
            // 返回最终结果
            return sb.toString();
        }
    }
    

## javaScript

    
    
    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    class StringReverse {
      constructor() {
        this.deque = Array(2009).fill('');
        this.head = 0;
        this.tail = -1;
        this.path = Array(2009).fill('');
      }
    
      reverseParentheses(s) {
        let n = s.length;
        for (let i = 0; i < n; i++) {
          let c = s[i];
          if (c == ')') {
            let idx = 0;
            while (this.tail >= this.head) {
              if (this.deque[this.tail] == '(') {
                this.deque[this.tail] = '';
                this.tail--;
                for (let j = 0; j < idx; j++) {
                  this.deque[this.tail + 1] = this.path[j];
                  this.tail++;
                }
                break;
              } else {
                this.path[idx] = this.deque[this.tail];
                this.deque[this.tail] = '';
                this.tail--;
                idx++;
              }
            }
          } else {
            this.deque[this.tail + 1] = c;
            this.tail++;
          }
        }
        let result = '';
        while (this.tail >= this.head) {
          result += this.deque[this.head];
          this.head++;
        }
        return result;
      }
    }
    
    readline.on('line', s => {
      let main = new StringReverse();
      console.log(main.reverseParentheses(s));
      readline.close();
    });
    

## Python

    
    
    class Main:
        def __init__(self):
            self.deque = [''] * 2009
            self.head = 0
            self.tail = -1
            self.path = [''] * 2009
    
        def reverseParentheses(self, s):
            n = len(s)
            for i in range(n):
                c = s[i]
                if c == ')':
                    idx = 0
                    while self.tail >= self.head:
                        if self.deque[self.tail] == '(':
                            self.deque[self.tail] = ''
                            self.tail -= 1
                            for j in range(idx):
                                self.deque[self.tail + 1] = self.path[j]
                                self.tail += 1
                            break
                        else:
                            self.path[idx] = self.deque[self.tail]
                            self.deque[self.tail] = ''
                            self.tail -= 1
                            idx += 1
                else:
                    self.deque[self.tail + 1] = c
                    self.tail += 1
            result = ''
            while self.tail >= self.head:
                result += self.deque[self.head]
                self.head += 1
            return result
    
    if __name__ == "__main__":
        s = input()
        main = Main()
        print(main.reverseParentheses(s))
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * **示例 1：**
  * **示例 2：**
  * **示例 3：**
  * **示例 4：**
  * **提示：**
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/65a6cf12409df7faeb55de70b71b710d.png)

