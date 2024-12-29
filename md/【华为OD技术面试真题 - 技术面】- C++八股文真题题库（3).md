## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 选择 UDP 而非 TCP 的应用场景
  *     *       * UDP 与 TCP 的基本区别
      * 选择 UDP 而非 TCP 的应用场景
  * UDP协议传输时出现丢包如何解决
  *     *       * 1\. **应用层实现重传机制**
      * 2\. **序列号和数据包重排序**
      * 3\. **使用 FEC（前向纠错编码）**
      * 4\. **网络质量监控和自适应传输**
  * CP/IP协议相对安全，请说说为什么安全
  * 冒泡排序的核心代码
  *     *       * 冒泡排序的核心代码
      * 代码解析
  * 关键字staic和const的用法
  *     *       * `static` 关键字
      * `static` 示例代码
      * `const` 关键字
      * `const` 示例代码
  * 链表与数组的区别
  *     * 1\. 内存管理
    * 2\. 访问方式
    * 3\. 插入和删除操作
    * 4\. 内存使用效率
    * 5\. 简单示例代码
  * TCP/IP协议相对UDP安全，请说说为什么安全
  *     *       *         * 1\. 连接性和状态性
        * 2\. 数据传输的可靠性
        * 3\. 数据完整性和顺序
        * 4\. 流量控制和拥塞控制
        * 5\. 应用场景

## 选择 UDP 而非 TCP 的应用场景

#### UDP 与 TCP 的基本区别

  1. **连接性** ：

     * **TCP** ：面向连接的协议，在发送数据前需要建立连接（三次握手），保证数据的可靠传输。
     * **UDP** ：无连接的协议，不需要建立连接即可发送数据，减少了连接建立的开销。
  2. **可靠性** ：

     * **TCP** ：提供可靠的传输服务，数据传输过程中有确认机制、序列号、重传控制，确保数据按顺序且无误地到达。
     * **UDP** ：不保证数据的可靠性，没有确认机制、重传控制、流量控制，因此数据可能丢失、重复或乱序。
  3. **流量控制与拥塞控制** ：

     * **TCP** ：具有流量控制和拥塞控制机制，防止网络拥堵，提高传输效率。
     * **UDP** ：没有流量控制和拥塞控制机制，适用于对实时性要求高的应用。
  4. **速度与开销** ：

     * **TCP** ：由于提供可靠传输，需要更多的头部信息和控制机制，开销较大，传输速度相对较慢。
     * **UDP** ：头部信息少，没有连接建立和控制机制，开销小，传输速度快。

#### 选择 UDP 而非 TCP 的应用场景

  1. **实时应用** ：

     * **VoIP（网络电话）、视频会议、在线游戏** ：这些应用对实时性要求高，数据延迟敏感。即使数据包丢失，也能继续传输，而不需要重传数据包。因此，UDP 适合此类应用。
  2. **广播和多播** ：

     * **实时流媒体** ：例如直播视频、实时数据分发等，需要将数据传输给多个接收者。UDP 支持广播和多播，可以高效地实现一对多的通信。
  3. **简单请求响应协议** ：

     * **DNS 查询** ：域名系统（DNS）查询通常采用 UDP，因为请求和响应都很小且简单，UDP 的低开销和快速响应更为合适。
  4. **局域网中的高效通信** ：

     * **网络文件传输、流控制协议（如 TFTP）** ：在局域网内，网络环境相对稳定，丢包率低，采用 UDP 可以提高传输效率。

## UDP协议传输时出现丢包如何解决

#### 1\. **应用层实现重传机制**

**原理** ：由于 UDP 本身不提供重传机制，丢包后数据无法自动重发。可以在应用层添加确认和重传逻辑，确保数据可靠传输。

**实现方法** ：

  * **发送方** ：每发送一个数据包后，等待接收方的确认（ACK）。
  * **接收方** ：收到数据包后，发送确认回执（ACK）给发送方。
  * **重传逻辑** ：如果发送方在一定时间内没有收到 ACK，则重传该数据包，直到收到确认或达到重传次数上限。

