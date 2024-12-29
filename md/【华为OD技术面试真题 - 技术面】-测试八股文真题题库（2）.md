## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 黑盒测试的8种测试方法
  * 3次握手4次挥手
  *     *       * 三次握手 (Three-Way Handshake)
      * 四次挥手 (Four-Way Handshake)
  * UI自动化测试
  *     *       * UI自动化测试的优点：
  * po模型的分层
  *     *       * Page Object 模型 (Page Object Model, POM)
      * PO模型的分层结构：
  * 开发设计说明书的评审会议参与过没有
  * 实现获取本机的物理地址和ip地址
  * 提出的bug开发人员不认
  * 抓包
  *     *       * 工具选择
  * 用例的设计
  * 黑盒测试方法在项目里具体的运用

![封面](https://i-blog.csdnimg.cn/blog_migrate/044c13f12b7b05fa860f365d481b03ab.png)

## 黑盒测试的8种测试方法

> [八大黑盒测试方法总结【超详细】_黑盒测试的八大测试方法-
> CSDN博客](https://blog.csdn.net/Gabbana/article/details/108698502)

  1. 等价类划分：将输入条件划分为等价类，从每个等价类中选择测试用例，以代表该等价类的典型情况。

  2. 边界值分析：通过选择接近或在边界值上的测试用例，检测系统在边界处的行为。

  3. 错误推测：基于对系统的理解和经验，推测可能存在的错误，并设计测试用例来验证这些错误是否存在。

  4. 因果图法：使用因果图展示系统中各个输入和输出之间的关系，根据因果关系设计测试用例。

  5. 判定图测试：将系统行为建模为一组规则，设计测试用例以覆盖这些规则的各种组合情况。

  6. 状态迁移测试：针对系统的状态转换进行测试，包括测试状态之间的转换触发条件和动作。

  7. 错误猜测：基于对系统的理解和经验，猜测可能存在的错误类型，并设计测试用例来验证这些错误。

  8. 正交测试：使用正交表设计测试用例，以覆盖系统输入的各种组合情况，从而减少测试用例的数量。

## 3次握手4次挥手

#### 三次握手 (Three-Way Handshake)

三次握手是TCP协议建立连接的过程，用于确保连接的双方能够成功通信。具体步骤如下：

  1. **SYN** ：

     * 客户端向服务器发送一个SYN（synchronize）报文，表示请求建立连接。
     * 报文包含初始序列号（ISN, Initial Sequence Number）。
  2. **SYN-ACK** ：

     * 服务器收到SYN报文后，响应一个SYN-ACK报文。
     * 服务器也生成一个自己的初始序列号，并在SYN-ACK报文中发送给客户端。
     * 同时确认（ACK）客户端的SYN报文，序列号加1。
  3. **ACK** ：

     * 客户端收到服务器的SYN-ACK报文后，向服务器发送一个ACK报文，确认服务器的SYN报文。
     * 这一步完成后，连接建立，客户端和服务器可以开始传输数据。

#### 四次挥手 (Four-Way Handshake)

四次挥手是TCP协议关闭连接的过程，用于确保连接的双方能够成功关闭通信。具体步骤如下：

  1. **FIN** ：

     * 客户端向服务器发送一个FIN（finish）报文，表示请求关闭连接。
     * 客户端进入FIN_WAIT_1状态。
  2. **ACK** ：

     * 服务器收到FIN报文后，响应一个ACK报文，确认客户端的FIN报文。
     * 服务器进入CLOSE_WAIT状态，客户端进入FIN_WAIT_2状态。
  3. **FIN** ：

     * 服务器准备好关闭连接时，发送一个FIN报文给客户端。
     * 服务器进入LAST_ACK状态。
  4. **ACK** ：

     * 客户端收到服务器的FIN报文后，响应一个ACK报文，确认服务器的FIN报文。
     * 客户端进入TIME_WAIT状态，服务器关闭连接。
     * 在等待一段时间（通常是2倍的MSL，Maximum Segment Lifetime）后，客户端关闭连接，进入CLOSED状态。

## UI自动化测试

UI自动化测试是使用自动化工具模拟用户在图形用户界面（GUI）上的操作，以验证软件应用程序的功能和性能。UI自动化测试的主要目的是提高测试效率和覆盖率，减少人为错误，并确保应用程序在各种环境下都能正常运行。UI自动化测试属于黑盒测试(功能测试)

适合的UI自动化测试工具：如Selenium、Appium、Cypress，**TestCafe** 等。

#### UI自动化测试的优点：

  * **提高效率** ：自动化测试能够快速执行大量测试用例，比手动测试更高效。
  * **提高覆盖率** ：可以在各种环境和设备上运行，增加测试覆盖率。
  * **可重复性** ：测试脚本可以重复运行，确保一致性和可靠性。
  * **减少人为错误** ：自动化测试减少了人为操作的错误，提高了测试的准确性。

## po模型的分层

#### Page Object 模型 (Page Object Model, POM)

Page Object
模型是一种设计模式，用于自动化测试中，旨在提高测试代码的可维护性和可读性。它通过将页面上的元素和操作封装到对象中，使测试脚本与页面细节解耦。

#### PO模型的分层结构：

  1. **页面层 (Page Layer)** ：

     * **Page Object 类** ：每个页面或组件都有一个对应的类，这个类封装了页面上的所有元素和操作。例如，登录页面可能有一个LoginPage类，它包含了用户名输入框、密码输入框和登录按钮等元素，以及登录操作的方法。
    
        public class LoginPage {
        WebDriver driver;
    
        // 定位器
        By usernameField = By.id("username");
        By passwordField = By.id("password");
        By loginButton = By.id("login");
    
        // 构造函数
        public LoginPage(WebDriver driver) {
            this.driver = driver;
        }
    
        // 操作方法
        public void enterUsername(String username) {
            driver.findElement(usernameField).sendKeys(username);
        }
    
        public void enterPassword(String password) {
            driver.findElement(passwordField).sendKeys(password);
        }
    
        public void clickLoginButton() {
            driver.findElement(loginButton).click();
        }
    }
    

  2. **业务逻辑层 (Business Logic Layer)** ：

     * **业务方法** ：在这一层，多个页面对象的操作被组合成更高级别的业务逻辑。例如，登录操作可以在业务逻辑层中组合调用LoginPage类中的方法。
    
        public class LoginActions {
        WebDriver driver;
        LoginPage loginPage;
    
        // 构造函数
        public LoginActions(WebDriver driver) {
            this.driver = driver;
            loginPage = new LoginPage(driver);
        }
    
        // 登录业务方法
        public void login(String username, String password) {
            loginPage.enterUsername(username);
            loginPage.enterPassword(password);
            loginPage.clickLoginButton();
        }
    }
    

  3. **测试层 (Test Layer)** ：

     * **测试脚本** ：在这一层，测试脚本调用业务逻辑层的方法进行测试。测试脚本只关心测试逻辑，而不需要了解具体的页面细节。
    
        public class LoginTest {
        WebDriver driver;
        LoginActions loginActions;
    
        @Before
        public void setUp() {
            // 初始化WebDriver和LoginActions
            driver = new ChromeDriver();
            loginActions = new LoginActions(driver);
        }
    
        @Test
        public void testLogin() {
            // 打开登录页面
            driver.get("https://example.com/login");
    
            // 执行登录操作
            loginActions.login("testuser", "testpassword");
    
            // 验证登录结果
            // Assert语句可以验证登录是否成功
        }
    
        @After
        public void tearDown() {
            // 关闭浏览器
            driver.quit();
        }
    }
    

## 开发设计说明书的评审会议参与过没有

联系个人实际i回答

## 实现获取本机的物理地址和ip地址

使用 `os.popen` 来获取本机的物理地址（MAC地址）和IP地址，可以通过执行系统命令来实现。以下是一个示例代码：

    
    
    import os
    import re
    
    def get_ip_addresses():
        ip_addresses = []
        ifconfig_result = os.popen('ifconfig').read()
        ip_pattern = re.compile(r'inet\s(\d+\.\d+\.\d+\.\d+)')
        ip_addresses = ip_pattern.findall(ifconfig_result)
        return ip_addresses
    
    def get_mac_addresses():
        mac_addresses = []
        ifconfig_result = os.popen('ifconfig').read()
        mac_pattern = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})')
        mac_addresses = mac_pattern.findall(ifconfig_result)
        # Join the MAC address parts
        mac_addresses = [''.join(mac) for mac in mac_addresses]
        return mac_addresses
    
    # 获取IP地址
    ips = get_ip_addresses()
    print("IP Addresses:", ips)
    
    # 获取MAC地址
    macs = get_mac_addresses()
    print("MAC Addresses:", macs)
    
    
    
    import socket
    import uuid
    ip = socket.gethostbyname(socket.gethostname())
    node = uuid.getnode()
    macHex = uuid.UUID(int=node).hex[-12:]
    mac =[]
    for i in range(len(macHex))[::2]:
    mac.append(macHex[i:i+2])
    mac =':'.join(mac)
    print('IP:', ip)
    print('MAC:', mac)
    

