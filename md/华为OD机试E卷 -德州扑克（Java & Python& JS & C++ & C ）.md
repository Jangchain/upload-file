#### 题目描述

五张牌，每张牌由牌大小和花色组成，牌大小2~10、J、Q、K、A，牌花色为红桃、黑桃、梅花、方块四种花色之一。

判断牌型:

牌型1，同花顺：同一花色的顺子，如红桃2红桃3红桃4红桃5红桃6。  
牌型2，四条：四张相同数字 + 单张，如红桃A黑桃A梅花A方块A + 黑桃K。  
牌型3，葫芦：三张相同数字 + 一对，如红桃5黑桃5梅花5 + 方块9梅花9。  
牌型4，同花：同一花色，如方块3方块7方块10方块J方块Q。  
牌型5，顺子：花色不一样的顺子，如红桃2黑桃3红桃4红桃5方块6。  
牌型6，三条：三张相同+两张单。

说明：

（1）五张牌里不会出现牌大小和花色完全相同的牌。  
（2）编号小的牌型较大，如同花顺比四条大，依次类推。  
（3）包含A的合法的顺子只有10 J Q K A和A 2 3 4 5;类似K A 2 3 4的序列不认为是顺子。

#### 输入描述

输入由5行组成，每行为一张牌大小和花色，牌大小为2~10、J、Q、K、A，花色分别用字符H、S、C、D表示红桃、黑桃、梅花、方块。

#### 输出描述

输出牌型序号，5张牌符合多种牌型时，取最大的牌型序号输出。

#### 用例

输入| 4 H  
5 S  
6 C  
7 D  
8 D  
---|---  
输出| 5  
说明| 4 5 6 7 8构成顺子，输出5  
输入| 9 S  
5 S  
6 S  
7 S  
8 S  
---|---  
输出| 1  
说明| 既是顺子又是同花，输出1，同花顺  
  
#### C++

    
    
    #include <vector>
    #include <set>
    #include <map>
    #include <algorithm>
    #include <iostream>
    using namespace std;
    
    // 判断是否为顺子
    bool isStraight(map<string, int>& cards, vector<string>& nums) {
        // 特判 A 2 3 4 5 的情况
        if (nums[0] == "2" && nums[1] == "3" && nums[2] == "4" && nums[3] == "5" && nums[4] == "A") return true;
    
        // 判断是否为普通的顺子
        for (int i = 1; i < nums.size(); i++) {
            const int num1 = cards[nums[i - 1]];
            const int num2 = cards[nums[i]];
    
            if (num1 + 1 != num2) return false;
        }
        return true;
    }
    
    // 判断是否为同花
    bool isFlush(vector<string>& colors) {
        // 利用 set 去重，如果只有一种花色，那么 set 的大小为 1
        return set<string>(colors.begin(), colors.end()).size() == 1;
    }
    
    // 判断是否为四条
    bool isFourOfAKind(vector<string>& nums) {
        map<string, int> count;
    
        // 统计每个数字出现的次数
        for (auto num : nums) {
            count[num]++;
        }
    
        // 如果只有两种数字，那么必须有一种数字出现了 4 次，另一种数字出现了 1 次
        if (count.size() == 2) {
            for (auto& [num, cnt] : count) {
                if (cnt == 4 || cnt == 1) return true;
            }
        }
        return false;
    }
    
    // 判断是否为葫芦
    bool isFullHouse(vector<string>& nums) {
        map<string, int> count;
    
        // 统计每个数字出现的次数
        for (auto num : nums) {
            count[num]++;
        }
    
        // 如果只有两种数字，那么必须有一种数字出现了 3 次，另一种数字出现了 2 次
        if (count.size() == 2) {
            for (auto& [num, cnt] : count) {
                if (cnt == 3 || cnt == 2) return true;
            }
        }
        return false;
    }
    
    // 判断是否为三条
    bool isThreeOfAKind(vector<string>& nums) {
        map<string, int> count;
    
        // 统计每个数字出现的次数
        for (auto num : nums) {
            count[num]++;
        }
    
        // 如果有三种数字，那么必须有一种数字出现了 3 次
        if (count.size() == 3) {
            for (auto& [num, cnt] : count) {
                if (cnt == 3) return true;
            }
        }
        return false;
    }
    
    // 获取牌型得分
    int getMaxScoreCards(vector<vector<string>>& cards) {
        // 定义每个数字对应的大小
        map<string, int> cardValues = {
            {"2", 2},
            {"3", 3},
            {"4", 4},
            {"5", 5},
            {"6", 6},
            {"7", 7},
            {"8", 8},
            {"9", 9},
            {"10", 10},
            {"J", 11},
            {"Q", 12},
            {"K", 13},
            {"A", 14},
        };
    
        vector<string> nums;
        vector<string> colors;
    
        // 分离数字和花色
        for (auto& card : cards) {
            nums.push_back(card[0]);
            colors.push_back(card[1]);
        }
    
        // 将数字排序，方便后续判断顺子
        sort(nums.begin(), nums.end(), [&](string a, string b) {
            return cardValues[a] < cardValues[b];
        });
    
        // 判断不同的牌型，按照题目要求返回不同的分数
        if (isStraight(cardValues, nums) && isFlush(colors)) {
            return 1;
        } else if (isFourOfAKind(nums)) {
            return 2;
        } else if (isFullHouse(nums)) {
            return 3;
        } else if (isFlush(colors)) {
            return 4;
        } else if (isStraight(cardValues, nums)) {
            return 5;
        } else if (isThreeOfAKind(nums)) {
            return 6;
        } else {
            return 0;
        }
    }
    
    int main() {
        vector<vector<string>> cards;
        string line;
    
        // 读入数据，每输入 5 行就计算一次分数并输出
        while (getline(cin, line)) {
            vector<string> nums;
            string num, color;
    
            for (int i = 0; i < line.size(); i++) {
                if (line[i] == ' ') {
                    nums.push_back(num);
                    num = "";
                } else {
                    num += line[i];
                }
            }
            nums.push_back(num);
    
            cards.push_back(nums);
    
            if (cards.size() == 5) {
                cout << getMaxScoreCards(cards) << endl;
                cards.clear();
            }
        }
    
        return 0;
    }
    