**代码示例** ：

    
    
    #include <iostream>
    #include <chrono>
    #include <thread>
    #include <unordered_map>
    #include <boost/asio.hpp>
    
    using boost::asio::ip::udp;
    
    const int max_retries = 5;
    const int timeout_ms = 1000;
    
    void send_with_retransmission(udp::socket& socket, const udp::endpoint& endpoint, const std::string& message) {
        std::unordered_map<int, bool> ack_received;
        for (int i = 0; i < max_retries; ++i) {
            socket.send_to(boost::asio::buffer(message), endpoint);
    
            // Wait for ACK with timeout
            boost::asio::deadline_timer timer(socket.get_io_service());
            timer.expires_from_now(boost::posix_time::milliseconds(timeout_ms));
            timer.async_wait([&](const boost::system::error_code& error) {
                if (error != boost::asio::error::operation_aborted) {
                    ack_received[i] = false;
                }
            });
    
            // Check for ACK
            char ack_buffer[128];
            udp::endpoint sender_endpoint;
            socket.async_receive_from(boost::asio::buffer(ack_buffer), sender_endpoint, [&](const boost::system::error_code& error, std::size_t) {
                if (!error) {
                    ack_received[i] = true;
                    timer.cancel();
                }
            });
    
            socket.get_io_service().run();
            socket.get_io_service().reset();
    
            if (ack_received[i]) {
                std::cout << "ACK received for message: " << message << std::endl;
                return;
            }
        }
        std::cout << "Failed to receive ACK after " << max_retries << " attempts" << std::endl;
    }
    
    int main() {
        boost::asio::io_service io_service;
        udp::socket socket(io_service, udp::endpoint(udp::v4(), 0));
        udp::endpoint endpoint(boost::asio::ip::address::from_string("127.0.0.1"), 12345);
    
        std::string message = "Hello, world!";
        send_with_retransmission(socket, endpoint, message);
    
        return 0;
    }
    

#### 2\. **序列号和数据包重排序**

**原理** ：由于 UDP 数据包可能乱序到达，可以给每个数据包添加序列号，接收方根据序列号重排序数据包，确保数据按正确顺序处理。

**实现方法** ：

  * **发送方** ：给每个数据包附加一个递增的序列号。
  * **接收方** ：根据序列号排序接收到的数据包，丢弃重复的或过期的数据包。

**代码示例** ：

    
    
    #include <iostream>
    #include <vector>
    #include <unordered_map>
    #include <algorithm>
    
    struct Packet {
        int sequence_number;
        std::string data;
    };
    
    void receive_and_reorder_packets(std::vector<Packet>& received_packets) {
        std::unordered_map<int, Packet> packet_map;
        for (const auto& packet : received_packets) {
            packet_map[packet.sequence_number] = packet;
        }
    
        std::vector<int> sequence_numbers;
        for (const auto& entry : packet_map) {
            sequence_numbers.push_back(entry.first);
        }
    
        std::sort(sequence_numbers.begin(), sequence_numbers.end());
    
        std::cout << "Reordered packets: " << std::endl;
        for (const auto& seq_num : sequence_numbers) {
            std::cout << "Packet " << seq_num << ": " << packet_map[seq_num].data << std::endl;
        }
    }
    
    int main() {
        std::vector<Packet> received_packets = {
            {2, "Packet 2 data"},
            {1, "Packet 1 data"},
            {3, "Packet 3 data"},
            {5, "Packet 5 data"},
            {4, "Packet 4 data"}
        };
    
        receive_and_reorder_packets(received_packets);
    
        return 0;
    }
    

#### 3\. **使用 FEC（前向纠错编码）**

**原理** ：通过发送冗余数据包来纠正丢失的数据包。即使部分数据包丢失，接收方仍能重建原始数据。

**实现方法** ：

  * **发送方** ：使用 FEC 算法生成冗余数据包，并与原始数据包一起发送。
  * **接收方** ：使用接收到的原始数据包和冗余数据包来恢复丢失的数据包。

#### 4\. **网络质量监控和自适应传输**

**原理** ：实时监控网络质量，根据网络状况动态调整传输速率和数据包大小，降低丢包率。

**实现方法** ：

  * **发送方** ：根据接收方反馈的网络状况，调整传输参数，如减少数据包大小或降低发送速率。
  * **接收方** ：定期向发送方反馈网络质量信息，如丢包率和延迟。

## CP/IP协议相对安全，请说说为什么安全

## 冒泡排序的核心代码

