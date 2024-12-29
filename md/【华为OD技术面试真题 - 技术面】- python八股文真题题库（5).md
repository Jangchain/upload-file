## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * python的GIL锁
  *     *       * 什么是Python的GIL锁？
      * 为什么需要GIL？
      *         * 1\. CPython的内存管理
        * 2\. 简化实现和提高安全性
      * GIL的影响
      *         * 1\. 多线程性能瓶颈
        * 2\. I/O密集型 vs. CPU密集型
      * 解决GIL的常见方法
      *         * 1\. 多进程
        * 2\. 使用C扩展或其他语言
  * 多进程间如何通信
  *     *       * 1\. 管道（Pipe）
      * 2\. 队列（Queue）
      * 3\. 共享内存（Shared Memory）
      * 4\. 管理器（Manager）
  * 面向对象的特点
  *     *       *         * 1\. 封装（Encapsulation）
        * 2\. 继承（Inheritance）
        * 3\. 多态（Polymorphism）
        * 4\. 抽象（Abstraction）
  * python的内存管理方式
  *     *       *         * 1\. 引用计数（Reference Counting）
        * 2\. 垃圾回收（Garbage Collection, GC）
        * 3\. 内存池管理（Memory Pool Management）
        * 4\. 全局解释器锁（Global Interpreter Lock, GIL）
  * *arg 和**karg的区别是什么
  *     *       *         * 1\. `*args`
        * 2\. `**kwargs`
      * 组合使用`*args`和`**kwargs`
  * 内存监控工具
  *     *       *         * 1\. `memory_profiler`
        * 2\. `tracemalloc`
        * 3\. `objgraph`

## python的GIL锁

#### 什么是Python的GIL锁？

**Global Interpreter Lock (GIL)**
是Python解释器级别的一个全局锁，用于确保同一时刻只有一个线程执行Python字节码。GIL的存在使得Python线程不能充分利用多核CPU的优势，从而在某些并发场景下影响性能。

#### 为什么需要GIL？

##### 1\. CPython的内存管理

  * **CPython实现** ：GIL主要存在于CPython解释器中。CPython使用引用计数来管理内存，引用计数在多线程环境中会变得复杂，因为多个线程可能同时修改对象的引用计数。GIL通过确保同一时刻只有一个线程执行Python代码，避免了对引用计数的竞态条件，从而简化了内存管理。

##### 2\. 简化实现和提高安全性

  * **线程安全性** ：GIL简化了CPython解释器的实现，使得在单线程环境下，Python的内存管理和其他底层操作可以是线程安全的。虽然这在多线程环境中限制了并发性能，但在单线程应用中，提供了更高的安全性和稳定性。

#### GIL的影响

##### 1\. 多线程性能瓶颈

  * **多线程限制** ：由于GIL的存在，Python多线程程序在多核CPU上无法真正实现并行执行。这意味着在I/O密集型任务中，Python的多线程仍能提供性能优势，但在CPU密集型任务中，多线程的性能提升有限。

##### 2\. I/O密集型 vs. CPU密集型

  * **I/O密集型任务** ：如网络请求、文件I/O等，线程会频繁地等待I/O操作完成。在这些情况下，Python可以通过线程切换在等待期间执行其他线程的任务，从而提高并发性能。
  * **CPU密集型任务** ：如计算密集的数学运算，多线程并不能显著提高性能，因为GIL会阻止多个线程同时执行Python字节码。

#### 解决GIL的常见方法

##### 1\. 多进程

  * **多进程** ：使用`multiprocessing`模块创建多个进程，每个进程有自己的Python解释器实例和GIL，因此可以实现真正的并行执行。多进程适合CPU密集型任务，但需要注意进程间通信的开销。

    
    
    import multiprocessing
    
    def cpu_bound_task():
        # Some CPU-intensive task
        pass
    
    if __name__ == "__main__":
        processes = []
        for _ in range(multiprocessing.cpu_count()):
            p = multiprocessing.Process(target=cpu_bound_task)
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()
    

