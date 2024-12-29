## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试手撕算法代码真题 🌟

所有题目均为华为od实际面试过程中出现的算法代码真题。

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 用例
  * 题解
  *   * Java
  * 

![image-20240410152906698](https://i-blog.csdnimg.cn/blog_migrate/57a2a07f6a41b6f849d5fdcff61886ac.png)

## 题目描述

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

## 用例

**示例 1:**

    
    
    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    

**示例 2:**

    
    
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    

**示例 3:**

    
    
    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    

**提示：**

  * `0 <= s.length <= 5 * 104`
  * `s` 由英文字母、数字、符号和空格组成

## 题解

> https://leetcode.cn/problems/longest-substring-without-repeating-
> characters/solutions/2361797/3-wu-zhong-fu-zi-fu-de-zui-chang-zi-chua-26i5/

##

## Java

    
    
    class Solution {
        public int lengthOfLongestSubstring(String s) {
            Map<Character, Integer> dic = new HashMap<>();
            int i = -1, res = 0, len = s.length();
            for(int j = 0; j < len; j++) {
                if (dic.containsKey(s.charAt(j)))
                    i = Math.max(i, dic.get(s.charAt(j))); // 更新左指针 i
                dic.put(s.charAt(j), j); // 哈希表记录
                res = Math.max(res, j - i); // 更新结果
            }
            return res;
        }
    }
    
     
    

##

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 用例
  * 题解
  *   * Java
  * 

![fengmian](https://i-blog.csdnimg.cn/blog_migrate/408f39a9eb8cdd1b57a6d8f29ad865b2.png)

