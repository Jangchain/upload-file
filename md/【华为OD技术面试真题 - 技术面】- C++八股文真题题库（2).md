## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * STL有哪些容器
  *     *       * 1\. 序列容器
      * 2\. 关联容器
      * 3\. 无序关联容器（C++11新增）
      * 4\. 容器适配器
  * Vector和list的区别是什么
  *     *       * 1\. 数据结构
      * 2\. 性能特点
      * 3\. 内存使用
      * 4\. 应用场景
  * 在一个循环中将vector中的奇数位元素全部删除
  *     *       * 方法：反向迭代删除
      * 注意事项：
  * makefile和CMake
  *     *       * makefile
      * CMake
      * 对比
  * 进程线程
  *     *       * 进程（Process）
      * 线程（Thread）
      * 进程与线程的区别
      * C++中的并发编程
      * 进程
      * 线程
  * 指针和引用
  *     *       * 指针
      * 引用
  * 类的构造与析构
  *     *       * 构造函数
      * 析构函数
  * C++内存分配机制
  *     *       * 栈内存分配（Stack Allocation）
      * 堆内存分配（Heap Allocation）
      * 静态存储区域（Static Storage）
  * sizeof和len的区别
  *     *       * sizeof
      * len 或 size() 方法
  * 平时会用gdb吗，讲一讲基本用法
  *     *       * `gdb` 基本用法

## STL有哪些容器

#### 1\. 序列容器

这些容器在内部按顺序存储元素。

  * **`vector`** ：提供动态数组功能，可以随机访问元素。优点是访问速度快，尾部添加/删除元素效率高；缺点是中间插入或删除元素效率低。
  * **`deque`** ：双端队列，支持在头部和尾部高效地插入和删除元素。相比`vector`，`deque`在头部插入和删除效率更高。
  * **`list`** ：双向链表，支持在任何位置高效地插入和删除元素。优点是插入和删除效率高；缺点是不支持随机访问，访问元素效率较低。
  * **`forward_list`** （C++11新增）：单向链表，比`list`更节省空间，但只能向前遍历。

#### 2\. 关联容器

这些容器内部使用树结构（通常是红黑树），元素根据键进行排序。

  * **`set`** ：集合，存储唯一键的集合，自动排序。
  * **`map`** ：映射，存储键值对，根据键排序，键是唯一的。
  * **`multiset`** ：多重集合，可以存储重复的键。
  * **`multimap`** ：多重映射，可以存储重复键的键值对。

#### 3\. 无序关联容器（C++11新增）

基于哈希表实现，元素不排序，提供平均常数时间的复杂度进行查找、插入和删除操作。

  * **`unordered_set`** ：无序集合，存储唯一键的集合。
  * **`unordered_map`** ：无序映射，存储键值对，键是唯一的。
  * **`unordered_multiset`** ：无序多重集合，可以存储重复的键。
  * **`unordered_multimap`** ：无序多重映射，可以存储重复键的键值对。

#### 4\. 容器适配器

容器适配器提供了一种方式，以修改现有容器类的接口。

  * **`stack`** ：栈适配器，默认使用`deque`实现。后进先出（LIFO）数据结构。
  * **`queue`** ：队列适配器，默认使用`deque`实现。先进先出（FIFO）数据结构。
  * **`priority_queue`** ：优先队列适配器，默认使用`vector`实现，但元素按优先级排序。

## Vector和list的区别是什么

#### 1\. 数据结构

  * **`vector`** ：基于动态数组的实现。它在内存中连续存储所有元素，这意味着可以通过指针算术直接计算元素位置，从而实现快速的随机访问。
  * **`list`** ：基于双向链表的实现。每个元素都作为一个节点独立存储，每个节点通过指针连接前一个和后一个节点。这种结构使得在任何位置插入和删除操作都非常高效，但不支持直接的随机访问。

