## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 1\. python 常用的数据结构都有什么
  * 2\. 需要大量的查询, 而且删除与插入很少, 那么应该用链表还是数组?
  * 3\. 数组与元组有什么区别
  *     *       * 列表操作示例
      * 元组操作示例
  * 4\. 二叉树都有什么遍历方式
  * 5\. 排序算法
  *     *       * 1\. 冒泡排序（Bubble Sort）
      * 2\. 选择排序（Selection Sort）
      * 3\. 插入排序（Insertion Sort）
      * 4\. 快速排序（Quick Sort）
      * 5\. 归并排序（Merge Sort）
      * 6\. 堆排序（Heap Sort）
  * 6\. python中的进程和协程
  *     *       * 进程（Process）
      *         * 特点：
      * 协程（Coroutine）
      *         * 特点：
        * 使用示例
  * 7\. return和yield的区别
  *     *       * `return`
      *         * 示例代码：
      * `yield`
      *         * 示例代码：
      * 主要区别
  * 8\. python的可变/不可变对象介绍下
  *     *       * 不可变对象（Immutable Objects）
      *         * 示例：
      * 可变对象（Mutable Objects）
      *         * 示例：
      * 重要性和影响

## 1\. python 常用的数据结构都有什么

  1. **列表（List）** ：

     * 功能：列表是可变的序列，能够存储不同类型的元素。
     * 特点：支持增加、删除、访问元素等操作，支持索引和切片操作。
     * 使用场景：适用于需要顺序访问的情况，或当你需要经常修改数据时。
  2. **元组（Tuple）** ：

     * 功能：元组是不可变的序列，一旦创建便不能修改。
     * 特点：比列表访问速度快，可以用作字典的键（以及其他原生不可变类型）。
     * 使用场景：适用于存储不应改变的数据元素，如函数的返回值。
  3. **字典（Dictionary）** ：

     * 功能：字典存储键值对，其中键必须是唯一的。
     * 特点：通过键而非索引访问元素，查找速度快。
     * 使用场景：适用于通过键快速检索、插入或删除数据项的场景。
  4. **集合（Set）** ：

     * 功能：集合是一个无序的元素集，自动去除重复元素。
     * 特点：提供高效的成员检查，可以进行数学上的集合操作，如并集、交集、差集等。
     * 使用场景：适用于需要元素唯一性的场景，或需要进行集合运算的地方。
  5. **字符串（String）** ：

     * 功能：字符串是字符的不可变序列。
     * 特点：提供丰富的方法和操作，如切片、连接、查找等。
     * 使用场景：处理文本数据的任何场景。
  6. **双端队列（Deque）** ：

     * 功能：来自collections模块，Deque是一个从两端都可以快速增加和弹出的队列。
     * 特点：当你需要一个从头部和尾部都可以快速添加或删除的列表时，比列表更有效。
     * 使用场景：适用于需要队列操作的场景，如在任务队列的头部或尾部添加或移除任务。
  7. **堆（Heap）** ：

     * 功能：通过`heapq`模块实现，堆是一个特殊的完全二叉树。
     * 特点：在堆中，最小元素总是位于顶部。`heapq`提供了操作堆的方法，如`heappush`和`heappop`。
     * 使用场景：适用于需要频繁访问最小元素但不需要全部排序的数据结构。

## 2\. 需要大量的查询, 而且删除与插入很少, 那么应该用链表还是数组?

在面对这样的场景，即需要大量的查询操作，而且删除与插入操作很少时，通常使用数组（在Python中表现为列表）而不是链表。

  1. **查询效率** ：

     * **数组** ：数组提供通过索引的直接访问，其访问时间复杂度为 O(1)。这意味着无论要访问数组中的哪个元素，所需时间都是常数级别的。
     * **链表** ：链表的查询效率较低，因为链表不支持随机访问。要访问链表中的一个元素，可能需要从头节点开始逐一访问后续节点，最坏情况下的时间复杂度为 O(n)，n 是链表长度。
  2. **插入与删除操作** ：

     * 虽然链表在插入和删除操作时通常优于数组（因为链表的插入和删除操作时间复杂度为 O(1)，而数组为 O(n)），但应用场景中这些操作较少，这一优势并不明显。
  3. **内存利用率** ：

     * **数组** ：数组在内存中占用连续空间，这有助于数据的快速访问，但可能需要在扩展大小时重新分配整个数组空间。
     * **链表** ：链表的内存分布是分散的，每个节点除了存储数据外，还需要额外的空间存储指向下一个节点的指针（或者在双向链表中，还有指向前一个节点的指针）。这会增加额外的内存开销。

