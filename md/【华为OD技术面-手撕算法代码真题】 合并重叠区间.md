## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 解题思路
  * C++
  * Java
  * javaScript
  * Python

## 题目描述

> 以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]`
> 。请你合并所有重叠的区间，并返回 _一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间_ 。
>
> **示例 1：**
>  
>  
>     输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
>     输出：[[1,6],[8,10],[15,18]]
>     解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
>  
>
> **示例 2：**
>  
>  
>     输入：intervals = [[1,4],[4,5]]
>     输出：[[1,5]]
>     解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
>  
>
> **提示：**
>
>   * `1 <= intervals.length <= 104`
>   * `intervals[i].length == 2`
>   * `0 <= starti <= endi <= 104`
>

## 解题思路

当你需要合并一组可能重叠的区间时，可以使用以下解题思路：

  1. **排序** ：首先，将所有区间按照起始位置进行排序。这一步是合并区间的关键，因为排序后，你可以按顺序检查每个区间，从而简化合并过程。

  2. **初始化结果数组** ：创建一个空数组 `merged`，用来存储合并后的区间。

  3. **遍历区间** ：

     * 对于每个区间，检查它是否与结果数组中最后一个区间重叠。
     * 如果结果数组为空，或者当前区间的起始位置大于结果数组中最后一个区间的结束位置，则将当前区间直接添加到结果数组中。
     * 如果有重叠（即当前区间的起始位置小于或等于结果数组中最后一个区间的结束位置），则需要合并当前区间与结果数组中最后一个区间。更新结果数组中最后一个区间的结束位置，将其设置为当前区间的结束位置和结果数组中最后一个区间的结束位置中的较大值。
  4. **返回结果** ：遍历完成后，`merged` 数组中存储的即为合并后的区间列表。

这个思路利用排序来简化区间合并的过程，确保只需要单次遍历就可以完成所有的合并操作，从而有效地减少了时间复杂度。排序之后的线性遍历让我们只需要关心当前区间和结果数组中最后一个区间的关系，极大地简化了逻辑判断。这种方法的时间复杂度主要由排序步骤决定，为
(O(n \log n))，其中 (n) 是区间的数量，之后的遍历为 (O(n))，因此总体时间复杂度为 (O(n \log n))。

## C++

    
    
    // 函数定义，输入是一个二维向量intervals，每个子向量表示一个区间[starti, endi]
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // 首先对区间进行排序，根据每个区间的起始位置starti排序，使得处理合并时更加方便
        sort(intervals.begin(), intervals.end());
    
        // 定义结果向量ans，用于存储合并后的区间
        vector<vector<int>> ans;
    
        // 使用一个for循环遍历所有区间
        for (int i = 0; i < intervals.size();) {
            // t记录当前考察的区间的结束点endi
            int t = intervals[i][1];
    
            // j用于查找与当前区间可能重叠的后续区间
            int j = i + 1;
    
            // 如果后续区间的起始点小于或等于当前区间的结束点，则表示这两个区间有重叠
            while (j < intervals.size() && intervals[j][0] <= t) {
                // 更新当前考察的区间的结束点为当前区间和重叠区间的结束点的较大值
                t = max(t, intervals[j][1]);
                // 移动j到下一个区间
                j++;
            }
    
            // 将当前扩展后的区间添加到结果向量中
            ans.push_back({intervals[i][0], t});
            // 更新i为j，即跳过所有已经合并的区间，直接开始新一轮的合并
            i = j;
        }
    
        // 返回合并后的区间列表
        return ans;
    }
    

## Java

    
    
    class Solution {
        // 合并区间函数，输入是一个二维数组，每个子数组是[start, end]
        public int[][] merge(int[][] intervals) {
            // 首先对区间进行排序，根据每个区间的起始位置进行排序
            Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
    
            // 定义结果列表，用于存储合并后的区间
            List<int[]> ans = new ArrayList<>();
    
            // 使用for循环遍历所有区间
            for (int i = 0; i < intervals.length;) {
                // 获取当前区间的结束点
                int t = intervals[i][1];
    
                // j用于查找与当前区间可能重叠的后续区间
                int j = i + 1;
    
                // 检查是否有重叠区间
                while (j < intervals.length && intervals[j][0] <= t) {
                    // 更新结束点，如果有重叠，取较大值
                    t = Math.max(t, intervals[j][1]);
                    j++;
                }
    
                // 将合并后的区间加入结果列表
                ans.add(new int[]{intervals[i][0], t});
    
                // 更新i，跳过所有已经合并的区间
                i = j;
            }
    
            // 将结果列表转换为二维数组并返回
            return ans.toArray(new int[ans.size()][]);
        }
    }
    

## javaScript

    
    
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    var merge = function(intervals) {
        // 对区间按照起始位置进行排序
        intervals.sort((a, b) => a[0] - b[0]);
    
        // 结果数组，用来存储合并后的区间
        const merged = [];
    
        // 遍历排序后的区间数组
        for (let i = 0; i < intervals.length; i++) {
            // 如果结果数组为空，或者当前区间的起始位置大于结果数组中最后一个区间的结束位置
            // 则不重叠，直接将当前区间添加到结果数组
            if (merged.length === 0 || merged[merged.length - 1][1] < intervals[i][0]) {
                merged.push(intervals[i]);
            } else {
                // 否则，有重叠，合并区间
                // 更新结果数组中最后一个区间的结束位置为当前区间和最后一个区间结束位置的较大值
                merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], intervals[i][1]);
            }
        }
    
        // 返回合并后的区间数组
        return merged;
    };
    

## Python

    
    
     
    
    class Solution:
        # 合并区间函数，输入是一个二维列表，每个子列表是[start, end]
        def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            # 对区间进行排序，根据每个区间的起始位置
            intervals.sort(key=lambda x: x[0])
    
            # 定义结果列表，用于存储合并后的区间
            ans = []
    
            # 遍历所有区间
            i = 0
            while i < len(intervals):
                # 获取当前区间的结束点
                t = intervals[i][1]
    
                # j用于查找可能与当前区间重叠的后续区间
                j = i + 1
    
                # 检查是否有重叠区间
                while j < len(intervals) and intervals[j][0] <= t:
                    # 更新结束点，选择最大值
                    t = max(t, intervals[j][1])
                    j += 1
    
                # 将合并后的区间加入结果列表
                ans.append([intervals[i][0], t])
    
                # 更新i以跳过所有已合并的区间
                i = j
    
            # 返回合并后的不重叠区间
            return ans
    

#### 文章目录

  * 华为OD面试真题精选
  * 题目描述
  * 解题思路
  * C++
  * Java
  * javaScript
  * Python

![封面](https://i-blog.csdnimg.cn/blog_migrate/fe0e945c6dc7410e52666f1e8053a25e.png)