#### 冒泡排序的核心代码

    
    
    #include <iostream>
    #include <vector>
    
    // 冒泡排序函数
    void bubbleSort(std::vector<int>& arr) {
        int n = arr.size();
        for (int i = 0; i < n - 1; ++i) {
            // 提前退出标志位
            bool swapped = false;
            for (int j = 0; j < n - 1 - i; ++j) {
                if (arr[j] > arr[j + 1]) {
                    // 交换相邻元素
                    std::swap(arr[j], arr[j + 1]);
                    swapped = true;
                }
            }
            // 如果没有交换操作，说明数组已排序，提前退出
            if (!swapped) break;
        }
    }
    
    // 主函数进行测试
    int main() {
        std::vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
        
        std::cout << "未排序数组: ";
        for (int num : arr) std::cout << num << " ";
        std::cout << std::endl;
        
        bubbleSort(arr);
        
        std::cout << "排序后数组: ";
        for (int num : arr) std::cout << num << " ";
        std::cout << std::endl;
        
        return 0;
    }
    

#### 代码解析

  1. **外层循环** ：控制遍历次数，共进行  n − 1 n-1 n−1 次遍历，因为最后一次遍历时，只剩下一个元素，无需再比较。
  2. **内层循环** ：进行相邻元素的比较和交换，每次遍历结束后，当前最大的元素会被移动到未排序部分的末尾。
  3. **提前退出标志位`swapped`**：用于优化算法，如果在某次遍历中没有发生交换，说明数组已经有序，可以提前退出循环。

## 关键字staic和const的用法

#### `static` 关键字

  1. **在类中的静态成员** ：

     * **静态数据成员** ：属于类本身而不是类的任何一个对象。所有对象共享同一个静态数据成员。
     * **静态成员函数** ：只能访问静态数据成员和静态成员函数，不依赖于任何对象实例。
  2. **在函数中的静态变量** ：

     * 函数内的静态变量在函数调用之间保持其值。它只在第一次调用时初始化，后续调用中不会再初始化。
  3. **文件作用域内的静态变量** ：

     * 静态变量在声明的源文件内可见，其他文件无法访问。

#### `static` 示例代码

    
    
    #include <iostream>
    
    class Example {
    public:
        static int staticVar;
        static void staticFunction() {
            std::cout << "Static Function. staticVar = " << staticVar << std::endl;
        }
    };
    
    int Example::staticVar = 0; // 初始化静态数据成员
    
    void functionWithStatic() {
        static int count = 0; // 函数内静态变量
        count++;
        std::cout << "Static variable in function: " << count << std::endl;
    }
    
    int main() {
        Example::staticVar = 5;
        Example::staticFunction(); // 输出: Static Function. staticVar = 5
        
        functionWithStatic(); // 输出: Static variable in function: 1
        functionWithStatic(); // 输出: Static variable in function: 2
    
        return 0;
    }
    

#### `const` 关键字

  1. **常量变量** ：

     * 声明后不能修改其值。
  2. **常量指针和指针常量** ：

     * 常量指针：指针所指向的值不能通过该指针修改。
     * 指针常量：指针本身不能修改，但指向的值可以修改。
  3. **常量成员函数** ：

     * 不能修改类的任何数据成员，保证成员函数的只读特性。
  4. **常量参数** ：

     * 保证传递给函数的参数在函数内部不会被修改。

#### `const` 示例代码

    
    
    #include <iostream>
    
    class ConstExample {
    public:
        const int constVar; // 常量成员变量
    
        ConstExample(int val) : constVar(val) {} // 初始化常量成员变量
    
        void display() const { // 常量成员函数
            std::cout << "constVar = " << constVar << std::endl;
        }
    };
    
    void constPointerExample() {
        int value = 10;
        const int* ptr = &value; // 常量指针，不能通过 ptr 修改 value 的值
        // *ptr = 20; // 错误
    
        int* const ptrConst = &value; // 指针常量，不能修改 ptrConst 本身
        *ptrConst = 20; // 正确
        // ptrConst = nullptr; // 错误
    }
    
    void constParameter(const int param) {
        // param = 10; // 错误，不能修改常量参数
        std::cout << "constParameter: " << param << std::endl;
    }
    
    int main() {
        ConstExample example(42);
        example.display(); // 输出: constVar = 42
    
        constPointerExample();
    
        constParameter(5);
    
        return 0;
    }
    

## 链表与数组的区别

### 1\. 内存管理

  * **数组** ：数组在内存中占用连续的内存块。在声明时必须指定其大小，大小固定不变。数组的内存分配通常在栈上（对于静态数组）或堆上（对于动态数组）。
  * **链表** ：链表的节点在内存中不需要是连续的，每个节点通过指针连接到下一个节点。链表的大小可以动态变化，节点的内存通常在堆上分配。