#### java

    
    
    import java.util.*;
    
    public class Main {
        // 判断是否为顺子
        public static boolean isStraight(Map<String, Integer> cards, List<String> nums) {
            // 特判 A 2 3 4 5 的情况
            if (nums.get(0).equals("2") && nums.get(1).equals("3") && nums.get(2).equals("4")
                    && nums.get(3).equals("5") && nums.get(4).equals("A")) {
                return true;
            }
    
            // 判断是否为普通的顺子
            for (int i = 1; i < nums.size(); i++) {
                int num1 = cards.get(nums.get(i - 1));
                int num2 = cards.get(nums.get(i));
    
                if (num1 + 1 != num2) {
                    return false;
                }
            }
            return true;
        }
    
        // 判断是否为同花
        public static boolean isFlush(List<String> colors) {
            // 利用 Set 去重，如果只有一种花色，那么 Set 的大小为 1
            return new HashSet<>(colors).size() == 1;
        }
    
        // 判断是否为四条
        public static boolean isFourOfAKind(List<String> nums) {
            Map<String, Integer> count = new HashMap<>();
    
            // 统计每个数字出现的次数
            for (String num : nums) {
                count.put(num, count.getOrDefault(num, 0) + 1);
            }
    
            // 如果只有两种数字，那么必须有一种数字出现了 4 次，另一种数字出现了 1 次
            if (count.size() == 2) {
                for (Map.Entry<String, Integer> entry : count.entrySet()) {
                    if (entry.getValue() == 4 || entry.getValue() == 1) {
                        return true;
                    }
                }
            }
            return false;
        }
    
        // 判断是否为葫芦
        public static boolean isFullHouse(List<String> nums) {
            Map<String, Integer> count = new HashMap<>();
    
            // 统计每个数字出现的次数
            for (String num : nums) {
                count.put(num, count.getOrDefault(num, 0) + 1);
            }
    
            // 如果只有两种数字，那么必须有一种数字出现了 3 次，另一种数字出现了 2 次
            if (count.size() == 2) {
                for (Map.Entry<String, Integer> entry : count.entrySet()) {
                    if (entry.getValue() == 3 || entry.getValue() == 2) {
                        return true;
                    }
                }
            }
            return false;
        }
    
        // 判断是否为三条
        public static boolean isThreeOfAKind(List<String> nums) {
            Map<String, Integer> count = new HashMap<>();
    
            // 统计每个数字出现的次数
            for (String num : nums) {
                count.put(num, count.getOrDefault(num, 0) + 1);
            }
    
            // 如果有三种数字，那么必须有一种数字出现了 3 次
            if (count.size() == 3) {
                for (Map.Entry<String, Integer> entry : count.entrySet()) {
                    if (entry.getValue() == 3) {
                        return true;
                    }
                }
            }
            return false;
        }
    
        // 获取牌型得分
        public static int getMaxScoreCards(List<List<String>> cards) {
            // 定义每个数字对应的大小
            Map<String, Integer> cardValues = new HashMap<>();
            cardValues.put("2", 2);
            cardValues.put("3", 3);
            cardValues.put("4", 4);
            cardValues.put("5", 5);
            cardValues.put("6", 6);
            cardValues.put("7", 7);
            cardValues.put("8", 8);
            cardValues.put("9", 9);
            cardValues.put("10", 10);
            cardValues.put("J", 11);
            cardValues.put("Q", 12);
            cardValues.put("K", 13);
            cardValues.put("A", 14);
    
            List<String> nums = new ArrayList<>();
            List<String> colors = new ArrayList<>();
    
            // 分离数字和花色
            for (List<String> card : cards) {
                nums.add(card.get(0));
                colors.add(card.get(1));
            }
    
            // 将数字排序，方便后续判断顺子
            Collections.sort(nums, (a, b) -> cardValues.get(a) - cardValues.get(b));
    
            // 判断不同的牌型，按照题目要求返回不同的分数
            if (isStraight(cardValues, nums) && isFlush(colors)) {
                return 1;
            } else if (isFourOfAKind(nums)) {
                return 2;
            } else if (isFullHouse(nums)) {
                return 3;
            } else if (isFlush(colors)) {
                return 4;
            } else if (isStraight(cardValues, nums)) {
                return 5;
            } else if (isThreeOfAKind(nums)) {
                return 6;
            } else {
                return 0;
            }
        }
    
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            List<List<String>> cards = new ArrayList<>();
    
            // 读入数据，每输入 5 行就计算一次分数并输出
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                List<String> nums = new ArrayList<>();
                String num = "";
                for (int i = 0; i < line.length(); i++) {
                    if (line.charAt(i) == ' ') {
                        nums.add(num);
                        num = "";
                    } else {
                        num += line.charAt(i);
                    }
                }
                nums.add(num);
    
                cards.add(nums);
    
                if (cards.size() == 5) {
                    System.out.println(getMaxScoreCards(cards));
                    cards.clear();
                }
            }
    
            scanner.close();
        }
    }
    