#### 2\. 性能特点

  * **访问元素** ：

    * `vector`：提供非常高效的随机访问能力，访问任意位置的元素的时间复杂度为O(1)。
    * `list`：只能通过顺序访问来找到特定元素，访问任意位置的元素的时间复杂度为O(n)。
  * **插入和删除操作** ：

    * `vector`： 
      * 在尾部插入和删除操作非常高效（通常为O(1)），但可能涉及到动态数组的重新分配和元素的复制或移动。
      * 在中间或开始插入和删除效率较低，因为可能需要移动多个元素。
    * `list`： 
      * 在任何位置插入和删除元素都非常高效，时间复杂度为O(1)，因为这仅仅涉及修改指针而不需要移动其他元素。

#### 3\. 内存使用

  * **`vector`** ：由于内部使用数组，所以内存使用相对紧凑，但在扩容时可能会有额外的内存开销。
  * **`list`** ：每个元素需要额外的内存来存储指向前后节点的指针，因此内存使用比`vector`更高。

#### 4\. 应用场景

  * **`vector`** ：适合那些需要快速随机访问元素的场景，或者添加和删除操作主要发生在序列的末尾。
  * **`list`** ：适合那些需要频繁插入和删除操作的场景，尤其是在序列的中间或开始位置进行这些操作。

## 在一个循环中将vector中的奇数位元素全部删除

#### 方法：反向迭代删除

由于在循环中删除`vector`元素可能会导致迭代器失效和元素移动，最安全的做法是从后向前迭代`vector`并进行删除。这样做的好处是，删除元素后，只会影响到当前元素之后的元素的位置和迭代器，而不会影响到已经处理过的元素。这里是如何实现的：

    
    
    #include <iostream>
    #include <vector>
    
    int main() {
        std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
        // 从后向前迭代，删除奇数位元素（注意索引从0开始）
        for (int i = vec.size() - 1; i >= 0; --i) {
            if (i % 2 == 0) {  // 选取奇数位元素（索引为偶数）
                vec.erase(vec.begin() + i);
            }
        }
    
        // 输出结果验证
        for (int num : vec) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    
        return 0;
    }
    

#### 注意事项：

  1. **迭代器失效** ：在`vector`中删除元素会使从当前位置到末尾的所有迭代器、指针和引用失效。因此从后向前删除可以避免处理已失效的迭代器。

  2. **性能考虑** ：每次调用`erase`都可能导致从当前元素到末尾的所有元素复制或移动，这在元素数量较多时可能导致较高的性能成本。

## makefile和CMake

#### makefile

  * **定义** ：`makefile`是一个文本文件，其中定义了一组规则来指定如何编译和链接程序。它被`make`工具使用，来自动化编译过程。
  * **特点** ： 
    * 通过编写一系列的规则来描述源文件如何被编译和链接。
    * 每个规则指明一个目标文件、依赖和用于生成目标的命令。
    * 适用于小到中型的项目，特别是当项目结构相对简单时。

#### CMake

  * **定义** ：`CMake`是一个跨平台的自动化构建系统，它使用`CMakeLists.txt`文件来定义构建过程。
  * **特点** ： 
    * 不直接构建项目，而是生成标准的构建文件（如Unix的Makefiles或Windows的项目文件），然后依靠相应的构建系统进行项目构建。
    * 可以根据不同平台生成对应的构建系统文件，提高项目的可移植性。
    * 适用于大型项目，特别是需要跨平台编译的项目。

#### 对比

  1. **平台兼容性** ：

     * `makefile`：通常与Unix-like系统紧密相关，虽然可以在Windows上通过工具如Cygwin使用，但不如CMake那样天然跨平台。
     * `CMake`：天然支持跨平台，可以生成多种平台上的构建系统文件，如Makefiles、Ninja、Visual Studio项目文件等。
  2. **易用性和灵活性** ：

     * `makefile`：需要详细指定编译命令和链接命令，对新手可能较为复杂。
     * `CMake`：通过简单的配置语法自动处理许多复杂的构建任务，更易于管理大型项目。
  3. **可维护性** ：

     * `makefile`：随着项目规模的扩大，makefile可能变得难以管理和维护。
     * `CMake`：通过组织多个`CMakeLists.txt`文件，可以更好地管理大型项目的构建过程。

## 进程线程