## 提出的bug开发人员不认

随便说，只要不导致冲突，解决问题就行。

“当开发人员不认同发现的 Bug 时，我会首先确保我的 Bug
报告足够详细，包括重现步骤、预期结果和实际结果，并附上相关的截图或日志。如果仍然有分歧，我会亲自或与开发人员一起重现问题，确保他们能够亲眼看到 Bug
的存在。同时，我会保持开放和建设性的沟通，解释问题的严重性和影响，并在必要时寻求其他团队成员或主管的意见来解决分歧。”

## 抓包

抓包（Packet
Capturing）是指通过网络分析工具截获和记录网络数据包，以便进行分析和调试。抓包有助于了解网络通信的详细信息，包括请求和响应数据、协议使用情况等。

#### 工具选择

常用的抓包工具有：

  * **Wireshark** ：功能强大且广泛使用的网络协议分析工具。
  * **tcpdump** ：基于命令行的网络数据包分析工具，通常用于 Unix 系统。
  * **Fiddler** ：专注于 HTTP/HTTPS 流量的调试代理工具。

## 用例的设计

  * **用例标识** ：为每个用例分配唯一的标识符。
  * **用例描述** ：简要描述用例的目的。
  * **前置条件** ：列出执行该用例所需的前置条件。
  * **测试步骤** ：详细列出执行测试的步骤。
  * **预期结果** ：明确每一步的预期结果。
  * **实际结果** ：执行测试后记录的实际结果（用于测试执行阶段）

## 黑盒测试方法在项目里具体的运用

需要结合自己做过的项目来说

