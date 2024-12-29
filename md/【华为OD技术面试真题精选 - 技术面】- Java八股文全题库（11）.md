## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试真题精选 🌟

大家好！今天我给大家推荐一份备受赞誉的华为OD技术面试精选题目。
所有题目均为华为od实际面试过程中出现的问题。这些面试题主要涉及到编程八股文、职业态度以及独特的个性特点。让我们一起深入了解这个精心整理的面试题集吧！😊
希望这些问题能够帮助你在面试中脱颖而出，展现出你的技术实力和独特魅力。加油！💪💼

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)

![doutub_gif](https://i-blog.csdnimg.cn/blog_migrate/e9413fcd109f2f3d7297192eab0c0b2a.gif)

## string怎么转list，list怎么转string

### 字符串转列表

#### 使用String.split()

    
    
    String str = "apple,banana,orange";
    List<String> list = Arrays.asList(str.split(","));
    

这是最常见和简单的方法。`split()`方法根据给定的正则表达式分隔字符串,返回一个字符串数组。然后使用`Arrays.asList()`将该数组转换为列表。

注意`Arrays.asList()`返回的是一个受内部数组支持的固定大小列表,不能进行添加或删除操作。如果需要可变大小的列表,可以构造一个新的ArrayList:

    
    
    List<String> list = new ArrayList<>(Arrays.asList(str.split(",")));
    

#### 使用StringTokenizer

    
    
    StringTokenizer st = new StringTokenizer(str, ",");  
    List<String> list = new ArrayList<>();
    while (st.hasMoreTokens()) {
        list.add(st.nextToken());
    }
    

`StringTokenizer`是一个遗留的类,在处理基于分隔符的字符串时提供了一些额外的功能,比如识别连续的分隔符。但通常建议使用`split()`方法。

#### 使用Stream

Java 8引入的Stream API提供了一种函数式编程风格:

    
    
    List<String> list = Pattern.compile(",")
                               .splitAsStream(str)
                               .collect(Collectors.toList());
    

这种方式代码更加简洁,但可读性和性能可能会受到影响。

### 列表转字符串

#### 使用String.join()

    
    
    List<String> list = Arrays.asList("apple","banana","orange");
    String str = String.join(",", list);
    

`String.join()`是Java 8引入的一个静态方法,可以很方便地将列表元素拼接为字符串。第一个参数是分隔符,第二个参数是列表。

#### 使用StringJoiner

    
    
    StringJoiner sj = new StringJoiner(",");
    for(String s : list) {
        sj.add(s);
    }
    String str = sj.toString();
    

`StringJoiner`类提供了一种简单的可重入格式化对象,可用于构造字符串连接操作的字符序列。

#### 使用StringBuilder

    
    
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<list.size(); i++) {
        sb.append(list.get(i));
        if(i<list.size()-1) {
            sb.append(",");
        }
    }
    String str = sb.toString();
    

## 抽象类和接口的区别

### 抽象类(Abstract Class)

  * 抽象类可以包含抽象方法(没有方法体)和具体方法
  * 抽象类不能被实例化,需要被继承并重写其抽象方法
  * 一个类只能继承一个抽象类
  * 抽象类可以有构造方法,用于初始化
  * 抽象类可以有静态方法和静态变量
  * 抽象类可以有访问修饰符(public,protected,default,private)

### 接口(Interface)

  * 接口完全是抽象的,只包含常量和抽象方法
  * 接口不能被实例化,需要被实现(implements)
  * 一个类可以实现多个接口
  * 接口中所有的方法默认都是公有的(public)
  * 接口中所有的字段默认都是公有的、静态的、最终的(public static final)
  * 接口不能有构造方法
  * 从Java 8开始,接口可以有默认方法和静态方法

