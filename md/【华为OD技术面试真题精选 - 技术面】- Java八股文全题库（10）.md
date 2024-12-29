![doutub_gif](https://i-blog.csdnimg.cn/blog_migrate/e9413fcd109f2f3d7297192eab0c0b2a.gif)

## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试真题精选 🌟

大家好！今天我给大家推荐一份备受赞誉的华为OD技术面试精选题目。
所有题目均为华为od实际面试过程中出现的问题。这些面试题主要涉及到编程八股文、职业态度以及独特的个性特点。让我们一起深入了解这个精心整理的面试题集吧！😊
希望这些问题能够帮助你在面试中脱颖而出，展现出你的技术实力和独特魅力。加油！💪💼

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 1\. 工作中是否出现过oom，怎么导出dump文件（jmat命令），使用什么进行分析处理（jprofile、mat）

在工作中确实遇到过OutOfMemoryError（OOM）问题。当遇到OOM问题时，我首先会尝试导出堆转储文件（heap
dump），这可以通过多种方式完成，比如使用JVM参数或者在运行时使用工具。

  1. **导出堆转储文件** :

     * 通过在Java应用启动命令中添加JVM参数来自动导出堆转储文件，例如使用`-XX:+HeapDumpOnOutOfMemoryError`参数，它会在OOM发生时自动生成堆转储文件。
     * 使用`jmap`命令手动导出堆转储文件。`jmap`是JDK自带的工具，可以用来生成堆转储文件。命令格式为`jmap -dump:live,format=b,file=<filename> <pid>`，其中`<filename>`是你想要保存的文件名，`<pid>`是Java进程的ID。
  2. **分析堆转储文件** :

     * 对于堆转储文件的分析，我通常会使用Eclipse Memory Analyzer (MAT) 或 JProfiler。这两个工具都非常强大，可以帮助识别内存泄漏和分析内存消耗。
     * **MAT** : Eclipse Memory Analyzer 是一个快速、功能丰富的Java堆分析工具，它可以帮助我们找到内存泄漏并减少内存消耗。使用MAT，我可以轻松地查看哪些对象占用了最多的内存，以及通过“泄漏疑点报告”来识别潜在的内存泄漏。
     * **JProfiler** : JProfiler 是一个全功能的Java性能分析工具，不仅可以分析内存使用情况，还可以分析CPU使用情况、线程、锁等。使用JProfiler，我可以对应用程序的性能进行深入分析，找出性能瓶颈。

相关链接：

    
    
    1. https://juejin.cn/post/7269660552677294120
    2. https://heapdump.cn/article/3059968
    

## 2\. redis的缓存击穿、穿透、雪崩

Redis缓存问题主要包括缓存击穿、缓存穿透和缓存雪崩，下面是这三个问题的解释及相应的解决方案：

  1. **缓存穿透** :

     * **问题描述** : 缓存穿透是指查询一个数据库中不存在的数据，由于缓存不命中，并且由于数据不存在，每次请求都要去数据库查询，导致数据库压力过大。
     * **解决方案** : 解决缓存穿透的方法包括将查询的结果（即使是空结果）缓存起来，并设置一个较短的过期时间。另一种方法是使用布隆过滤器，先检查数据是否可能存在，如果布隆过滤器说不存在，就直接返回，不再查询数据库。
  2. **缓存击穿** :

     * **问题描述** : 缓存击穿是指一个热点key突然失效（过期），导致大量请求直接打到数据库上，造成数据库压力过大。
     * **解决方案** : 解决缓存击穿的方法包括设置热点数据永不过期，或者使用互斥锁（Mutex Lock）。当缓存失效的时候，不是所有请求都去数据库加载数据，而是先加锁，由一个请求去数据库查询并重新加载到缓存中，其他请求等待缓存重建后再访问缓存。
  3. **缓存雪崩** :

     * **问题描述** : 缓存雪崩是指在某一个时间段内，大量的缓存集中过期失效，导致所有的请求都去访问数据库，从而引起数据库压力过大甚至崩溃。
     * **解决方案** : 解决缓存雪崩的方法包括缓存数据的过期时间设置随机，避免大量缓存同时过期；使用高可用的缓存架构，比如使用集群，保证缓存服务的稳定性；以及提前使用缓存预热技术，在缓存过期前重新加载缓存数据。

相关链接

    
    
    https://www.51cto.com/article/703396.html
    

## 3\. nio

Java NIO（New Input/Output）是从Java 1.4版本开始引入的一套新的IO API，用来替代标准的Java IO
API。NIO支持面向缓冲区的（Buffer-oriented）、基于通道的（Channel-
based）IO操作。NIO提供了更高的性能特别是在需要高速读写、大量并发IO操作时。NIO主要包括以下几个核心组件：

  1. **缓冲区（Buffers）** :

     * 缓冲区是NIO中数据读写的容器。Java NIO中的Buffer用于与NIO Channel交互，你可以从Channel中读取数据到Buffer中，也可以将数据从Buffer写入到Channel中。
  2. **通道（Channels）** :

     * 通道是连接IO服务的通道，可以理解为到数据源或目标的开放连接，如文件或网络套接字。Channel类似于传统IO中的流，但主要区别在于Channel是双向的，既可以用来进行读操作也可以用来进行写操作。
  3. **选择器（Selectors）** :

     * 选择器用于监听多个通道的事件（比如：连接打开、数据到达）。通过单个线程处理多个Channel，可以管理多个网络连接，而无需为每个连接都创建一个线程，从而提高了效率。

**NIO的主要优势** :

  * **非阻塞模式** ：NIO允许非阻塞模式，即在进行IO操作时，线程可以进行其他任务，当IO操作完成时，线程可以继续处理IO操作，提高了应用程序的响应性能。
  * **缓冲区管理** ：NIO的缓冲管理更灵活，可以更高效地处理数据。
  * **选择器** ：通过使用选择器，单个线程可以管理多个网络连接，这对于构建高性能的网络服务器非常有用。

**使用场景** :  
Java NIO非常适合于需要高速读写、大量并发IO操作的场景，例如网络服务器和大文件处理。在这些场景下，NIO能够提供比传统IO更好的性能。

相关链接

    
    
    https://xie.infoq.cn/article/fb524c4992beea6bb4487af87
    

## 4\. java中线程通信方式

在Java中，线程通信主要依赖于以下几种基本方式来协调线程之间的工作，确保数据的正确性和同步。

  1. **等待/通知机制（wait/notify）** : 
     * 这是最基本的线程通信方式。当一个线程处理完特定数据后，它可以调用`wait()`方法进入等待状态，同时释放锁。另一个线程可以在适当的时候调用相同对象的`notify()`或`notifyAll()`方法来通知等待状态的线程继续执行。`wait()`和`notify()`方法必须在同步代码块中使用，即在对象的监视器（monitor）上调用。

    
    
    synchronized (object) {
        while (<condition does not hold>) {
            object.wait();
        }
        // Perform action appropriate to condition
        object.notifyAll(); // or object.notify();
    }
    

  2. **信号量（Semaphore）** : 
     * 信号量是一种更为高级的线程通信机制，可以控制对共享资源的访问。信号量内部维护了一组许可（permits），线程可以通过调用`acquire()`方法来获取许可，如果许可不可用，当前线程将阻塞直到许可成为可用。线程完成资源的使用后，通过调用`release()`方法来释放许可。

    
    
    Semaphore semaphore = new Semaphore(permits);
    semaphore.acquire(); // 获取许可
    // 访问共享资源
    semaphore.release(); // 释放许可
    

  3. **管道（PipedInputStream/PipedOutputStream）** : 
     * 管道提供了线程之间通过输入/输出流进行通信的机制。一个线程发送数据到输出管道，另一个线程从输入管道读取数据。这种方式适用于数据传输的场景。

    
    
    PipedOutputStream output = new PipedOutputStream();
    PipedInputStream input = new PipedInputStream(output);
    // Thread 1: 写数据到output
    // Thread 2: 从input读数据
    

  4. **并发工具类（如 CountDownLatch、CyclicBarrier, Phaser）** : 
     * `CountDownLatch`允许一个或多个线程等待其他线程完成操作。
     * `CyclicBarrier`允许一组线程相互等待，达到一个公共屏障点。
     * `Phaser`是一个更灵活的线程同步器，可以处理多阶段任务。

使用这些机制和类，可以实现线程间的协调和通信，解决并发编程中的同步问题。

相关链接

    
    
    https://juejin.cn/post/6844903919781412877
    

## 5\. 责任链模式

责任链模式（Chain of Responsibility
Pattern）是一种行为设计模式，它允许将请求的发送者和接收者解耦，让多个对象都有机会处理这个请求。在这个模式中，请求从链中的一个对象传递到下一个对象，直到有对象处理这个请求为止。

责任链模式通常涉及以下几个角色：

  1. **处理器（Handler）** ：定义了处理请求的接口，通常在这个接口中定义了一个方法来接收或者处理请求。它也可以定义一个链中的下一个处理器对象的引用。

  2. **具体处理器（Concrete Handler）** ：处理器接口的实现类。如果可以处理请求，就处理之；否则将请求转发给链中的下一个处理器。

  3. **客户端（Client）** ：负责创建处理链，并向链的第一个处理器对象提交请求。

责任链模式的主要优点是减少请求的发送者和接收者之间的耦合，增强了系统的灵活性。通过改变链中的成员或者调整它们的顺序，允许动态地新增或者删除责任。

下面是一个简单的责任链模式的实现示例：

    
    
    // 处理器（Handler）抽象类
    abstract class Handler {
        protected Handler successor;
    
        public void setSuccessor(Handler successor) {
            this.successor = successor;
        }
    
        public abstract void handleRequest(int request);
    }
    
    // 具体处理器（Concrete Handler）类
    class ConcreteHandler1 extends Handler {
        public void handleRequest(int request) {
            if (request >= 0 && request < 10) {
                System.out.println(this.getClass().getSimpleName() + " 处理请求 " + request);
            } else if (successor != null) {
                successor.handleRequest(request);
            }
        }
    }
    
    class ConcreteHandler2 extends Handler {
        public void handleRequest(int request) {
            if (request >= 10 && request < 20) {
                System.out.println(this.getClass().getSimpleName() + " 处理请求 " + request);
            } else if (successor != null) {
                successor.handleRequest(request);
            }
        }
    }
    
    // 客户端（Client）类
    public class Client {
        public static void main(String[] args) {
            // 组装责任链
            Handler handler1 = new ConcreteHandler1();
            Handler handler2 = new ConcreteHandler2();
            
            handler1.setSuccessor(handler2);
    
            // 提交请求
            handler1.handleRequest(5);
            handler1.handleRequest(15);
        }
    }
    

在这个例子中，`Client`类创建了一个责任链，链中包含了两个具体处理器（`ConcreteHandler1`和`ConcreteHandler2`）。请求首先被`ConcreteHandler1`接收，如果`ConcreteHandler1`能够处理这个请求，它就处理之；否则，它就将请求转发给链中的下一个处理器。

    
    
    https://dunwu.github.io/design/pages/b25735/
    

## 6\. redis热key和大key

在处理Redis性能问题时，"热Key"和"大Key"是两个常见的概念，它们对Redis的性能有显著影响。

#### 热Key

**定义** :
热Key是指那些在短时间内被频繁访问的Key。由于访问频率高，这些Key可能会成为性能瓶颈，尤其是在分布式环境中，如果多个客户端同时访问同一个热Key，可能会导致网络拥塞或者Redis服务器的处理瓶颈。

**解决方法** :

  1. **缓存分层** : 将热Key缓存在更接近客户端的地方，比如本地缓存或者边缘缓存，减少对中心Redis的访问压力。
  2. **读写分离** : 使用Redis主从复制功能，将读操作分发到多个从服务器，减轻主服务器的压力。
  3. **数据分片** : 将数据分布到多个Redis实例，减少单个实例的访问压力。但需注意，这种方法需要合理设计Key的分片策略，以避免新的热点问题。
  4. **限流和降级** : 对访问进行限流，超过阈值的请求进行降级处理，比如返回默认值或者旧的数据。

#### 大Key

**定义** :
大Key是指那些存储了大量数据的Key，如一个包含数万个元素的List、Set、Hash或ZSet。大Key的操作（比如删除、遍历）可能会阻塞Redis服务器，影响性能。

**解决方法** :

  1. **定期扫描分析** : 使用Redis的`SCAN`命令配合`HSCAN`、`SSCAN`、`ZSCAN`等命令，定期扫描并分析Key的大小，找出潜在的大Key。
  2. **分片处理** : 对大Key进行分片处理，例如将一个大的List分成多个小List，每个小List包含一定数量的元素。
  3. **渐进式删除** : 对于需要删除的大Key，不要一次性删除，可以使用`HDEL`、`SREM`、`ZREM`等命令对其进行渐进式的元素删除，或者利用`SCAN`命令分批次删除，避免一次性操作造成的长时间阻塞。
  4. **优化数据结构** : 根据实际使用场景优化数据结构，例如使用更加紧凑的数据类型或者将大对象拆解存储。

综上所述，热Key和大Key问题的解决需要综合运用多种策略，既要注意到单个Key的问题，也要考虑整个系统的访问模式和数据分布，以保证Redis的高效和稳定运行。

相关链接：

    
    
    https://blog.verysu.com/aritcle/java/1998
    

## 7\. mysql的数据类型，30用什么类型存，300，30000，3000000

在MySQL中，选择合适的数据类型来存储特定范围的数值对于优化存储空间、提高查询性能和保证数据准确性都非常重要。对于整数类型，MySQL提供了多种不同的数据类型，包括`TINYINT`、`SMALLINT`、`MEDIUMINT`、`INT`（或`INTEGER`）、和`BIGINT`。这些类型可以存储不同范围的整数值，并且每种类型都可以是有符号的或无符号的。

对于给定的数值30、300、30000、3000000，我们可以根据它们的大小选择最合适的数据类型：

  * **30** : 这是一个非常小的数值，可以使用`TINYINT`类型存储。`TINYINT`的范围是-128到127（有符号）或0到255（无符号）。因此，对于30这样的小数值，使用有符号或无符号的`TINYINT`都是合适的。

  * **300** : 这个数值超出了`TINYINT`的范围，但可以使用`SMALLINT`类型存储。`SMALLINT`的范围是-32768到32767（有符号）或0到65535（无符号）。因此，300可以使用有符号或无符号的`SMALLINT`存储。

  * **30000** : 这个数值可以使用`SMALLINT`类型存储（如果是无符号的），因为无符号的`SMALLINT`范围是0到65535。如果是有符号的情况，也可以考虑使用`MEDIUMINT`，其范围是-8388608到8388607（有符号）或0到16777215（无符号）。

  * **3000000** : 这个数值超出了`SMALLINT`的范围，但可以使用`MEDIUMINT`或`INT`类型存储。考虑到范围和存储效率，`MEDIUMINT`是一个较好的选择，因为它足以存储这个数值，同时比`INT`使用更少的存储空间。

总结如下：

  * **30** : `TINYINT`
  * **300** : `SMALLINT`
  * **30000** : `SMALLINT UNSIGNED` 或 `MEDIUMINT`
  * **3000000** : `MEDIUMINT`

选择合适的数据类型不仅可以节省存储空间，还可以提高查询效率和数据处理性能。在实际应用中，还需要考虑到数值的预期增长范围，以便选择能够满足长期需求的数据类型。

