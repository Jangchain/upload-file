## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 解题思路
  *     *       * 优化后的语言表达：
      *         * **题目概述**
        * **解题思路**
  * Java
  * javaScript
  * Python

## 题目描述

> > 数组、哈希表、字符串、计数
>>

>> 中等难度

>>

>> https://leetcode.cn/problems/subdomain-visit-count/

## 解题思路

#### 优化后的语言表达：

##### **题目概述**

网站域名通常由多个子域名组成。例如，“discuss.leetcode.com” 由三个层级的域名构成，其中：

  * 顶级域名为 “com”，
  * 二级域名为 “leetcode.com”，
  * 三级域名为 “discuss.leetcode.com”。

当访问 “discuss.leetcode.com” 时，实际上也会隐式访问其父域名 “leetcode.com” 和顶级域名 “com”。

计算机配对域名的格式为 “rep d1.d2.d3” 或 “rep d1.d2”，其中 `rep` 代表该域名的访问次数，`d1.d2.d3` 或
`d1.d2` 为实际域名。

例如，“9001 discuss.leetcode.com” 表示 “discuss.leetcode.com” 被访问了 9001 次。

现给定一个由此类计算机配对域名组成的数组
`cpdomains`，需要解析每个配对域名，并计算各级域名的总访问次数，最后以数组形式返回结果。返回顺序可以是任意的。

##### **解题思路**

此题要求汇总各层级域名的访问次数，可以利用哈希表来完成统计。具体步骤如下：

  1. **特殊情况处理** ：如果 `cpdomains` 数组为空，直接返回空数组。

  2. **使用哈希表存储访问次数** ：

     * 创建一个哈希表 `times_dict`，用于存储不同层级域名的访问次数。
  3. **解析并统计访问次数** ：

     * 遍历 `cpdomains` 数组，对于每个计算机配对域名 `cpdomain`，先将其访问次数 `times` 与域名 `domain` 分离。
     * 将 `domain` 转换为子域名数组 `domain_list`，然后逆序拼接形成不同级别的子域名 `sub_domain`。
     * 对于每个 `sub_domain`，如果它不在 `times_dict` 中，则将其与对应的访问次数 `times` 添加到哈希表中；如果它已经存在，则累加其访问次数。
  4. **构建并返回结果数组** ：

     * 遍历哈希表 `times_dict`，将每个域名和其访问次数拼接成字符串，存入结果数组中。
     * 返回结果数组。

## Java

    
    
     
    
    class Solution {
        public List<String> subdomainVisits(String[] cpdomains) {
            if (cpdomains == null || cpdomains.length == 0) {
                return new ArrayList<>();
            }
    
            Map<String, Integer> timesDict = new HashMap<>();
    
            for (String cpdomain : cpdomains) {
                String[] parts = cpdomain.split(" ");
                int times = Integer.parseInt(parts[0]);
                String domain = parts[1];
    
                String[] domainList = domain.split("\\.");
                for (int i = domainList.length - 1; i >= 0; i--) {
                    String subDomain = String.join(".", Arrays.copyOfRange(domainList, i, domainList.length));
                    timesDict.put(subDomain, timesDict.getOrDefault(subDomain, 0) + times);
                }
            }
    
            List<String> res = new ArrayList<>();
            for (String key : timesDict.keySet()) {
                res.add(timesDict.get(key) + " " + key);
            }
    
            return res;
        }
    }
    

## javaScript

    
    
     
    var subdomainVisits = function(cpdomains) {
        if (!cpdomains || cpdomains.length === 0) {
            return [];
        }
    
        let timesDict = {};
    
        cpdomains.forEach(cpdomain => {
            let [times, domain] = cpdomain.split(' ');
            times = parseInt(times);
            
            let domainList = domain.split('.');
            for (let i = domainList.length - 1; i >= 0; i--) {
                let subDomain = domainList.slice(i).join('.');
                if (!timesDict[subDomain]) {
                    timesDict[subDomain] = times;
                } else {
                    timesDict[subDomain] += times;
                }
            }
        });
    
        let res = [];
        for (let key in timesDict) {
            res.push(timesDict[key] + ' ' + key);
        }
    
        return res;
    };
     
    

## Python

    
    
    class Solution:
        def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
            if not cpdomains:
                return []
    
            times_dict = dict()
            for cpdomain in cpdomains:
                tiems, domain = cpdomain.split()
                tiems = int(tiems)
                
                domain_list = domain.split('.')
                for i in range(len(domain_list) - 1, -1, -1):
                    sub_domain = '.'.join(domain_list[i:])
                    if sub_domain not in times_dict:
                        times_dict[sub_domain] = tiems
                    else:
                        times_dict[sub_domain] += tiems
            
            res = []
            for key in times_dict.keys():
                res.append(str(times_dict[key]) + ' ' + key)
            return res
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 解题思路
  *     *       * 优化后的语言表达：
      *         * **题目概述**
        * **解题思路**
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/b6608860e62feedde911d2bcf4217ab2.png)

