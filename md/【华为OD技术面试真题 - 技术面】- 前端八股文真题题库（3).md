## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * Webpack loader和plugin区别
  *     *       * Webpack Loader
      * Webpack Plugin
      * 总结
  * 攻击手段 xss csrf 这些 具体怎么攻击
  *     *       * 1\. XSS（跨站脚本攻击）
      * 2\. CSRF（跨站请求伪造）
  * 原型链
  *     *       * 原型链的工作原理：
      * 一个简单的例子：
  * 怎么创建一个没有原型的对象
  *     *       * 使用 `Object.create(null)` 创建对象
  * Constructor 可不可以写多次在class里面
  *     *       * 示例：
      * 错误示例：
  * ES6 的Proxy
  *     *       * Proxy 基本概念
      * Handler 对象的方法
      * 示例：使用 Proxy

![封面](https://i-blog.csdnimg.cn/blog_migrate/531481147412447605047d39bc063274.png)

## Webpack loader和plugin区别

#### Webpack Loader

Loader 在 Webpack 中用于处理源文件。Webpack 自身只能理解 JavaScript 和 JSON 文件，Loader 让 Webpack
有能力去处理其他类型的文件，并将它们转换为有效的模块，这些模块可以被包含在依赖图中。简单地说，Loader 用于转换特定类型的文件并将其包含到依赖图中。

  * **用途** ：比如，将 TypeScript 转换为 JavaScript，将 SCSS 转换为 CSS，或将 JSX 转换为 JavaScript。
  * **配置方式** ：在 Webpack 的配置文件中，Loader 是作为模块规则（module rules）来配置的。你可以指定多个 Loader 来处理不同类型的文件。

例如，使用 `babel-loader` 处理 JavaScript 文件的配置：

    
    
    module: {
      rules: [
        {
          test: /\.js$/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env']
            }
          }
        }
      ]
    }
    

#### Webpack Plugin

Plugin 在 Webpack 中用于执行更广泛的任务。它们直接影响到 Webpack
构建过程，可以用于执行范围广泛的任务，如打包优化、资源管理和环境变量注入等。

  * **用途** ：比如，优化打包文件，管理输出资产，定义环境变量等。
  * **配置方式** ：在 Webpack 配置中，Plugin 是在 `plugins` 数组中直接添加的。

例如，使用 `HtmlWebpackPlugin` 来自动生成 HTML 文件的配置：

    
    
    const HtmlWebpackPlugin = require('html-webpack-plugin');
    
    module.exports = {
      plugins: [
        new HtmlWebpackPlugin({
          template: './src/index.html'
        })
      ]
    }
    

#### 总结

  * **Loader** ：专注于单个文件的转换。
  * **Plugin** ：影响整个构建流程和 Webpack 的核心功能。

## 攻击手段 xss csrf 这些 具体怎么攻击

#### 1\. XSS（跨站脚本攻击）

XSS
攻击是通过将恶意脚本注入到网页上，然后当其他用户浏览该网页时执行这些脚本，从而达到攻击目的。这种攻击通常利用网站允许用户输入未经充分过滤或未正确转义的数据。

  * **攻击方式** ：

    * **存储型 XSS** ：恶意脚本存储在服务器上（如数据库、消息论坛、访客日志等），任何访问该数据的用户都会触发这些脚本。
    * **反射型 XSS** ：恶意脚本在用户的请求中发送，通过诸如 URL 参数的方式，当用户点击一个恶意链接时，服务器将脚本作为响应的一部分返回，脚本随即在用户的浏览器上执行。
    * **DOM 基 XSS** ：当脚本通过修改页面的 DOM 而执行时，源于客户端的数据处理不当，比如 JavaScript 可以读取 URL 参数并动态修改 HTML 内容。
  * **防御措施** ：

    * 对所有输入进行过滤和转义，特别是来自用户的输入。
    * 使用内容安全策略（CSP）限制资源的获取。
    * 对存储的数据进行适当的编码和处理。

#### 2\. CSRF（跨站请求伪造）

CSRF 攻击是指攻击者诱使用户的浏览器去执行未经认证的操作，如在用户不知情的情况下，使用用户当前的登录状态发起恶意请求。

  * **攻击方式** ：

    * 攻击者创建一个恶意网站或邮件，其中包含一个请求指向一个合法网站（用户已登录的），例如通过隐藏的表单自动提交。
    * 当用户浏览到这个恶意网站时，如果他们已经登录了目标网站，那么这个请求就会在用户的浏览器上以用户的身份自动发送。
  * **防御措施** ：

    * 使用 CSRF 令牌（Anti-CSRF tokens），每个会话生成一个唯一的令牌，用于验证用户提交的请求确实是他们意图发送的。
    * 对敏感操作使用双重验证。
    * 设置并验证 HTTP 的 `Referer` 和 `Origin` 头部，以确保请求是从合法的源发起的。

## 原型链

#### 原型链的工作原理：

  1. **原型对象（Prototype Object）** ：JavaScript 中的每个函数都有一个特殊的属性叫做 `prototype`。这个 `prototype` 属性是一个对象，它包含应该由特定类型的所有实例继承的属性和方法。例如，如果有一个 `Person` 函数，那么 `Person.prototype` 将包含所有 `Person` 实例应该共享的属性和方法。

  2. **构造函数（Constructor）** ：当使用 `new` 关键字创建一个新对象时，这个新对象会继承其构造函数的 `prototype` 对象。例如，使用 `new Person()` 创建的所有对象将继承自 `Person.prototype`。

  3. **原型链（Prototype Chain）** ：当访问一个对象的属性或方法时，如果对象本身没有这个属性或方法，JavaScript 会尝试在对象的原型（即 `Person.prototype`）中查找。如果在原型中也找不到，那么 JavaScript 会查找原型的原型，依此类推，直到找到该属性或方法或到达原型链的末端（通常结束于 `Object.prototype`）。