## 3\. 数组与元组有什么区别

在Python中，数组（通常指列表）和元组是两种基本的数据结构，它们都可以用来存储一系列的元素。它们的主要区别在于可变性、用途和性能方面：

  1. **可变性（Mutability）** ：

     * **列表（List）** ：列表是可变的，意味着你可以在创建后添加、删除或更改其元素。
     * **元组（Tuple）** ：元组是不可变的，一旦创建，你不能修改其内容。这包括不能添加、删除或更改存储在元组中的元素。
  2. **性能** ：

     * 由于元组的不可变性，它们在某些情况下比列表具有更好的性能。例如，元组的创建速度通常比列表快，它们还可以作为字典中的键使用，而列表则不能，因为字典的键必须是不可变类型。
  3. **用途** ：

     * **列表** ：更适用于数据集合，其中包含的元素可能会经常变动，如数据库记录的列表或进行多次编辑的数据集。
     * **元组** ：通常用于存储不同数据类型的记录，如从函数返回多个值或将多个值传递给函数。元组的不可变性使得它们可以用于确保数据在传递过程中不被修改。
  4. **语法** ：

     * **列表** ：列表用方括号表示，例如：`[1, 2, 3]`。
     * **元组** ：元组用圆括号表示，例如：`(1, 2, 3)`。不过，当元组中只有一个元素时，需要在元素后添加逗号，如`(1,)`，否则它不会被识别为元组。
  5. **存储方式** ：

     * 元组由于其不可变性，可以在内部优化存储方式，这在处理大量数据时可以更节省内存。

#### 列表操作示例

    
    
    # 创建一个列表
    my_list = [1, 2, 3]
    
    # 添加元素到列表末尾
    my_list.append(4)
    print("After appending:", my_list)
    
    # 修改列表中的元素
    my_list[1] = 20
    print("After modifying:", my_list)
    
    # 删除列表中的元素
    del my_list[2]
    print("After deleting:", my_list)
    

输出：

    
    
    After appending: [1, 2, 3, 4]
    After modifying: [1, 20, 3, 4]
    After deleting: [1, 20, 4]
    

#### 元组操作示例

    
    
    # 创建一个元组
    my_tuple = (1, 2, 3)
    
    # 尝试修改元组中的元素（这将引发错误）
    try:
        my_tuple[1] = 20
    except TypeError as e:
        print(e)
    
    # 元组可以包含不同类型的数据
    another_tuple = (1, "hello", 3.14)
    print("Mixed types:", another_tuple)
    
    # 元组的拆包
    a, b, c = another_tuple
    print("Unpacked:", a, b, c)
    
    # 从函数返回多个值（使用元组）
    def min_max(numbers):
        return min(numbers), max(numbers)
    
    result = min_max([1, 2, 3, 4, 5])
    print("Min and max:", result)
    

输出：

    
    
    'tuple' object does not support item assignment
    Mixed types: (1, 'hello', 3.14)
    Unpacked: 1 hello 3.14
    Min and max: (1, 5)
    

## 4\. 二叉树都有什么遍历方式

常见的遍历方式主要有四种：

  1. **前序遍历（Pre-order Traversal）** ：

     * 在前序遍历中，访问顺序为：根节点 -> 左子树 -> 右子树。
     * 这意味着首先访问根节点，然后递归地执行前序遍历左子树，接着递归地执行前序遍历右子树。
  2. **中序遍历（In-order Traversal）** ：

     * 在中序遍历中，访问顺序为：左子树 -> 根节点 -> 右子树。
     * 这种方式首先递归地访问左子树，然后访问根节点，最后递归地访问右子树。
     * 对于二叉搜索树（BST），中序遍历会按照键的升序访问树中的所有键。
  3. **后序遍历（Post-order Traversal）** ：

     * 在后序遍历中，访问顺序为：左子树 -> 右子树 -> 根节点。
     * 这种方式首先递归地访问左子树，然后递归地访问右子树，最后访问根节点。
  4. **层序遍历（Level-order Traversal）或广度优先遍历（Breadth-first Traversal）** ：

     * 层序遍历从根节点开始，按层次从上到下、从左到右遍历整棵树。

     * 这通常通过使用队列来实现，将当前节点的子节点按顺序放入队列中，然后逐个取出进行访问。

每种遍历方法都有其特定的应用场景。例如，前序遍历常用于打印结构化的树，中序遍历适用于二叉搜索树的排序操作，后序遍历常用于先处理子节点后处理父节点的场景，如树的删除或释放操作，层序遍历则特别适用于需要按层次处理或查找最短路径的场景。