### 主要区别

  1. **继承 vs 实现**

     * 类继承抽象类,可以重写抽象方法
     * 类实现接口,需要重写接口中的所有抽象方法
  2. **单继承 vs 多实现**

     * 一个类只能继承一个抽象类
     * 一个类可以实现多个接口
  3. **访问修饰符**

     * 抽象类中的成员可以有不同的访问修饰符
     * 接口中的所有方法和字段都是公有的
  4. **构造方法**

     * 抽象类可以有构造方法
     * 接口不能有构造方法
  5. **字段**

     * 抽象类可以有实例字段
     * 接口中只能有常量字段(public static final)
  6. **主要用途**

     * 抽象类主要用于代码复用,提供部分实现
     * 接口主要用于定义规范,实现多重继承

总的来说,抽象类更适合做代码复用,接口更适合定义规范。

## 分布式锁

分布式锁是一种在分布式系统中用于控制共享资源访问的机制。它确保在同一时间只有一个进程或线程可以访问共享资源,避免了并发访问导致的数据不一致问题。

### 分布式锁的特点

  1. **互斥性** : 在任意时刻,只有一个客户端能持有锁。
  2. **高可用** : 分布式锁服务需要高可用,不能存在单点故障。
  3. **高性能** : 获取和释放锁的操作需要快速高效。
  4. **可重入** : 同一个客户端可以多次获取同一把锁。
  5. **安全性** : 锁的持有和释放必须是同一个客户端,不能把别人的锁给释放了。
  6. **死锁避免** : 必须有超时机制或撤销机制,避免死锁。

### 分布式锁的实现方式

  1. **基于数据库实现**

     * 利用数据库的唯一约束,如MySQL的`for update`语句。
     * 优点: 简单,易于理解。
     * 缺点: 性能差,容易产生死锁,不可重入。
  2. **基于缓存实现(如Redis)**

     * 利用Redis的`setnx`(set if not exists)命令。
     * 优点: 性能好,可重入,避免死锁。
     * 缺点: 需要考虑Redis的可用性和一致性问题。
  3. **基于Zookeeper实现**

     * 利用Zookeeper的临时有序节点。
     * 优点: 高可用,可重入,避免死锁。
     * 缺点: 实现复杂,需要考虑Zookeeper的性能和可靠性。
  4. **基于Etcd实现**

     * 利用Etcd的lease机制。
     * 优点: 高可用,高性能,可重入。
     * 缺点: 实现复杂,Etcd集群的运维成本高。

### 使用场景

分布式锁适用于以下场景:

  1. 分布式系统中的并发控制,如秒杀、抢红包等。
  2. 分布式任务调度,避免重复执行。
  3. 分布式缓存,避免缓存击穿和雪崩。
  4. 分布式事务,实现两阶段提交。

### 注意事项

使用分布式锁时需要注意以下问题:

  1. 锁的粒度不要太大,避免影响性能。
  2. 获取锁和释放锁要成对出现,避免死锁。
  3. 锁的有效期要合理设置,避免长时间持有锁。
  4. 要有重试机制和异常处理,提高系统的健壮性。
  5. 不同的实现方式各有优缺点,要根据实际需求选择。

## sql注入

SQL注入是一种常见的Web安全漏洞,攻击者通过在用户输入中插入特殊字符或SQL语句片段,欺骗应用程序执行非预期的SQL查询,从而获取敏感信息或破坏数据完整性。

### SQL注入的原理

SQL注入发生的原因是应用程序没有正确过滤或转义用户输入,直接将其拼接到SQL查询语句中。例如:

    
    
    String query = "SELECT * FROM users WHERE username='" + username + "' AND passwor d='" + passwor d + "'";
    

如果攻击者输入的username为`' OR 1=1--`,那么最终执行的SQL语句就变成了:

    
    
    SELECT * FROM users WHERE username='' OR 1=1--' AND passwor d=''
    

这样就绕过了身份验证,可以在不知道密码的情况下登录任意用户。

### SQL注入的危害

