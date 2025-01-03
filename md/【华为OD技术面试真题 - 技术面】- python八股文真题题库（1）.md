## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 1\. 数据预处理流程
  *     *       * 数据预处理的主要步骤
      * 工具和库
  * 2.介绍线性回归、逻辑回归模型
  *     *       * 线性回归（Linear Regression）
      *         * 模型形式：
        * 关键点：
      * 逻辑回归（Logistic Regression）
      *         * 模型形式：
        * 关键点：
      * 参数估计与评估：
  * 3\. python浅拷贝及深拷贝
  *     *       * 浅拷贝（Shallow Copy）
      *         * 创建浅拷贝的方法：
        * 示例：
      * 深拷贝（Deep Copy）
      *         * 创建深拷贝的方法：
        * 示例：
      * 关键区别：
  * 4\. python lambda匿名函数
  *     *       * `lambda` 函数的基本语法：
      * 特点：
      * 常见用例：
  * 5\. python装饰器
  *     *       * 装饰器基本概念：
      * 基本语法：
      * 装饰器的高级用法：
  * 6\. python执行过程
  *     *       * Python执行过程概述
      * 重要的内部机制
  * 7\. is和==的区别
  *     *       * `==` （等于）
      * `is` （同一性）
      * 示例解释
      * 引申
  * 8\. python多线程 ，GIL
  *     *       * 1\. Python多线程概述
      * 2\. 全局解释器锁（GIL）
      * 3\. 绕过GIL的方法
      * 引申

## 1\. 数据预处理流程

#### 数据预处理的主要步骤

  1. **数据清洗** ：

     * **处理缺失值** ：识别数据中的缺失值，并决定如何处理它们（例如，填充缺失值、删除含缺失值的行或列等）。
     * **去除重复记录** ：检查并删除数据中的重复行，以防止数据偏差和重复计算。
  2. **数据转换** ：

     * **类型转换** ：确保每列数据的类型（如整数、浮点数、字符串等）正确地匹配其内容，以方便后续处理。
     * **标准化/归一化** ：对数值数据进行标准化或归一化处理，使其位于同一量级，便于模型处理（如Z-score标准化、Min-Max归一化等）。
  3. **数据编码** ：

     * **类别数据编码** ：将非数值类型数据转换为数值型，例如使用独热编码（One-Hot Encoding）、标签编码（Label Encoding）等方法处理分类数据。
  4. **特征工程** ：

     * **特征选择** ：选择对模型预测最有帮助的特征，以减少维度并提高模型的效率和效果。
     * **特征构造** ：基于现有数据构造新的特征，以增强模型的预测能力。
  5. **异常值处理** ：

     * **检测和处理异常值** ：识别可能的异常值并决定如何处理它们，可以使用统计测试、箱型图等方法。
  6. **数据划分** ：

     * **训练集和测试集分割** ：将数据划分为训练集和测试集，以确保模型能在未见过的数据上进行有效的测试。

#### 工具和库

在Python中，有许多库可以帮助进行数据预处理，如：

  * **Pandas** ：提供了强大的数据结构和数据分析工具，非常适合数据清洗和探索。
  * **NumPy** ：用于处理大型多维数组和矩阵的科学计算。
  * **Scikit-learn** ：包含了许多用于数据预处理的工具，如标凈化、编码、特征选择等。
  * **Matplotlib** 和 **Seaborn** ：用于数据可视化，帮助理解数据分布和特征关系。

## 2.介绍线性回归、逻辑回归模型

#### 线性回归（Linear Regression）

线性回归是一种用于预测连续数值目标变量（因变量）的回归分析方法，其中的预测是基于一个或多个独立变量（自变量）。它假设因变量和自变量之间存在线性关系。

##### 模型形式：

线性回归模型可以表示为：  
y = β 0 \+ β 1 x 1 \+ β 2 x 2 \+ . . . \+ β n x n \+ ϵ y = \beta_0 +
\beta_1x_1 + \beta_2x_2 + ... + \beta_nx_n + \epsilon
y=β0​+β1​x1​+β2​x2​+...+βn​xn​+ϵ  
其中， y y y 是因变量， x 1 , x 2 , . . . , x n x_1, x_2, ..., x_n x1​,x2​,...,xn​
是自变量， β 0 , β 1 , . . . , β n \beta_0, \beta_1, ..., \beta_n β0​,β1​,...,βn​
是模型参数， ϵ \epsilon ϵ 是误差项。