##### 2\. 使用C扩展或其他语言

  * **C扩展** ：编写C扩展模块，进行CPU密集型计算时释放GIL，从而实现并行计算。许多科学计算库如NumPy等已经实现了这一点。
  * **其他语言** ：对于性能关键的部分，可以考虑使用不受GIL限制的语言（如C、C++）重写这些部分，然后通过接口与Python交互。

## 多进程间如何通信

在Python中，多进程间的通信（Inter-Process Communication, IPC）可以通过多种方式实现，主要包括以下几种：

#### 1\. 管道（Pipe）

管道允许两个进程之间进行双向通信。`multiprocessing.Pipe()`函数返回一对连接对象，可以用于发送和接收数据。

    
    
    import multiprocessing
    
    def sender(conn):
        conn.send("Hello from sender")
        conn.close()
    
    def receiver(conn):
        msg = conn.recv()
        print(f"Received message: {msg}")
    
    if __name__ == "__main__":
        parent_conn, child_conn = multiprocessing.Pipe()
        p1 = multiprocessing.Process(target=sender, args=(child_conn,))
        p2 = multiprocessing.Process(target=receiver, args=(parent_conn,))
        
        p1.start()
        p2.start()
        
        p1.join()
        p2.join()
    

#### 2\. 队列（Queue）

`multiprocessing.Queue`提供了多进程安全的队列，可以实现多个生产者和多个消费者模型。它类似于线程中的`queue.Queue`，但是适用于多进程环境。

    
    
    import multiprocessing
    
    def producer(queue):
        queue.put("Hello from producer")
    
    def consumer(queue):
        msg = queue.get()
        print(f"Received message: {msg}")
    
    if __name__ == "__main__":
        queue = multiprocessing.Queue()
        p1 = multiprocessing.Process(target=producer, args=(queue,))
        p2 = multiprocessing.Process(target=consumer, args=(queue,))
        
        p1.start()
        p2.start()
        
        p1.join()
        p2.join()
    

#### 3\. 共享内存（Shared Memory）

`multiprocessing.Value`和`multiprocessing.Array`可以用于在多个进程间共享数据。`Value`适用于单个数据，`Array`适用于数组。

    
    
    import multiprocessing
    
    def increment_value(shared_value):
        with shared_value.get_lock():
            shared_value.value += 1
    
    if __name__ == "__main__":
        shared_value = multiprocessing.Value('i', 0)  # 'i'表示整数类型
        processes = [multiprocessing.Process(target=increment_value, args=(shared_value,)) for _ in range(10)]
        
        for p in processes:
            p.start()
        
        for p in processes:
            p.join()
        
        print(f"Final value: {shared_value.value}")
    

#### 4\. 管理器（Manager）

`multiprocessing.Manager`提供了一个服务器进程，可以使多个进程共享复杂的Python对象（如字典、列表、Namespace等）。

    
    
    import multiprocessing
    
    def update_dict(shared_dict, key, value):
        shared_dict[key] = value
    
    if __name__ == "__main__":
        manager = multiprocessing.Manager()
        shared_dict = manager.dict()
        processes = [multiprocessing.Process(target=update_dict, args=(shared_dict, f"key{i}", i)) for i in range(5)]
        
        for p in processes:
            p.start()
        
        for p in processes:
            p.join()
        
        print(f"Final dictionary: {shared_dict}")
    

## 面向对象的特点

##### 1\. 封装（Encapsulation）

**定义** ：封装是指将数据和操作数据的方法绑定在一起，隐藏对象的内部实现细节，只对外提供必要的接口。这种方式提高了代码的安全性和可维护性。

**实现** ：在Python中，通过定义类和使用访问修饰符（如`_`和`__`）来实现封装。

    
    
    class Person:
        def __init__(self, name, age):
            self.__name = name  # 私有变量
            self.__age = age    # 私有变量
        
        def get_name(self):
            return self.__name
        
        def get_age(self):
            return self.__age
    
        def set_age(self, age):
            if 0 <= age <= 120:
                self.__age = age
            else:
                raise ValueError("Invalid age")
    
    p = Person("Alice", 30)
    print(p.get_name())  # 输出: Alice
    print(p.get_age())   # 输出: 30
    

##### 2\. 继承（Inheritance）