#### javascript

    
    
    const readline = require('readline');
    
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    // 判断是否为顺子
    function isStraight(cards, nums) {
      // 特判 A 2 3 4 5 的情况
      if (nums[0] === "2" && nums[1] === "3" && nums[2] === "4" && nums[3] === "5" && nums[4] === "A") return true;
    
      // 判断是否为普通的顺子
      for (let i = 1; i < nums.length; i++) {
        const num1 = cards[nums[i - 1]];
        const num2 = cards[nums[i]];
    
        if (num1 + 1 !== num2) return false;
      }
      return true;
    }
    
    // 判断是否为同花
    function isFlush(colors) {
      // 利用 Set 去重，如果只有一种花色，那么 Set 的大小为 1
      return new Set(colors).size === 1;
    }
    
    // 判断是否为四条
    function isFourOfAKind(nums) {
      const count = {};
    
      // 统计每个数字出现的次数
      for (const num of nums) {
        count[num] = count[num] ? count[num] + 1 : 1;
      }
    
      // 如果只有两种数字，那么必须有一种数字出现了 4 次，另一种数字出现了 1 次
      if (Object.keys(count).length === 2) {
        for (const [num, cnt] of Object.entries(count)) {
          if (cnt === 4 || cnt === 1) return true;
        }
      }
      return false;
    }
    
    // 判断是否为葫芦
    function isFullHouse(nums) {
      const count = {};
    
      // 统计每个数字出现的次数
      for (const num of nums) {
        count[num] = count[num] ? count[num] + 1 : 1;
      }
    
      // 如果只有两种数字，那么必须有一种数字出现了 3 次，另一种数字出现了 2 次
      if (Object.keys(count).length === 2) {
        for (const [num, cnt] of Object.entries(count)) {
          if (cnt === 3 || cnt === 2) return true;
        }
      }
      return false;
    }
    
    // 判断是否为三条
    function isThreeOfAKind(nums) {
      const count = {};
    
      // 统计每个数字出现的次数
      for (const num of nums) {
        count[num] = count[num] ? count[num] + 1 : 1;
      }
    
      // 如果有三种数字，那么必须有一种数字出现了 3 次
      if (Object.keys(count).length === 3) {
        for (const [num, cnt] of Object.entries(count)) {
          if (cnt === 3) return true;
        }
      }
      return false;
    }
    
    // 获取牌型得分
    function getMaxScoreCards(cards) {
      // 定义每个数字对应的大小
      const cardValues = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
      };
    
      const nums = [];
      const colors = [];
    
      // 分离数字和花色
      for (const card of cards) {
        nums.push(card[0]);
        colors.push(card[1]);
      }
    
      // 将数字排序，方便后续判断顺子
      nums.sort((a, b) => cardValues[a] - cardValues[b]);
    
      // 判断不同的牌型，按照题目要求返回不同的分数
      if (isStraight(cardValues, nums) && isFlush(colors)) {
        return 1;
      } else if (isFourOfAKind(nums)) {
        return 2;
      } else if (isFullHouse(nums)) {
        return 3;
      } else if (isFlush(colors)) {
        return 4;
      } else if (isStraight(cardValues, nums)) {
        return 5;
      } else if (isThreeOfAKind(nums)) {
        return 6;
      } else {
        return 0;
      }
    }
    
    const cards = [];
    
    rl.on('line', (line) => {
      const nums = line.trim().split(' ');
    
      cards.push(nums);
    
      if (cards.length === 5) {
        console.log(getMaxScoreCards(cards));
        cards.length = 0;
      }
    });
    