以下是使用Python实现这些遍历的简单示例：

    
    
    class TreeNode:
        def __init__(self, value=0, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right
    
    def preorder_traversal(root):
        if root:
            print(root.value, end=' ')
            preorder_traversal(root.left)
            preorder_traversal(root.right)
    
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value, end=' ')
            inorder_traversal(root.right)
    
    def postorder_traversal(root):
        if root:
            postorder_traversal(root.left)
            postorder_traversal(root.right)
            print(root.value, end=' ')
    
    def level_order_traversal(root):
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Preorder traversal: ")
    preorder_traversal(root)
    print("\nInorder traversal: ")
    inorder_traversal(root)
    print("\nPostorder traversal: ")
    postorder_traversal(root)
    print("\nLevel order traversal: ")
    level_order_traversal(root)
    

## 5\. 排序算法

#### 1\. 冒泡排序（Bubble Sort）

  * **描述** ：重复地遍历要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。遍历数列的工作是重复进行的，直到没有再需要交换，也就是说该数列已经排序完成。
  * **时间复杂度** ： 
    * 最佳情况： O ( n ) O(n) O(n)（已经排序的数列）
    * 平均情况： O ( n 2 ) O(n^2) O(n2)
    * 最坏情况： O ( n 2 ) O(n^2) O(n2)

#### 2\. 选择排序（Selection Sort）

  * **描述** ：不断地选择剩余元素中的最小者，将它与数组的前端交换，然后，再从剩下的元素中继续这种选择和交换的过程。
  * **时间复杂度** ： 
    * 最佳情况： O ( n 2 ) O(n^2) O(n2)
    * 平均情况： O ( n 2 ) O(n^2) O(n2)
    * 最坏情况： O ( n 2 ) O(n^2) O(n2)

#### 3\. 插入排序（Insertion Sort）

  * **描述** ：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
  * **时间复杂度** ： 
    * 最佳情况： O ( n ) O(n) O(n)（已经排序的数列）
    * 平均情况： O ( n 2 ) O(n^2) O(n2)
    * 最坏情况： O ( n 2 ) O(n^2) O(n2)

#### 4\. 快速排序（Quick Sort）

  * **描述** ：选取一个元素作为“基准”（pivot），数列分割成独立的两部分，将小于基准值的元素排在基准前面，大于基准值的排在基准的后面，然后递归地对这两部分继续进行快速排序。
  * **时间复杂度** ： 
    * 最佳情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 平均情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 最坏情况： O ( n 2 ) O(n^2) O(n2)（数列已经是正序或逆序）

#### 5\. 归并排序（Merge Sort）

  * **描述** ：将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
  * **时间复杂度** ： 
    * 最佳情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 平均情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 最坏情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)

#### 6\. 堆排序（Heap Sort）

  * **描述** ：利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是小于（或者大于）它的父节点。
  * **时间复杂度** ： 
    * 最佳情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 平均情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)
    * 最坏情况： O ( n log ⁡ n ) O(n \log n) O(nlogn)

## 6\. python中的进程和协程

#### 进程（Process）

在Python中，进程可以通过`multiprocessing`模块创建和管理。每个进程在操作系统层面拥有自己的内存空间和资源。这意味着进程间的数据是隔离的，它们不能直接共享全局变量或数据结构，除非通过进程间通信（如队列、管道）来交换信息。

##### 特点：

  * **独立性** ：每个进程拥有独立的执行环境和内存空间。
  * **资源消耗较大** ：创建和销毁进程相比于线程和协程来说更加资源密集。
  * **适用场景** ：适合执行计算密集型任务，可以利用多核CPU的优势。

#### 协程（Coroutine）

Python的协程是通过`asyncio`库实现的，它提供了一个事件循环的机制，允许代码在需要等待外部操作（如IO操作）时挂起，转而执行其他任务。协程是一种在用户态下实现的轻量级线程，由程序员在代码级别控制其调度。

##### 特点：

  * **轻量级** ：协程相比于线程和进程需要更少的资源开销，切换速度快。
  * **非阻塞** ：可以在单个线程内实现并发执行。
  * **适用场景** ：适合IO密集型任务，例如在Web服务器中处理大量的客户端请求。

##### 使用示例

**进程的使用示例** ：

    
    
    from multiprocessing import Process
    
    def f(name):
        print('hello', name)
    
    if __name__ == '__main__':
        p = Process(target=f, args=('Bob',))
        p.start()
        p.join()
    