#### 进程（Process）

  * **定义** ：进程是计算机中的一个程序的实例。它是系统进行资源分配和调度的基本单位，拥有独立的地址空间和系统资源。
  * **特点** ： 
    * 每个进程都有自己独立的内存地址空间。
    * 进程间通信需要使用特定的IPC（Inter-process communication）机制，如管道、消息队列、共享内存等。
    * 进程之间的切换开销较大，因为涉及到完整的上下文切换。

#### 线程（Thread）

  * **定义** ：线程是进程的执行单元，是CPU调度和执行的实际单元，一个进程可以包含一个或多个线程。
  * **特点** ： 
    * 线程在同一个进程下共享进程资源，如内存和文件描述符等。
    * 线程的创建、终止和切换的开销小于进程，因为线程间的上下文切换不需要地址空间的切换。
    * 多线程可以利用多核处理器的并行处理能力，提高应用程序的执行效率。

#### 进程与线程的区别

  * **资源独立性** ：进程有完全独立的地址空间，线程共享所属进程的地址空间。
  * **通信方式** ：进程间通信（IPC）比较复杂，线程间通信可以直接通过读写共享数据来进行。
  * **开销** ：进程的创建、销毁和切换开销更大，线程相对较小。

#### C++中的并发编程

C++11及以后的版本引入了`<thread>`库，支持原生的多线程编程。通过使用`std::thread`，程序员可以在C++中创建并管理线程。此外，C++还提供了其他并发编程的工具，如互斥锁`std::mutex`、条件变量`std::condition_variable`等，来帮助同步多线程之间的活动。

作为一名C++面试官，你需要确保候选人不仅了解理论概念，还能实际应用它们。以下是对进程和线程的解释以及代码示例：

#### 进程

**代码示例** ：在C++中可以通过使用POSIX标准库（在Linux和macOS上），使用`fork()`来创建新的进程。例如：

    
    
    #include <iostream>
    #include <unistd.h>
    
    int main() {
        pid_t pid = fork(); // 创建一个新的进程
        if (pid < 0) {
            std::cerr << "Fork failed" << std::endl;
            return 1;
        } else if (pid == 0) {
            // 子进程
            std::cout << "This is the child process. PID: " << getpid() << std::endl;
        } else {
            // 父进程
            std::cout << "This is the parent process. PID: " << getpid() << std::endl;
        }
        return 0;
    }
    

在这个例子中，`fork()`函数会复制当前进程，生成一个新的子进程。父进程会获得子进程的PID，而子进程的PID为0。

#### 线程

**代码示例** ：C++11引入了标准线程库，可以使用`std::thread`来创建线程。例如：

    
    
    #include <iostream>
    #include <thread>
    
    // 线程函数
    void print_message(const std::string &message, int count) {
        for (int i = 0; i < count; ++i) {
            std::cout << message << std::endl;
        }
    }
    
    int main() {
        // 创建并启动线程
        std::thread t1(print_message, "Hello from thread 1", 3);
        std::thread t2(print_message, "Hello from thread 2", 3);
    
        // 等待线程完成
        t1.join();
        t2.join();
    
        return 0;
    }
    

在这个例子中，`std::thread`被用来创建并启动线程。`t1.join()`和`t2.join()`用于确保主线程等待子线程完成。

## 指针和引用

#### 指针

**定义** ：指针是一个变量，其存储的是另一个变量的地址。通过指针，可以间接访问和修改它所指向的内存位置的数据。

**特点** ：

  * 指针可以被初始化为`nullptr`，表示它不指向任何内存位置。
  * 指针的值可以改变，可以指向不同的变量或动态分配的内存。
  * 通过解引用操作符`*`可以访问或修改指针所指向的数据。

**代码示例** ：

    
    
    #include <iostream>
    
    int main() {
        int x = 10;
        int* p = &x; // 'p' 是指向 'x' 的指针
    
        std::cout << "Value of x: " << x << std::endl;       // 输出: Value of x: 10
        std::cout << "Address of x: " << &x << std::endl;    // 输出: Address of x: [x 的内存地址]
        std::cout << "Value of p (address): " << p << std::endl; // 输出: Value of p (address): [x 的内存地址]
        std::cout << "Value pointed by p: " << *p << std::endl;  // 输出: Value pointed by p: 10
    
        *p = 20; // 通过指针修改 'x' 的值
        std::cout << "New value of x: " << x << std::endl;   // 输出: New value of x: 20
    
        return 0;
    }
    