SQL注入可能导致以下危害:

  1. 绕过身份验证,未授权访问。
  2. 窃取敏感数据,如用户信息、财务数据等。
  3. 篡改或删除数据,破坏数据完整性。
  4. 执行恶意操作,如向系统中插入木马、后门等。
  5. 导致拒绝服务攻击,耗尽服务器资源。

### 防范SQL注入的措施

  1. **使用预编译语句(PreparedStatement)**

     * 预编译语句会将SQL语句和参数分开处理,避免了拼接产生的漏洞。
     * 示例:
        
                String sql = "SELECT * FROM users WHERE username=? AND passwor d=?";
        PreparedStatement stmt = connection.prepareStatement(sql);
        stmt.setString(1, username);
        stmt.setString(2, passwor d);
        

  2. **使用ORM框架**

     * 像Hibernate、MyBatis这样的ORM框架会自动处理SQL参数,避免了手动拼接SQL的风险。
  3. **过滤和转义用户输入**

     * 对用户输入进行严格的验证和过滤,如长度限制、格式校验、特殊字符转义等。
     * 可以使用一些成熟的过滤库,如OWASP的ESAPI。
  4. **限制数据库权限**

     * 为应用程序设置最小权限的数据库账号,避免权限过大带来的风险。
  5. **使用Web应用防火墙(WAF)**

     * WAF可以检测和阻止常见的SQL注入攻击。

## 异常分类

在Java中,所有的异常都派生自`java.lang.Throwable`类。`Throwable`类有两个主要子类:`Error`和`Exception`。

### Error

`Error`类层次结构描述了Java运行时系统的内部错误和资源耗尽错误。这些错误通常是不可恢复的,应用程序不应该试图捕获或处理这些错误。一些常见的`Error`类型包括:

  1. **OutOfMemoryError** : 当Java虚拟机无法分配对象所需的内存时抛出。
  2. **StackOverflowError** : 当应用程序递归太深导致栈溢出时抛出。
  3. **NoClassDefFoundError** : 当Java虚拟机无法加载所需的类时抛出。

### Exception

`Exception`类是程序员可以捕获和处理的异常。`Exception`类又分为两种类型:

#### 1\. 已检查异常(Checked Exception)

已检查异常是编译器可以检测到的异常,程序员必须显式地捕获或抛出这些异常。一些常见的已检查异常包括:

  * **IOException** : 当发生输入/输出操作失败时抛出。
  * **SQLException** : 当发生数据库操作失败时抛出。
  * **ClassNotFoundException** : 当Java虚拟机无法加载所需的类时抛出。

#### 2\. 未检查异常(Unchecked Exception)

未检查异常是编译器无法检测到的异常,程序员可以选择捕获或不捕获。未检查异常通常是由于程序错误导致的,如空指针引用、数组下标越界等。一些常见的未检查异常包括:

  * **NullPointerException** : 当应用程序试图在null对象上调用实例方法时抛出。
  * **ArrayIndexOutOfBoundsException** : 当应用程序试图访问数组中不存在的索引时抛出。
  * **ArithmeticException** : 当发生算术运算错误时抛出,如除数为零。

### 异常处理

在Java中,我们可以使用`try-catch-
finally`语句块来捕获和处理异常。`try`块包含可能抛出异常的代码,`catch`块捕获并处理异常,`finally`块用于执行必须执行的清理代码。

    
    
    try {
        // 可能抛出异常的代码
    } catch (Exception1 e) {
        // 处理Exception1异常
    } catch (Exception2 e) {
        // 处理Exception2异常
    } finally {
        // 清理代码
    }
    

## redis过期策略

Redis是一个高性能的内存数据库,支持多种数据结构和丰富的功能。其中,Redis的过期策略是一个重要的特性,用于自动删除过期的键,释放内存空间。

### Redis的过期策略