##### 关键点：

  * **参数估计** ：通常使用最小二乘法来估计参数（即找到参数的值，使得实际观察值与模型预测值之间的差的平方和最小）。
  * **用途** ：广泛用于预测分析和因果关系研究，如房价预测、销售量分析等。

#### 逻辑回归（Logistic Regression）

逻辑回归是用于二分类问题的统计模型，它预测的是一个概率值，表示给定自变量下因变量属于某一类别的概率。

##### 模型形式：

逻辑回归模型通过逻辑函数（Sigmoid函数）将线性回归的输出转换为概率，形式如下：  
P ( y = 1 ∣ X ) = 1 1 \+ e − ( β 0 \+ β 1 x 1 \+ β 2 x 2 \+ . . . \+ β n x n )
P(y = 1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2 + ... +
\beta_nx_n)}} P(y=1∣X)=1+e−(β0​+β1​x1​+β2​x2​+...+βn​xn​)1​  
其中， P ( y = 1 ∣ X ) P(y = 1|X) P(y=1∣X) 是在给定自变量X的条件下y=1的概率， β 0 , β 1 , . . .
, β n \beta_0, \beta_1, ..., \beta_n β0​,β1​,...,βn​ 是模型参数。

##### 关键点：

  * **输出** ：输出介于0和1之间的概率值。
  * **用途** ：广泛用于分类任务，如疾病诊断、信用风险评估等。
  * **阈值决定** ：通过设定一个阈值（常用0.5），将连续的概率值转换为二元分类结果。

#### 参数估计与评估：

  * **逻辑回归** 使用最大似然估计法（MLE）来估计模型参数，目的是最大化观察到的样本出现的概率。
  * **模型评估** 可以通过多种指标，如均方误差（MSE）, 精确度（Accuracy）, AUC-ROC曲线等来进行。

## 3\. python浅拷贝及深拷贝

#### 浅拷贝（Shallow Copy）

浅拷贝创建一个新对象，但它包含的是对原始对象中包含项的引用（即地址），而不是其副本。因此，如果原始对象中的项是可变的，修改这些项将会影响到拷贝后的新对象。

##### 创建浅拷贝的方法：

  1. 使用列表的 `list.copy()` 方法。
  2. 切片操作，例如 `new_list = old_list[:]`。
  3. 使用 `copy` 模块中的 `copy()` 函数：`from copy import copy; new_list = copy(old_list)`。

##### 示例：

    
    
    import copy
    original = [1, 2, [3, 4]]
    shallow = copy.copy(original)
    
    # 修改原始列表中的嵌套列表也会影响浅拷贝
    original[2][0] = "changed"
    print(shallow)  # 输出：[1, 2, ['changed', 4]]
    

#### 深拷贝（Deep Copy）

深拷贝创建一个新对象，并且递归地拷贝原始对象中的所有项。这意味着它将创建所有项的副本，包括嵌套的对象。修改原始对象不会影响到深拷贝创建的副本。

##### 创建深拷贝的方法：

使用 `copy` 模块中的 `deepcopy()` 函数。

    
    
    from copy import deepcopy
    deep = deepcopy(original)
    

##### 示例：

    
    
    original = [1, 2, [3, 4]]
    deep = deepcopy(original)
    
    # 修改原始列表中的嵌套列表不会影响深拷贝
    original[2][0] = "no change"
    print(deep)  # 输出：[1, 2, [3, 4]]
    

#### 关键区别：

  * **浅拷贝** 对于非嵌套对象（如包含原始数据类型的列表）表现得像深拷贝，但对于包含可变对象（如列表或字典等）的对象，则只复制顶层结构。
  * **深拷贝** 完全独立于原始对象，适用于包含复杂、嵌套数据结构的对象。

## 4\. python lambda匿名函数

在Python中，`lambda` 函数是一种轻量级的匿名函数，它通常用于编写简单的、一行的函数，无需正式定义函数名。

#### `lambda` 函数的基本语法：