#### 引用

**定义** ：引用是另一个变量的别名，它是一个已存在变量的另一个名字。

**特点** ：

  * 引用一旦被初始化与一个变量，就不能改变为引用另一个变量。
  * 引用必须在声明时初始化。
  * 引用允许通过自身直接访问和修改它所引用的变量，就如同操作原始变量一样。

**代码示例** ：

    
    
    #include <iostream>
    
    int main() {
        int x = 10;
        int& ref = x; // 'ref' 是 'x' 的引用
    
        std::cout << "Value of x: " << x << std::endl;      // 输出: Value of x: 10
        std::cout << "Value of ref: " << ref << std::endl;  // 输出: Value of ref: 10
    
        ref = 20; // 修改引用同时也修改原始变量 'x'
        std::cout << "New value of x: " << x << std::endl;  // 输出: New value of x: 20
        std::cout << "New value of ref: " << ref << std::endl; // 输出: New value of ref: 20
    
        return 0;
    }
    

## 类的构造与析构

#### 构造函数

**定义** ：构造函数是一种特殊的成员函数，它在创建类的对象时自动调用，用于初始化对象的成员变量。

**特点** ：

  * 构造函数的名称与类名相同，并且不返回任何类型。
  * 可以有多个构造函数，实现重载。
  * 支持默认构造函数（无参数）、参数化构造函数以及复制构造函数。

**代码示例** ：

    
    
    #include <iostream>
    #include <string>
    
    class Person {
    public:
        std::string name;
        int age;
    
        // 默认构造函数
        Person() : name("Unknown"), age(0) {
            std::cout << "Default constructor called" << std::endl;
        }
    
        // 参数化构造函数
        Person(std::string n, int a) : name(n), age(a) {
            std::cout << "Parameterized constructor called" << std::endl;
        }
    
        // 复制构造函数
        Person(const Person &p) : name(p.name), age(p.age) {
            std::cout << "Copy constructor called" << std::endl;
        }
    };
    
    int main() {
        Person person1;
        Person person2("John Doe", 30);
        Person person3 = person2; // 调用复制构造函数
    
        return 0;
    }
    

#### 析构函数

**定义** ：析构函数是一种特殊的成员函数，它在对象生命周期结束时被自动调用，用于执行清理操作，如释放资源、内存等。

**特点** ：

  * 析构函数的名称是在类名前加上波浪符号 `~`。
  * 每个类只能有一个析构函数，且不带参数。
  * 析构函数通常用于释放构造函数或成员函数中分配的资源。

**代码示例** ：

    
    
    #include <iostream>
    
    class Resource {
    public:
        Resource() {
            std::cout << "Resource acquired" << std::endl;
        }
        ~Resource() {
            std::cout << "Resource released" << std::endl;
        }
    };
    
    class Demo {
    public:
        Resource res;
    
        Demo() {
            std::cout << "Demo created" << std::endl;
        }
        ~Demo() {
            std::cout << "Demo destroyed" << std::endl;
        }
    };
    
    int main() {
        Demo demo; // 输出: Resource acquired -> Demo created -> Demo destroyed -> Resource released
        return 0;
    }
    

## C++内存分配机制

#### 栈内存分配（Stack Allocation）

栈是操作系统提供给程序的一块连续的内存区域，主要用于存储函数调用的局部变量。使用栈内存的特点是分配和释放速度非常快，但空间有限。

**特点** ：

  * 自动管理，局部变量在声明时自动分配内存，当函数调用结束时自动释放。
  * 存取速度快，适用于存储临时变量。
  * 内存大小和生命周期由作用域决定，超出作用域后，内存会被自动释放。

**示例** ：

    
    
    void function() {
        int localVariable = 5; // 在栈上分配
    } // 函数结束时，localVariable 被自动销毁
    

#### 堆内存分配（Heap Allocation）

堆内存用于存储动态分配的内存，这部分内存的管理由程序员控制，需要使用`new`和`delete`操作符来分配和释放内存。