**定义** ：继承是指一个类（子类）可以从另一个类（父类）继承属性和方法，子类可以扩展或重写父类的功能。继承促进了代码的重用和扩展。

**实现** ：在Python中，通过类定义时的括号指定父类来实现继承。

    
    
    class Animal:
        def __init__(self, name):
            self.name = name
    
        def speak(self):
            raise NotImplementedError("Subclass must implement abstract method")
    
    class Dog(Animal):
        def speak(self):
            return f"{self.name} says Woof!"
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says Meow!"
    
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    print(dog.speak())  # 输出: Buddy says Woof!
    print(cat.speak())  # 输出: Whiskers says Meow!
    

##### 3\. 多态（Polymorphism）

**定义** ：多态是指相同接口可以有不同的实现。多态允许不同类型的对象以相同的方式进行操作，从而提高代码的灵活性和可扩展性。

**实现** ：在Python中，通过方法重写和接口实现多态性。

    
    
    class Animal:
        def speak(self):
            raise NotImplementedError("Subclass must implement abstract method")
    
    class Dog(Animal):
        def speak(self):
            return "Woof!"
    
    class Cat(Animal):
        def speak(self):
            return "Meow!"
    
    def make_animal_speak(animal):
        print(animal.speak())
    
    dog = Dog()
    cat = Cat()
    make_animal_speak(dog)  # 输出: Woof!
    make_animal_speak(cat)  # 输出: Meow!
    

##### 4\. 抽象（Abstraction）

**定义** ：抽象是指将具体事物的共性提取出来，形成具有抽象特征的类，隐藏具体实现细节，只保留相关信息。抽象帮助简化复杂度，提供清晰的编程接口。

**实现** ：在Python中，可以通过定义抽象基类（Abstract Base Class, ABC）和抽象方法来实现抽象。

    
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
    
    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
    
        def area(self):
            return self.width * self.height
    
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
    
        def area(self):
            return 3.14 * (self.radius ** 2)
    
    rect = Rectangle(3, 4)
    circle = Circle(5)
    print(rect.area())  # 输出: 12
    print(circle.area())  # 输出: 78.5
    

## python的内存管理方式

Python的内存管理是由其内置的内存管理器自动处理的，主要包括以下几个方面：

##### 1\. 引用计数（Reference Counting）

**定义**
：引用计数是Python内存管理的核心机制。每个对象都有一个引用计数器，用于记录该对象被引用的次数。当一个对象的引用计数变为0时，说明该对象不再被使用，其占用的内存可以被回收。

**实现** ：每当创建对象、赋值或将对象传递给函数时，引用计数增加；当对象引用被删除或覆盖时，引用计数减少。

    
    
    import sys
    
    a = [1, 2, 3]
    b = a
    print(sys.getrefcount(a))  # 输出: 3 (a, b, 以及getrefcount的临时引用)
    
    b = None
    print(sys.getrefcount(a))  # 输出: 2 (a 以及getrefcount的临时引用)
    

##### 2\. 垃圾回收（Garbage Collection, GC）

**定义**
：为了处理引用计数机制无法解决的循环引用问题，Python还采用了垃圾回收机制。Python的垃圾回收器使用了分代收集（generational
collection）算法，分为0代、1代和2代，0代最年轻，2代最老。

**实现** ：垃圾回收器会周期性地检测并清理不再使用的对象。每一代对象都有不同的回收频率，年轻对象更频繁地回收。

    
    
    import gc
    
    class MyClass:
        def __init__(self):
            self.ref = None
    
    a = MyClass()
    b = MyClass()
    a.ref = b
    b.ref = a
    
    del a
    del b
    
    gc.collect()  # 显式调用垃圾回收器
    

##### 3\. 内存池管理（Memory Pool Management）

**定义**
：Python为了提高内存分配和释放的效率，使用内存池机制管理小对象。Python的内存池由多个块组成，不同大小的对象存储在不同的块中。常用的内存池管理器是`pymalloc`。

**实现**
：内存池机制减少了系统调用的次数，提高了内存分配的效率。对于小对象，Python使用内存池进行管理；对于大对象，Python直接使用操作系统的内存分配。