`lambda` 函数的基本语法非常简单：

    
    
    lambda arguments: expression
    

  * **arguments** ：参数，可以是多个，用逗号分隔。
  * **expression** ：一个表达式，描述了函数的行为，返回值是这个表达式的结果。

#### 特点：

  1. **匿名** ：`lambda` 函数通常是匿名的，即没有具体的函数名称。
  2. **一行表达式** ：只能有一个表达式，不能包含其他的语句或多个表达式。
  3. **可随时使用** ：可以用在任何需要函数的地方。
  4. **灵活性** ：常用于简化代码，特别是在函数编程或需要传递小函数作为参数的场合。

#### 常见用例：

**作为参数传递** ：`lambda` 经常被用作高阶函数（如 `map()`, `filter()`, `sorted()` 等）的参数。

  * 使用 `map()` 将每个元素加倍：
    
        list(map(lambda x: x * 2, [1, 2, 3, 4]))  # 结果: [2, 4, 6, 8]
    

  * 使用 `filter()` 过滤出大于 2 的元素：
    
        list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # 结果: [3, 4]
    

  * 使用 `sorted()` 根据列表中元组的第二个元素排序：
    
        sorted([(1, 'one'), (2, 'two'), (3, 'three')], key=lambda x: x[1])
    

## 5\. python装饰器

在Python中，装饰器是一种非常有用的设计模式，主要用于在不修改原始函数或方法定义的情况下，给函数或方法添加新的功能。这种功能的添加通常关联于跨越系统的关注点，如日志记录、性能测试、事务处理、缓存等。

#### 装饰器基本概念：

装饰器本质上是一个函数，它接受一个函数作为参数并返回一个新的函数。装饰器的核心功能是允许你在调用原始函数之前或之后执行额外的代码，而不需要改变原始函数的代码。

#### 基本语法：

装饰器的定义通常使用 `@` 符号，放在需要装饰的函数定义之前：

    
    
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper
    
    @my_decorator
    def say_hello():
        print("Hello!")
    

当 `say_hello()` 被调用时，实际上是在调用 `wrapper()` 函数，它增加了在原始函数调用前后打印信息的功能。

#### 装饰器的高级用法：

  1. **带参数的装饰器** ：有时候，装饰器需要接受额外的参数。这需要进一步的嵌套函数定义：
    
        def decorator_with_args(arg1, arg2):
        def my_decorator(func):
            def wrapper():
                print(f"Arguments received: {arg1}, {arg2}")
                func()
            return wrapper
        return my_decorator
    
    @decorator_with_args("arg1", "arg2")
    def say_hello():
        print("Hello!")
    

  2. **装饰有参数的函数** ：如果被装饰的函数有参数，装饰器内部的 `wrapper` 函数需要能够接受这些参数，并且在调用原始函数时传递给它：
    
        def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before calling the function")
            result = func(*args, **kwargs)
            print("After calling the function")
            return result
        return wrapper
    
    @my_decorator
    def add(a, b):
        return a + b
    

## 6\. python执行过程

#### Python执行过程概述

Python是一种解释型语言，这意味着Python代码在执行时首先被转换成字节码，然后由Python虚拟机（PVM）解释执行。详细的执行过程可以分为以下几个步骤：

  1. **源代码** ：编写的Python文件（`.py`文件）包含了可读的源代码。

  2. **编译** ：Python解释器首先将源代码编译成字节码。这一过程涉及到语法分析和语义分析，确保代码符合Python的语法规则。字节码是一种低级、与平台无关的代码，保存在`.pyc`文件中。

  3. **字节码** ：编译得到的字节码是一种中间表示形式，存储在内存中。字节码的执行比直接解释源代码要快。

  4. **Python虚拟机** ：Python虚拟机（PVM）是Python运行时环境的一部分，负责读取字节码，将其转换成机器码，然后执行。PVM是解释器的核心，它执行存储在`.pyc`文件中的字节码。

  5. **执行** ：PVM逐条执行字节码指令，进行函数调用、内存管理等操作。