#### 一个简单的例子：

    
    
    function Person(name) {
      this.name = name;
    }
    
    Person.prototype.greet = function() {
      console.log('Hello, my name is ' + this.name);
    };
    
    var alice = new Person('Alice');
    alice.greet(); // 输出: Hello, my name is Alice
    

在这个例子中：

  * `Person` 函数有一个 `prototype` 属性，我们向它添加了一个 `greet` 方法。
  * 创建的 `alice` 对象使用 `new Person('Alice')`，它继承自 `Person.prototype`。
  * 当调用 `alice.greet()` 时，虽然 `greet` 方法不是 `alice` 对象本身的属性，但由于原型链的存在，JavaScript 查找到 `Person.prototype` 中的 `greet` 方法并执行它。

## 怎么创建一个没有原型的对象

在 JavaScript 中，如果您想创建一个没有原型的对象，即一个不继承任何方法或属性（例如 `Object.prototype` 中的方法），可以使用
`Object.create(null)` 方法。这种方法会创建一个纯净的对象，它不继承任何东西，甚至基本的对象功能，如
`toString`、`hasOwnProperty` 等也不会有。

#### 使用 `Object.create(null)` 创建对象

`Object.create` 方法允许您指定一个原型对象作为新创建的对象的原型。通过传递 `null` 作为参数，您可以确保新对象不具有原型链：

    
    
    var obj = Object.create(null);
    
    console.log(obj.toString);      // undefined
    console.log('toString' in obj); // false
    console.log(obj.hasOwnProperty('toString')); // TypeError: obj.hasOwnProperty is not a function
    

在上面的例子中，尝试访问 `toString` 方法会返回 `undefined`，因为它不是 `obj` 对象的一部分。同样，尝试使用
`hasOwnProperty` 方法会导致错误，因为这个方法也不在对象上。

## Constructor 可不可以写多次在class里面

在 JavaScript 的类定义中，构造函数是通过 `constructor` 方法来指定的，它用于创建和初始化类创建的对象。根据 JavaScript
的类语法，一个类中只能有一个 `constructor` 方法。如果在一个类中定义了多个 `constructor` 方法，将会引发语法错误。

#### 示例：

这是一个定义良好的类，包含一个 `constructor`：

    
    
    class Person {
      constructor(name) {
        this.name = name;
      }
    
      greet() {
        console.log(`Hello, my name is ${this.name}`);
      }
    }
    
    const alice = new Person('Alice');
    alice.greet();  // 输出：Hello, my name is Alice
    

#### 错误示例：

下面的例子展示了尝试在一个类中包含多个 `constructor` 方法时会发生什么：

    
    
    class Person {
      constructor(name) {
        this.name = name;
      }
    
      constructor(age) {  // 这会导致语法错误
        this.age = age;
      }
    
      greet() {
        console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
      }
    }
    

这段代码在尝试编译时会抛出一个语法错误，因为 `Person` 类试图包含两个 `constructor` 方法。

![image-20240426164059562](https://i-blog.csdnimg.cn/blog_migrate/b71d318b7092783882bc4018f2873ac3.png)

## ES6 的Proxy

在 JavaScript 中，ES6 引入了 `Proxy`
这一新特性，它允许创建一个对象的代理（proxy），从而可以拦截并自定义对象的基本操作，例如属性读取、属性赋值、函数调用等。

#### Proxy 基本概念

`Proxy` 对象用于定义基本操作的自定义行为（如属性查找、赋值、枚举、函数调用等）。其构造函数语法如下：

    
    
    var proxy = new Proxy(target, handler);
    

  * **target** ：目标对象（可以是任何类型的对象，包括数组、函数或其他代理）。
  * **handler** ：一个对象，其属性是当执行一个操作时定义代理的行为的函数。

#### Handler 对象的方法

`handler` 对象可以定义很多种方法，这些方法对应不同的操作，比如：

  * `get(target, propKey, receiver)`：拦截对象属性的读取。
  * `set(target, propKey, value, receiver)`：拦截对象属性的设置。
  * `has(target, propKey)`：拦截 `propKey in proxy` 的操作，返回一个布尔值。
  * `deleteProperty(target, propKey)`：拦截 `delete proxy[propKey]` 的操作，返回一个布尔值。

#### 示例：使用 Proxy

下面是一个简单的例子，演示如何使用 `Proxy` 来拦截对象属性的读取和设置：

    
    
    let target = {
      message1: "hello",
      message2: "everyone"
    };
    
    let handler = {
      get: function(target, prop, receiver) {
        if (prop in target) {
          return `${target[prop]} world!`;
        }
        return `Property not found`;
      },
      set: function(target, prop, value) {
        if (value.length > 5) {
          target[prop] = value;
          return true;
        } else {
          console.log("Failed: value too short!");
          return false;
        }
      }
    };
    
    let proxy = new Proxy(target, handler);
    
    console.log(proxy.message1); // 输出: hello world!
    proxy.message2 = "hi";        // 输出: Failed: value too short!
    proxy.message2 = "everyone";  // 设置成功
    console.log(proxy.message2);  // 输出: everyone world!
    

在这个例子中：

  * `get` 方法增加了对任何被读取属性的修改。
  * `set` 方法对属性的赋值进行了条件限制。