##### 4\. 全局解释器锁（Global Interpreter Lock, GIL）

**定义** ：GIL是Python解释器为了在多线程环境中安全管理对象和内存而引入的一种机制。GIL确保同一时间只有一个线程执行Python字节码。

**实现** ：GIL的存在使得多线程无法真正并行执行Python代码，这在一定程度上影响了多线程的性能。

## *arg 和**karg的区别是什么

##### 1\. `*args`

**定义** ：`*args`用于将多个非键值对的参数以元组的形式传递给函数。这允许函数接受可变数量的位置参数。

**用法** ：在定义函数时，`*args`可以放在参数列表中。调用函数时，传递的多个参数会被收集到一个元组中。

    
    
    def example_function(*args):
        for arg in args:
            print(arg)
    
    example_function(1, 2, 3)  # 输出: 1 2 3
    example_function('a', 'b', 'c')  # 输出: a b c
    

##### 2\. `**kwargs`

**定义** ：`**kwargs`用于将多个键值对参数以字典的形式传递给函数。这允许函数接受可变数量的关键字参数。

**用法** ：在定义函数时，`**kwargs`可以放在参数列表中。调用函数时，传递的多个键值对参数会被收集到一个字典中。

    
    
    def example_function(**kwargs):
        for key, value in kwargs.items():
            print(f"{key} = {value}")
    
    example_function(a=1, b=2, c=3)  # 输出: a = 1, b = 2, c = 3
    example_function(x='hello', y='world')  # 输出: x = hello, y = world
    

#### 组合使用`*args`和`**kwargs`

在函数定义中，可以同时使用`*args`和`**kwargs`，以便接受任意数量的位置参数和关键字参数。通常，`*args`参数放在`**kwargs`之前。

    
    
    def example_function(*args, **kwargs):
        for arg in args:
            print(f"arg: {arg}")
        for key, value in kwargs.items():
            print(f"{key} = {value}")
    
    example_function(1, 2, 3, a=4, b=5) 
    # 输出:
    # arg: 1
    # arg: 2
    # arg: 3
    # a = 4
    # b = 5
    

## 内存监控工具

##### 1\. `memory_profiler`

**定义**
：`memory_profiler`是一个常用的Python库，用于监控内存使用情况。它可以按行报告函数的内存使用情况，帮助识别内存密集型代码段。

**安装** ：

    
    
    pip install memory_profiler
    

**用法** ：  
通过在代码中添加装饰器`@profile`来监控特定函数的内存使用情况。

    
    
    from memory_profiler import profile
    
    @profile
    def example_function():
        a = [1] * (10**6)
        b = [2] * (2 * 10**7)
        del b
        return a
    
    if __name__ == '__main__':
        example_function()
    

**运行** ：

    
    
    python -m memory_profiler your_script.py
    

##### 2\. `tracemalloc`

**定义** ：`tracemalloc`是Python内置的内存跟踪模块，用于跟踪内存分配。它可以帮助识别内存泄漏和分析内存使用情况。

**用法** ：  
使用`tracemalloc`跟踪内存分配，并显示内存使用的统计信息。

    
    
    import tracemalloc
    
    def example_function():
        a = [1] * (10**6)
        b = [2] * (2 * 10**7)
        del b
        return a
    
    tracemalloc.start()
    
    snapshot1 = tracemalloc.take_snapshot()
    example_function()
    snapshot2 = tracemalloc.take_snapshot()
    
    stats = snapshot2.compare_to(snapshot1, 'lineno')
    for stat in stats[:10]:
        print(stat)
    

##### 3\. `objgraph`

**定义** ：`objgraph`是一个Python库，用于绘制对象引用图和分析对象的关系。它可以帮助识别对象之间的引用关系和潜在的内存泄漏。

**安装** ：

    
    
    pip install objgraph
    

**用法** ：  
使用`objgraph`分析内存中的对象引用关系，并生成图像文件。

    
    
    import objgraph
    
    def example_function():
        a = [1] * (10**6)
        b = [2] * (2 * 10**7)
        del b
        return a
    
    example_function()
    
    objgraph.show_most_common_types()
    objgraph.show_refs([a], filename='refs.png')
    