#### 重要的内部机制

  * **全局解释器锁（GIL）** ：在CPython（Python的默认实现）中，GIL是一个互斥锁，确保同一时刻只有一个线程执行Python字节码。这意味着即使在多核处理器上，单个Python进程也不能同时执行多个线程。GIL是Python中多线程编程的一个重要限制。

  * **垃圾回收** ：Python使用引用计数和垃圾回收机制来管理内存。引用计数是主要的内存管理形式，当对象的引用计数降到0时，对象就会被立即删除。此外，Python还使用了一种名为“标记-清除”的垃圾回收算法来处理循环引用的情况。

## 7\. is和==的区别

#### `==` （等于）

  * `==` 操作符用来比较两个对象的值是否相等。在使用`==`时，实际上是调用了对象的`__eq__()`方法，这意味着`==`的行为可以根据对象的实现而改变。
  * 例如，在比较两个数字或两个字符串时，`==`会检查它们的值是否相等。

#### `is` （同一性）

  * `is` 操作符用于比较两个对象的身份是否相同，即它们是否是内存中的同一个对象。这基于对象的内存地址进行判断。
  * 使用`is`比较时，结果完全取决于两个对象的标识符（内存地址）是否相同。

#### 示例解释

    
    
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    
    print(a == b)  # 输出 True，因为a和b具有相同的内容。
    print(a is b)  # 输出 False，因为a和b不是同一个对象，它们在内存中有不同的地址。
    print(a is c)  # 输出 True，因为c和a指向同一个对象。
    

#### 引申

  * **问** ：“在什么情况下应该使用`is`而不是`==`？”

  * **答** ：“`is`应该用在你需要判断两个变量是否指向同一个对象的情况下，例如在判断一个变量是否为`None`时。使用`if var is None:`通常比`if var == None:`更快且语义更清晰。”

  * **问** ：“请说明为什么有时候小整数或小字符串使用`is`比较也会返回`True`？”

  * **答** ：“Python对小的整数和短字符串进行了优化，它们会被缓存并重用，这是一种内存优化机制。因此，多个变量即使独立声明，如果它们的值是小整数或短字符串，它们也可能指向同一个内存地址。”

## 8\. python多线程 ，GIL

多线程处理和全局解释器锁（Global Interpreter Lock，简称GIL）

#### 1\. Python多线程概述

Python的标准库提供了`threading`模块，允许程序创建多个线程来同时执行代码。多线程通常用于提高程序的执行效率，特别是在涉及I/O操作（如网络请求、文件读写等）时，可以显著提高程序响应性和速度。

#### 2\. 全局解释器锁（GIL）

  * **定义与目的** ：GIL是Python中的一个机制，它确保任何时候只有一个线程可以执行Python字节码。其主要目的是简化CPython（Python的一个主要实现）中内存管理的复杂性，并避免由多个线程同时访问Python对象引起的竞争条件。
  * **影响** ：由于GIL的存在，即使在多核处理器上，使用Python的`threading`模块创建的多线程程序也无法实现真正的并行执行，这意味着多线程主要适用于I/O密集型任务而不是CPU密集型任务。

#### 3\. 绕过GIL的方法

  * **多进程** ：使用`multiprocessing`模块可以创建多个进程，每个进程有自己的Python解释器和内存空间，因此不受GIL的限制。这使得多进程可以被用于提高CPU密集型应用的性能。
  * **其他解释器** ：选择不同的Python解释器，如Jython或IronPython，这些解释器没有GIL，可以实现真正的线程并行。
  * **C扩展** ：编写C语言扩展或使用已有的如NumPy这样优化过的库，这些库通常能够在底层进行并行操作，绕过GIL。

#### 引申

  * **问** ：“在什么场景下使用多线程，而在什么场景下使用多进程更为合适？”

  * **答** ：“在I/O密集型任务中，如网络请求或文件操作，多线程可以提高效率，因为线程可以在等待I/O完成时让出CPU。而在CPU密集型任务中，如大规模数值计算，多进程能更好地利用多核处理器的优势，因为每个进程都能在不同的CPU核心上并行运行，不受GIL的限制。”

  * **问** ：“GIL是如何影响多线程程序性能的？”

  * **答** ：“GIL确保了同一时刻只有一个线程可以执行Python字节码。这意味着在多线程环境中，尽管存在多个线程，但这些线程不能同时执行，从而限制了程序在多核处理器上的并行执行能力。特别是在CPU密集型任务中，这会成为性能瓶颈。”