Redis提供了两种过期策略:

  1. **被动过期(Passive Expiration)**

     * 当客户端访问一个键时,Redis会检查该键是否已过期。如果已过期,则删除该键并返回空值。
     * 优点是节省CPU资源,只有在访问键时才进行过期检查。
     * 缺点是可能存在过期键未被及时删除,占用内存空间。
  2. **主动过期(Active Expiration)**

     * Redis会定期随机抽取一些键进行过期检查,如果发现过期键则删除。
     * 优点是可以及时删除过期键,释放内存空间。
     * 缺点是会占用一定的CPU资源进行过期检查。

### 过期键的删除策略

Redis采用了以下策略来删除过期键:

  1. **惰性删除(Lazy Deletion)**

     * 在访问键时,如果发现键已过期,则删除该键。
     * 优点是节省CPU资源,只有在访问键时才进行删除操作。
     * 缺点是可能存在过期键未被及时删除,占用内存空间。
  2. **定期删除(Periodic Deletion)**

     * Redis会定期随机抽取一些键进行过期检查,如果发现过期键则删除。
     * 定期删除的频率和检查的键数量可以通过配置文件进行调整。
     * 优点是可以及时删除过期键,释放内存空间。
     * 缺点是会占用一定的CPU资源进行过期检查。

### 过期键的淘汰策略

当Redis内存不足时,会触发内存淘汰机制。Redis提供了以下几种淘汰策略:

  1. **noeviction** : 不淘汰任何键,当内存不足时,新写入操作会报错。
  2. **allkeys-lru** : 淘汰整个键值字典中最久未使用(Least Recently Used)的键。
  3. **volatile-lru** : 淘汰设置了过期时间的键中最久未使用的键。
  4. **allkeys-random** : 随机淘汰整个键值字典中的键。
  5. **volatile-random** : 随机淘汰设置了过期时间的键。
  6. **volatile-ttl** : 淘汰设置了过期时间的键中剩余寿命(Time To Live)最短的键。

可以根据实际需求选择合适的淘汰策略,平衡内存使用和数据持久性。

### 过期时间的设置

可以使用以下命令为键设置过期时间:

  * `EXPIRE key seconds`: 为键设置秒级过期时间。
  * `PEXPIRE key milliseconds`: 为键设置毫秒级过期时间。
  * `EXPIREAT key timestamp`: 为键设置秒级Unix时间戳过期时间。
  * `PEXPIREAT key milliseconds-timestamp`: 为键设置毫秒级Unix时间戳过期时间。

## RocketMQ怎么保证集群模式下顺序消费

RocketMQ是一个分布式消息队列系统,支持集群部署以提高可用性和吞吐量。在集群模式下,RocketMQ通过以下机制来保证消息的顺序消费:

### 1\. 消息队列的顺序性

RocketMQ的消息队列是一个FIFO(First In First
Out)队列,即先进入队列的消息会先被消费。每个消息队列内部的消息是有序的,消费者按照消息在队列中的顺序进行消费。

### 2\. 消息分区(Message Partitioning)

RocketMQ支持将消息按照一定的规则分区,将具有相同特征的消息发送到同一个消息队列中。通常,可以根据消息的某个字段(如订单ID)进行分区,保证相关联的消息在同一个队列中,从而实现顺序消费。

### 3\. 消费者的顺序消费

RocketMQ的消费者可以通过设置消费模式为`CONSUME_FROM_FIRST_OFFSET`或`CONSUME_FROM_LAST_OFFSET`来保证顺序消费。

  * `CONSUME_FROM_FIRST_OFFSET`: 从队列的开头开始消费,保证消费者按照消息在队列中的顺序进行消费。
  * `CONSUME_FROM_LAST_OFFSET`: 从队列的末尾开始消费,保证消费者按照消息到达队列的顺序进行消费。

### 4\. 消费者的并发控制

为了保证顺序消费,RocketMQ要求同一个消费者组内的消费者数量不能超过订阅的消息队列数量。这样可以确保每个消费者只消费一个或多个特定的消息队列,而不会出现多个消费者同时消费同一个队列的情况,从而保证了顺序消费。

### 5\. 消息重试机制