### 2\. 访问方式

  * **数组** ：支持随机访问，可以通过索引在  O ( 1 ) O(1) O(1) 时间内访问任何元素。
  * **链表** ：不支持随机访问，需要从头节点开始，顺序遍历链表来找到特定位置的元素，访问时间为  O ( n ) O(n) O(n)。

### 3\. 插入和删除操作

  * **数组** ：在数组中插入或删除元素需要移动其他元素，因此插入和删除的平均时间复杂度为  O ( n ) O(n) O(n)。在末尾插入元素的平均时间复杂度为  O ( 1 ) O(1) O(1)。
  * **链表** ：在链表中插入或删除节点只需要调整指针，不需要移动其他元素，时间复杂度为  O ( 1 ) O(1) O(1)。但是，找到插入或删除位置需要遍历链表，时间复杂度为  O ( n ) O(n) O(n)。

### 4\. 内存使用效率

  * **数组** ：由于数组大小固定，因此可能会造成内存浪费或不足。
  * **链表** ：链表节点动态分配内存，内存使用更灵活，但每个节点需要额外的指针存储空间，增加了内存开销。

### 5\. 简单示例代码

**数组示例** ：

    
    
    #include <iostream>
    
    int main() {
        int arr[5] = {1, 2, 3, 4, 5}; // 定义一个大小为5的静态数组
    
        // 访问数组元素
        std::cout << "Array elements: ";
        for(int i = 0; i < 5; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;
    
        return 0;
    }
    

**链表示例** ：

    
    
    #include <iostream>
    
    struct Node {
        int data;
        Node* next;
        Node(int val) : data(val), next(nullptr) {}
    };
    
    void insertAtHead(Node*& head, int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }
    
    void display(Node* head) {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
    
    int main() {
        Node* head = nullptr;
        
        insertAtHead(head, 1);
        insertAtHead(head, 2);
        insertAtHead(head, 3);
    
        std::cout << "Linked list elements: ";
        display(head);
    
        // 释放链表内存
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    
        return 0;
    }
    

## TCP/IP协议相对UDP安全，请说说为什么安全

##### 1\. 连接性和状态性

  * **TCP（Transmission Control Protocol）** ：TCP是面向连接的协议，它在通信之前需要建立一个连接（三次握手）。在数据传输过程中，TCP会维护一个连接状态，包括发送和接收的窗口、序列号等，确保数据按顺序、无误地传输。
  * **UDP（User Datagram Protocol）** ：UDP是无连接的协议，它不建立连接，数据报文的发送是独立的，接收方无法知道数据报文是否丢失或按顺序接收。

##### 2\. 数据传输的可靠性

  * **TCP** ：TCP通过确认机制（ACK）来确保数据包的可靠传输。如果数据包在传输过程中丢失，发送方会重新发送该数据包。此外，TCP还具有流量控制和拥塞控制机制，确保数据传输的稳定和高效。
  * **UDP** ：UDP不提供数据包的重传机制，也没有流量控制和拥塞控制。数据包在传输过程中可能会丢失、重复或乱序，接收方需要自行处理这些问题。

##### 3\. 数据完整性和顺序

  * **TCP** ：TCP保证数据包按发送顺序到达接收方，通过序列号和确认号机制确保数据的完整性和顺序。
  * **UDP** ：UDP不保证数据包按顺序到达，数据包可能会乱序到达接收方。UDP也没有内置的机制来检查数据的完整性，应用层需要自行处理。

##### 4\. 流量控制和拥塞控制

  * **TCP** ：TCP实现了流量控制（利用滑动窗口机制）和拥塞控制（例如慢启动、拥塞避免、快速重传和快速恢复），能够根据网络状况动态调整数据传输速率，避免网络拥塞。
  * **UDP** ：UDP没有流量控制和拥塞控制机制，发送数据的速率不受网络状况的影响，可能导致网络拥塞。

##### 5\. 应用场景

  * **TCP** ：由于其可靠性和有序性，TCP适用于需要高可靠性的数据传输场景，如网页浏览、文件传输、电子邮件等。
  * **UDP** ：UDP适用于对实时性要求高、对丢包不敏感的应用，如视频流、在线游戏、实时音频等。