#### python

    
    
    import sys
    
    # 判断是否为顺子
    def isStraight(cards, nums):
        # 特判 A 2 3 4 5 的情况
        if nums[0] == "2" and nums[1] == "3" and nums[2] == "4" and nums[3] == "5" and nums[4] == "A":
            return True
    
        # 判断是否为普通的顺子
        for i in range(1, len(nums)):
            num1 = cards[nums[i - 1]]
            num2 = cards[nums[i]]
    
            if num1 + 1 != num2:
                return False
    
        return True
    
    # 判断是否为同花
    def isFlush(colors):
        # 利用 set 去重，如果只有一种花色，那么 set 的大小为 1
        return len(set(colors)) == 1
    
    # 判断是否为四条
    def isFourOfAKind(nums):
        count = {}
    
        # 统计每个数字出现的次数
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        # 如果只有两种数字，那么必须有一种数字出现了 4 次，另一种数字出现了 1 次
        if len(count) == 2:
            for num, cnt in count.items():
                if cnt == 4 or cnt == 1:
                    return True
    
        return False
    
    # 判断是否为葫芦
    def isFullHouse(nums):
        count = {}
    
        # 统计每个数字出现的次数
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        # 如果只有两种数字，那么必须有一种数字出现了 3 次，另一种数字出现了 2 次
        if len(count) == 2:
            for num, cnt in count.items():
                if cnt == 3 or cnt == 2:
                    return True
    
        return False
    
    # 判断是否为三条
    def isThreeOfAKind(nums):
        count = {}
    
        # 统计每个数字出现的次数
        for num in nums:
            count[num] = count.get(num, 0) + 1
    
        # 如果有三种数字，那么必须有一种数字出现了 3 次
        if len(count) == 3:
            for num, cnt in count.items():
                if cnt == 3:
                    return True
    
        return False
    
    # 获取牌型得分
    def getMaxScoreCards(cards):
        # 定义每个数字对应的大小
        cardValues = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
    
        nums = []
        colors = []
    
        # 分离数字和花色
        for card in cards:
            nums.append(card[0])
            colors.append(card[1])
    
        # 将数字排序，方便后续判断顺子
        nums.sort(key=lambda x: cardValues[x])
    
        # 判断不同的牌型，按照题目要求返回不同的分数
        if isStraight(cardValues, nums) and isFlush(colors):
            return 1
        elif isFourOfAKind(nums):
            return 2
        elif isFullHouse(nums):
            return 3
        elif isFlush(colors):
            return 4
        elif isStraight(cardValues, nums):
            return 5
        elif isThreeOfAKind(nums):
            return 6
        else:
            return 0
    
    if __name__ == '__main__':
        cards = []
    
        # 读入数据，每输入 5 行就计算一次分数并输出
        for line in sys.stdin:
            nums = line.strip().split()
    
            cards.append(nums)
    
            if len(cards) == 5:
                print(getMaxScoreCards(cards))
                cards.clear()
    

#### 文章目录

  *     *       * 题目描述
      * 输入描述
      * 输出描述
      * 用例
      * C++
      * java
      * javascript
      * python

![fengmian](https://img-
blog.csdnimg.cn/img_convert/1d2f33ed8cf2fb1b9a4fe09513f7aa94.png)