**特点** ：

  * 灵活性高，可以动态地分配所需大小的内存。
  * 生命周期由程序员控制，不受作用域限制。
  * 使用不当容易导致内存泄露、内存碎片等问题。

**示例** ：

    
    
    int* ptr = new int; // 在堆上分配内存
    *ptr = 5; // 使用内存
    delete ptr; // 释放内存
    ptr = nullptr; // 避免悬空指针
    

#### 静态存储区域（Static Storage）

静态存储区域用于存储全局变量、静态变量和常量。这部分内存在程序启动时分配，在程序结束时释放。

**特点** ：

  * 内存分配和释放由程序自动管理。
  * 在程序整个运行期间都存在。

**示例** ：

    
    
    static int staticVariable = 10; // 静态变量，在静态存储区域分配
    int globalVariable = 20; // 全局变量，同样在静态存储区域
    

## sizeof和len的区别

在C++中，`sizeof` 和 `len`（通常不存在于标准C++库中，可能指的是某些特定容器的成员函数，如 `std::vector` 的
`size()`）是两个用于获取数据大小的不同方法，但它们的用途和功能有显著区别。

#### sizeof

`sizeof`
是一个编译时操作符，用于返回一个变量、数据类型或表达式的内存大小（以字节为单位）。这个大小在编译时就已经确定，不会因为运行时的数据变化而改变。

**特点** ：

  * 用于获取类型的存储大小，包括基本类型（如 `int`、`double`）和复合类型（如数组、结构体）。
  * 返回类型是 `std::size_t`。
  * 适用于获取数组的总大小（不适用于动态分配的数组指针），结构体的大小等。

**示例** ：

    
    
    int arr[10];
    std::cout << sizeof(arr) << std::endl;  // 输出数组总大小，例如 40（如果int是4字节）
    std::cout << sizeof(int) << std::endl;  // 输出4（如果int是4字节）
    

#### len 或 size() 方法

在C++标准库中，容器类（如 `std::vector`, `std::string` 等）通常提供了 `size()`
方法来获取容器中当前存储的元素数量。注意，这里没有 `len` 函数，如果在面试中提到 `len`，可能需要指明是从某个特定库中来的函数，如 Python
的内置 `len()` 函数。

**特点** ：

  * 动态查询容器当前包含的元素数量。
  * 返回值通常是 `std::size_t`。
  * 只适用于容器，不适用于基本数据类型或普通数组。

**示例** ：

    
    
    std::vector<int> vec = {1, 2, 3, 4, 5};
    std::cout << vec.size() << std::endl;  // 输出5，表示vec包含5个元素
    

## 平时会用gdb吗，讲一讲基本用法

#### `gdb` 基本用法

`gdb`（GNU
Debugger）是一个强大的开源调试工具，在开发和调试C++程序时非常实用。它可以帮助开发者逐步执行代码、检查变量、设置断点、查看内存和寄存器等，以找到并修复问题。

**1\. 启动与运行**

  * 通过 `gdb <可执行文件>` 命令启动调试器，并加载可执行文件。
  * 可以使用 `run` 命令启动程序。
  * `gdb` 可以传递命令行参数，如 `run arg1 arg2`。

**2\. 设置断点**

  * `break <文件名:行号>`：在指定文件的特定行设置断点。
  * `break <函数名>`：在函数入口处设置断点。
  * `info breakpoints`：列出当前所有断点。
  * `delete <编号>`：删除指定编号的断点。

**3\. 单步调试**

  * `step`：逐行执行代码并进入函数。
  * `next`：逐行执行代码但不进入函数。
  * `continue`：继续执行直到遇到下一个断点。

**4\. 检查变量**

  * `print <变量名>`：输出变量的值。
  * `info locals`：显示当前作用域内的所有局部变量及其值。
  * `watch <变量名>`：在变量值改变时触发断点。

**5\. 查看堆栈**

  * `backtrace` 或 `bt`：显示当前函数调用栈（backtrace），帮助追踪程序的执行路径。
  * `frame <编号>`：切换到特定的栈帧，便于调试特定的函数调用。

**6\. 其他高级功能**

  * `layout`：提供带有源代码的交互式TUI界面调试。
  * `set variable`：修改变量的值。
  * `x`：查看特定内存地址的内容。