RocketMQ提供了消息重试机制,当消费者消费消息失败时,消息会重新发送给消费者进行消费。重试机制确保了消息不会因为消费失败而丢失,同时也保证了消息的顺序性。

## spring事务的传播

在Spring框架中，事务传播行为定义了业务方法对事务的控制方式，即当一个事务管理的方法被另一个事务管理的方法调用时，这个事务如何被传播。Spring提供了多种事务传播行为选项，这些选项允许开发者根据具体需求选择最合适的事务管理策略。以下是Spring支持的事务传播行为类型及其说明：

  1. **`REQUIRED`** （默认）: 如果当前存在事务，则加入该事务；如果当前没有事务，则创建一个新的事务。

  2. **`SUPPORTS`** : 如果当前存在事务，则加入该事务；如果当前没有事务，则以非事务方式执行。

  3. **`MANDATORY`** : 如果当前存在事务，则加入该事务；如果当前没有事务，则抛出异常。

  4. **`REQUIRES_NEW`** : 总是启动一个新的事务，如果当前存在事务，则将当前事务挂起。

  5. **`NOT_SUPPORTED`** : 总是以非事务方式执行，如果当前存在事务，则将当前事务挂起。

  6. **`NEVER`** : 总是以非事务方式执行，如果当前存在事务，则抛出异常。

  7. **`NESTED`** : 如果当前存在事务，则在嵌套事务内执行。如果当前没有事务，则其行为与`REQUIRED`一样。

这些传播行为让开发者可以精确控制事务的边界和方式，确保业务逻辑的正确执行。例如，使用`REQUIRES_NEW`传播行为可以保证被调用的方法具有自己的独立事务，不受调用者事务的影响，这在需要确保某个业务操作不被外部事务影响时非常有用。而`NESTED`传播行为允许在同一个事务中创建多个保存点，使得内部事务可以独立于外部事务进行回滚，而不影响外部事务的完整性。

## spring cloud的组成

Spring Cloud是一个基于Spring
Boot的工具集，用于构建分布式系统中的一些常见模式（如配置管理、服务发现、断路器、智能路由、微代理、控制总线、全局锁、领导选举、分布式会话和集群状态）。它利用Spring
Boot的开发便利性简化了分布式系统基础设施的开发，使得开发者可以快速地启动和构建自己的服务。

Spring Cloud的主要组件包括但不限于：

  1. **Spring Cloud Config** : 提供服务端和客户端支持，用于外部化配置的管理。它可以使用一个中心化的外部配置仓库，如Git或SVN，来管理所有环境中应用程序的配置。

  2. **Spring Cloud Netflix** :

     * **Eureka** : 服务发现组件，提供了服务注册和发现的机制。
     * **Hystrix** : 提供了断路器功能，用于控制服务间调用的点对点压力。
     * **Zuul** : 提供了API网关服务，管理进出应用程序的流量。
  3. **Spring Cloud Consul** : 提供了服务发现和配置管理的功能，通过整合Consul实现。

  4. **Spring Cloud Gateway** : 是一个新的基于Spring Framework 5, Project Reactor和Spring Boot 2.0的网关服务，旨在提供一种简单有效的方式来路由到API，并为它们提供跨域处理、安全、监控/指标和弹性。

  5. **Spring Cloud Sleuth** : 提供了分布式追踪的解决方案，帮助开发者了解服务间的调用链路。

  6. **Spring Cloud Stream** : 用于构建消息驱动的微服务，提供了与Apache Kafka、RabbitMQ等消息中间件的集成。

  7. **Spring Cloud Bus** : 通过轻量消息代理连接分布式系统的节点，用于广播状态更改或事件（如配置更改事件）。

  8. **Spring Cloud Security** : 提供了一套安全的机制，用于构建安全的微服务。

  9. **Spring Cloud OpenFeign** : 一个声明式的Web服务客户端，它使得编写Web服务客户端变得更简单。