**协程的使用示例** ：

    
    
    import asyncio
    
    async def greet(name):
        await asyncio.sleep(1)  # 模拟IO操作
        print('Hello', name)
    
    async def main():
        await asyncio.gather(
            greet('Alice'),
            greet('Bob')
        )
    
    asyncio.run(main())
    

## 7\. return和yield的区别

在Python中，`return`和`yield`都用于函数中返回值 。

#### `return`

  * **功能** ：`return`语句用于从函数返回一个值并结束函数的执行。一旦函数执行到`return`语句，函数的局部变量和执行状态都将被丢弃。
  * **用途** ：适用于普通函数从中断点返回结果，并且不打算再从同一点继续执行。

##### 示例代码：

    
    
    def compute_sum(x, y):
        return x + y
    
    result = compute_sum(5, 3)
    print(result)  # 输出 8
    

#### `yield`

  * **功能** ：`yield`语句用于从函数返回一个值，并暂停函数的执行，保留函数的状态，以便后续从它离开的地方继续执行。
  * **用途** ：`yield`通常用在生成器函数中，这种函数可以生成一个值序列，供循环或迭代器消费，每次产生一个值之后暂停，等待下一次迭代请求值。

##### 示例代码：

    
    
    def count_down(n):
        while n > 0:
            yield n
            n -= 1
    
    for i in count_down(5):
        print(i)  # 依次打印 5, 4, 3, 2, 1
    

#### 主要区别

  1. **继续执行 vs 结束执行** ：

     * `yield`在提供值后暂停执行，并保留函数的状态，包括局部变量和指针信息，这使得函数可以在下次调用时从停止的地方继续执行。
     * `return`提供值并结束函数执行，函数状态不会被保存。
  2. **单值返回 vs 多值生成** ：

     * `return`一次只能返回一个值，并且一旦返回，函数就终止了。
     * `yield`可以多次返回，每次返回一个值，支持通过循环或迭代器多次调用，使得它可以生成一个值的序列。
  3. **应用场景** ：

     * 使用`return`适合处理那些一次计算并返回单个结果的普通功能。
     * 使用`yield`适合处理流式数据、懒加载数据或构建复杂的自定义迭代器。

## 8\. python的可变/不可变对象介绍下

#### 不可变对象（Immutable Objects）

不可变对象一旦创建，它们的内容就不能被修改。尝试修改不可变对象会导致创建一个新对象。不可变类型包括：

  * 整数（int）
  * 浮点数（float）
  * 复数（complex）
  * 布尔值（bool）
  * 字符串（str）
  * 元组（tuple）
  * 冻结集合（frozenset）

##### 示例：

    
    
    a = "hello"
    print(id(a))  # 输出a的内存地址
    a += " world"
    print(id(a))  # 输出新字符串的内存地址，与原地址不同
    
    t = (1, 2, 3)
    print(id(t))  # 输出元组的内存地址
    t += (4,)     # 尝试修改元组
    print(id(t))  # 输出新元组的内存地址，与原地址不同
    

在这个例子中，字符串和元组都是不可变的。尝试修改这些对象将导致创建一个新的对象，并且原来的对象保持不变。

#### 可变对象（Mutable Objects）

可变对象可以在不更改对象地址的情况下修改其内容。这意味着你可以修改对象中的数据，而对象的内存地址保持不变。可变类型包括：

  * 列表（list）
  * 字典（dict）
  * 集合（set）

##### 示例：

    
    
    lst = [1, 2, 3]
    print(id(lst))  # 输出列表的内存地址
    lst.append(4)   # 修改列表
    print(id(lst))  # 内存地址未变，依然是原来的地址
    
    d = {'a': 1, 'b': 2}
    print(id(d))    # 输出字典的内存地址
    d['c'] = 3      # 修改字典
    print(id(d))    # 内存地址未变，依然是原来的地址
    

在这个例子中，列表和字典是可变的。可以在不更改对象地址的情况下添加、删除或修改其中的元素。

#### 重要性和影响

  1. **函数参数传递** ：了解对象的可变性对于处理函数参数特别重要。不可变对象作为参数传递时，函数中的任何修改都不会影响原始数据。然而，可变对象作为参数传递时，函数内部的修改将影响到原始对象。
  2. **性能优化** ：在某些情况下，了解何时使用可变与不可变对象可以帮助优化程序的内存使用和执行速度。
  3. **并发编程** ：在多线程环境中，不可变对象因其不可更改的特性，自然是线程安全的。

