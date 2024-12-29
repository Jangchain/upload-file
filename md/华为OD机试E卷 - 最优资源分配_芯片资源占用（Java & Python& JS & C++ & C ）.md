## 最新华为OD机试

真题目录：[点击查看目录](https://blog.csdn.net/banxia_frontend/article/details/129640773)  
华为OD面试真题精选：[点击立即查看](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 题目描述

某块业务芯片最小容量单位为1.25G，总容量为M*1.25G，对该芯片资源编号为1，2，…，M。该芯片支持3种不同的配置，分别为A、B、C。

  * 配置A：占用容量为 1.25 * 1 = 1.25G
  * 配置B：占用容量为 1.25 * 2 = 2.5G
  * 配置C：占用容量为 1.25 * 8 = 10G

某块板卡上集成了N块上述芯片，对芯片编号为1，2，…，N，各个芯片之间彼此独立，不能跨芯片占用资源。

给定板卡上芯片数量N、每块芯片容量M、用户按次序配置后，请输出芯片资源占用情况，保证消耗的芯片数量最少。

资源分配规则：按照芯片编号从小到大分配所需资源，芯片上资源如果被占用标记为1，没有被占用标记为0.

用户配置序列：用户配置是按次序依次配置到芯片中，如果用户配置序列种某个配置超过了芯片总容量，丢弃该配置，继续遍历用户后续配置。

## 输入描述

M：每块芯片容量为 M * 1.25G，取值范围为：1~256

N：每块板卡包含芯片数量，取值范围为1~32

用户配置序列：例如ACABA，长度不超过1000

## 输出描述

板卡上每块芯片的占用情况

#### 备注

用户配置是按次序依次配置到芯片中，如果用户配置序列种某个配置超过了芯片总容量，丢弃该配置，继续遍历用户后续配置。

## 示例1

输入

    
    
    8
    2
    ACABA
    

输出

    
    
    11111000
    11111111
    

说明

> 用户第1个配置A：占用第1块芯片第1个资源，芯片占用情况为：  
>  10000000  
>  00000000  
>  用户第2个配置C：第1块芯片剩余8.75G，配置C容量不够，只能占用第2块芯片，芯片占用情况为：  
>  10000000  
>  11111111  
>  用户第3个配置A：第1块芯片剩余8.75G，还能继续配置，占用第1块芯片第2个资源，芯片占用情况为：  
>  11000000  
>  11111111  
>
> 用户第4个配置B：第1块芯片剩余7.[5G](https://so.csdn.net/so/search?q=5G&spm=1001.2101.3001.7020)，还能继续配置，占用第1块芯片第3、4个资源，芯片占用情况为：  
>  11110000  
>  11111111  
>  用户第5个配置A：第1块芯片剩余5G，还能继续配置，占用第1块芯片第5个资源，芯片占用情况为：  
>  11110000  
>  11111111

## 示例2

输入

    
    
    8
    2
    ACBCB
    

输出

    
    
    11111000
    11111111
    

说明

> 用户第1个配置A：占用第1块芯片第1个资源，芯片占用情况为：  
>  10000000  
>  00000000  
>  用户第2个配置C：第1块芯片剩余8.75G，配置C容量不够，只能占用第2块芯片，芯片占用情况为：  
>  10000000  
>  11111111  
>  用户第3个配置B：第1块芯片剩余8.75G，还能继续配置，占用第1块芯片第2、3个资源，芯片占用情况为：  
>  11100000  
>  11111111  
>  用户第4个配置C：芯片资源不够，丢弃配置，继续下一个配置，本次配置后芯片占用情况保持不变：  
>  11100000  
>  11111111  
>  用户第5个配置B：第1块芯片剩余6.25G,还能继续配置，占用第1块芯片第4、5个资源，芯片占用情况为：  
>  11111000  
>  11111111

## 解题思路

以用例1解释一下：

用例1的前两行输入表示：

板卡上有N=2个芯片，而每个芯片有8个单位容量，因此对应如下：

> 00000000
>
> 00000000

其中每个0代表一个单位容量，而一个芯片有8单位容量，因此第一排8个0代表一个芯片的总容量，第二排8个0代表另一个芯片的总容量。

#### 代码思路

首先，读入每块芯片的容量和板卡上芯片的数量，以及用户配置序列。然后，初始化每块板卡的总容量为芯片数量 *
芯片容量。接下来，定义一个字典，将用户配置序列中的字符映射到对应的容量。遍历用户配置序列，按照芯片编号从小到大分配所需资源。具体地，对于每个配置，遍历每块板卡，找到第一个容量足够的板卡，将其对应的总容量减去所需资源。最后，输出每块芯片的占用情况。对于每块芯片，计算已用和未用容量，构造字符串表示每块芯片的占用情况。

## Java

    
    
    import java.util.*;
    
    public class Main {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
    
            // 输入每块芯片的容量和板卡上芯片的数量
            int chip_capacity = scanner.nextInt();
            int chip_count = scanner.nextInt();
    
            // 输入用户配置序列
            String sequence = scanner.next();
    
            // 初始化每块板卡的总容量
            List<Double> board_card = new ArrayList<>(Collections.nCopies(chip_count, chip_capacity * 1.25));
    
            // 遍历用户配置序列，按照芯片编号从小到大分配所需资源
            for (int i = 0; i < sequence.length(); i++) {
                char config = sequence.charAt(i);
                double need;
    
                // 直接计算每种配置的需求
                switch (config) {
                    case 'A':
                        need = 1.25 * 1; // 1.25G
                        break;
                    case 'B':
                        need = 1.25 * 2; // 2.5G
                        break;
                    case 'C':
                        need = 1.25 * 8; // 10G
                        break;
                    default:
                        continue; // 如果是未知配置，跳过
                }
    
                // 分配资源
                for (int j = 0; j < chip_count; j++) {
                    if (board_card.get(j) >= need) {
                        board_card.set(j, board_card.get(j) - need);
                        break;
                    }
                }
            }
    
            // 输出每块芯片的占用情况
            for (int i = 0; i < chip_count; i++) {
                // 计算每块芯片的已用和未用容量
                int un_used = (int) (board_card.get(i) / 1.25);
                int used = chip_capacity - un_used;
    
                // 构造字符串表示每块芯片的占用情况
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < used; j++) {
                    sb.append('1');
                }
                for (int k = 0; k < un_used; k++) {
                    sb.append('0');
                }
                System.out.println(sb.toString());
            }
    
            scanner.close();
        }
    }
    

## Python

    
    
     
    import sys
    
    def main():
        # 输入每块芯片的容量和板卡上芯片的数量
        chip_capacity = int(input())  # 每块芯片的容量
        chip_count = int(input())      # 板卡上芯片的数量
    
        # 输入用户配置序列
        sequence = input()  # 用户配置序列
    
        # 初始化每块板卡的总容量
        board_card = [chip_capacity * 1.25] * chip_count
    
        # 遍历用户配置序列，按照芯片编号从小到大分配所需资源
        for config in sequence:
            if config == 'A':
                need = 1.25 * 1  # 1.25G
            elif config == 'B':
                need = 1.25 * 2  # 2.5G
            elif config == 'C':
                need = 1.25 * 8  # 10G
            else:
                continue  # 如果是未知配置，跳过
    
            # 分配资源
            for j in range(chip_count):
                if board_card[j] >= need:
                    board_card[j] -= need  # 减去所需容量
                    break
    
        # 输出每块芯片的占用情况
        for i in range(chip_count):
            un_used = int(board_card[i] / 1.25)  # 计算未使用的容量
            used = chip_capacity - un_used  # 计算已使用的容量
    
            # 构造字符串表示每块芯片的占用情况
            result = '1' * used + '0' * un_used  # 使用 '1' 表示已占用，'0' 表示未占用
            print(result)  # 输出结果
    
    if __name__ == "__main__":
        main()
    

## JavaScript

    
    
    // Node.js 版本
    const readline = require('readline');
    
    // 创建接口以读取输入
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    let chip_capacity;
    let chip_count;
    rl.on('line', (line) => {
        // 第一次输入：每块芯片的容量
        if (!chip_capacity) {
            chip_capacity = parseInt(line); // 读取芯片容量
            return;
        }
        // 第二次输入：板卡上芯片的数量
        if (!chip_count) {
            chip_count = parseInt(line); // 读取芯片数量
            return;
        }
        // 第三次输入：用户配置序列
        sequence = line; // 读取用户配置序列
        rl.close(); // 关闭输入接口
    
        // 初始化每块板卡的总容量
        const board_card = new Array(chip_count).fill(chip_capacity * 1.25);
    
        // 遍历用户配置序列，按照芯片编号从小到大分配所需资源
        for (let i = 0; i < sequence.length; i++) {
            let need;
            switch (sequence[i]) {
                case 'A':
                    need = 1.25 * 1; // 1.25G
                    break;
                case 'B':
                    need = 1.25 * 2; // 2.5G
                    break;
                case 'C':
                    need = 1.25 * 8; // 10G
                    break;
                default:
                    continue; // 如果是未知配置，跳过
            }
    
            // 分配资源
            for (let j = 0; j < chip_count; j++) {
                if (board_card[j] >= need) {
                    board_card[j] -= need; // 减去所需容量
                    break;
                }
            }
        }
    
        // 输出每块芯片的占用情况
        for (let i = 0; i < chip_count; i++) {
            const un_used = Math.floor(board_card[i] / 1.25); // 计算未使用的容量
            const used = chip_capacity - un_used; // 计算已使用的容量
    
            // 构造字符串表示每块芯片的占用情况
            const result = '1'.repeat(used) + '0'.repeat(un_used); // 使用 '1' 表示已占用，'0' 表示未占用
            console.log(result); // 输出结果
        }
    });
    

## C++

    
    
    #include <iostream>
    #include <vector>
    #include <string>
    
    using namespace std;
    
    int main() {
        // 输入每块芯片的容量和板卡上芯片的数量
        int chip_capacity, chip_count;
        cin >> chip_capacity >> chip_count;
    
        // 输入用户配置序列
        string sequence;
        cin >> sequence;
    
        // 初始化每块板卡的总容量
        vector<double> board_card(chip_count, chip_capacity * 1.25);
    
        // 遍历用户配置序列，按照芯片编号从小到大分配所需资源
        for (char config : sequence) {
            double need;
            switch (config) {
                case 'A':
                    need = 1.25 * 1; // 1.25G
                    break;
                case 'B':
                    need = 1.25 * 2; // 2.5G
                    break;
                case 'C':
                    need = 1.25 * 8; // 10G
                    break;
                default:
                    continue; // 如果是未知配置，跳过
            }
    
            // 分配资源
            for (int j = 0; j < chip_count; j++) {
                if (board_card[j] >= need) {
                    board_card[j] -= need; // 减去所需容量
                    break;
                }
            }
        }
    
        // 输出每块芯片的占用情况
        for (int i = 0; i < chip_count; i++) {
            int un_used = static_cast<int>(board_card[i] / 1.25); // 计算未使用的容量
            int used = chip_capacity - un_used; // 计算已使用的容量
    
            // 构造字符串表示每块芯片的占用情况
            string result(used, '1'); // 使用 '1' 表示已占用
            result.append(un_used, '0'); // 使用 '0' 表示未占用
            cout << result << endl; // 输出结果
        }
    
        return 0;
    }
    

## C语言

    
    
    #include <stdio.h>
    
    int main() {
        // 输入每块芯片的容量和板卡上芯片的数量
        int chip_capacity, chip_count;
        scanf("%d %d", &chip_capacity, &chip_count);
    
        // 输入用户配置序列
        char sequence[1001]; // 假设配置序列不超过1000个字符
        scanf("%s", sequence);
    
        // 初始化每块板卡的总容量
        double board_card[32]; // 假设最多有32块芯片
        for (int i = 0; i < chip_count; i++) {
            board_card[i] = chip_capacity * 1.25;
        }
    
        // 遍历用户配置序列，按照芯片编号从小到大分配所需资源
        for (int i = 0; sequence[i] != '\0'; i++) {
            double need;
            switch (sequence[i]) {
                case 'A':
                    need = 1.25 * 1; // 1.25G
                    break;
                case 'B':
                    need = 1.25 * 2; // 2.5G
                    break;
                case 'C':
                    need = 1.25 * 8; // 10G
                    break;
                default:
                    continue; // 如果是未知配置，跳过
            }
    
            // 分配资源
            for (int j = 0; j < chip_count; j++) {
                if (board_card[j] >= need) {
                    board_card[j] -= need; // 减去所需容量
                    break;
                }
            }
        }
    
        // 输出每块芯片的占用情况
        for (int i = 0; i < chip_count; i++) {
            int un_used = (int)(board_card[i] / 1.25); // 计算未使用的容量
            int used = chip_capacity - un_used; // 计算已使用的容量
    
            // 输出每块芯片的占用情况
            for (int k = 0; k < used; k++) {
                putchar('1'); // 输出 '1' 表示已占用
            }
            for (int k = 0; k < un_used; k++) {
                putchar('0'); // 输出 '0' 表示未占用
            }
            putchar('\n'); // 换行
        }
    
        return 0;
    }
    

![fengmian](https://img-
blog.csdnimg.cn/img_convert/9e3e34cc0dbdcb2f0810f5c600a0e8fc.png)

