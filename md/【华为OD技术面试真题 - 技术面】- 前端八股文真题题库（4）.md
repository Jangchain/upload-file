## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 基本数据类型
  *     *       * 1\. 数字（Number）
      * 2\. 字符串（String）
      * 3\. 布尔值（Boolean）
      * 4\. 未定义（Undefined）
      * 5\. 空（Null）
      * 6\. 符号（Symbol）
      * 7\. 大整数（BigInt）
  * ES6的新特性
  *     *       * 1\. 块级作用域和 `let`/`const`
      * 2\. 箭头函数
      * 3\. 模板字符串
      * 4\. 解构赋值
      * 5\. 扩展运算符
      * 6\. 类
      * 7\. Promise
      * 8\. 模块
  * vue值传递的方式
  *     *       * 1\. Props 和 Events（父子组件通信）
      * 2\. Event Bus（跨组件通信）
      * 3\. Vuex（全局状态管理）
      * 4\. Provide / Inject（祖孙组件通信）
  * 浏览器三种本地存储的区别
  *     *       * 1\. Cookies
      * 2\. localStorage
      * 3\. sessionStorage
  * vuex和localStorage的区别
  *     *       * Vuex
      * localStorage
      * 核心区别
  * 普通函数和[箭头函数](https://so.csdn.net/so/search?q=箭头函数&spm=1001.2101.3001.7020)的区别
  *     *       * 1\. `this` 关键字的绑定
      * 2\. 构造函数
      * 3\. `arguments` 对象
      * 4\. 显式返回值
      * 5\. 使用场景和语法简洁性
  * vue compute和watch的区别和使用场景
  *     *       * 计算属性（Computed Properties）
      * 侦听器（Watchers）
  * js事件循环，宏任务微任务
  *     *       * JavaScript 事件循环基本原理
      * 宏任务（Macro-tasks）
      * 微任务（Micro-tasks）
      * 事件循环的执行顺序
  * 前端性能优化指标
  *     *       * 1\. 首字节时间 (Time to First Byte, TTFB)
      * 2\. 首次内容绘制 (First Contentful Paint, FCP)
      * 3\. 可交互时间 (Time to Interactive, TTI)
      * 4\. 页面加载时间 (Load Time)
      * 5\. 累计布局偏移 (Cumulative Layout Shift, CLS)
      * 6\. 网络请求数量与体积
  * 前端跨域请求问题
  *     *       * 1\. **CORS（跨源资源共享）**
      * 2\. **JSONP（JSON with Padding）**
      * 3\. **代理服务器**

## 基本数据类型

#### 1\. 数字（Number）

JavaScript使用浮点数表示数字，这些数字遵循IEEE 754标准，可以表示整数和小数。

**特点** ：

  * `Number`类型在JavaScript中表示所有的数字，包括整数和浮点数。
  * 特殊的值：`NaN`（Not a Number，非数字）和`Infinity`（无穷大）。

**示例** ：

    
    
    let intNum = 42;        // 整数
    let floatNum = 3.14;    // 浮点数
    console.log(NaN);       // 输出NaN
    console.log(1 / 0);     // 输出Infinity
    

#### 2\. 字符串（String）

字符串表示字符序列，用双引号、单引号或反引号括起来。反引号（模板字符串）允许多行字符串和嵌入变量。

**特点** ：

  * 字符串是不可变的。
  * 反引号（模板字符串）可以嵌入变量和表达式。

**示例** ：

    
    
    let singleQuoteStr = 'Hello, World!';
    let doubleQuoteStr = "Hello, World!";
    let templateStr = `This is a number: ${intNum}`;
    

#### 3\. 布尔值（Boolean）

布尔值有两个取值：`true`（真）和`false`（假）。

**特点** ：

  * 通常用于条件判断和逻辑控制。

**示例** ：

    
    
    let isAvailable = true;
    let isFinished = false;
    

#### 4\. 未定义（Undefined）

`undefined`表示未定义的值，是全局对象的一个属性。

**特点** ：

  * 如果变量被声明但没有初始化，则它的值是`undefined`。
  * 如果函数没有返回值，默认返回`undefined`。

**示例** ：

    
    
    let notAssigned;
    console.log(notAssigned); // 输出undefined
    

#### 5\. 空（Null）

`null`表示“空”或“无值”的对象引用。

**特点** ：

  * `typeof null`返回`"object"`，但它与普通对象不同。

**示例** ：

    
    
    let emptyValue = null;
    console.log(emptyValue); // 输出null
    

#### 6\. 符号（Symbol）

`Symbol`是ES6中引入的一种数据类型，表示独特的标识符。

**特点** ：

  * `Symbol`是唯一的。
  * 通常用于定义对象的私有属性。

**示例** ：

    
    
    let sym1 = Symbol('identifier');
    let sym2 = Symbol('identifier');
    console.log(sym1 === sym2); // 输出false
    

#### 7\. 大整数（BigInt）

`BigInt`允许表示任意精度的整数，适用于操作非常大的整数。

**特点** ：

  * 以`n`结尾的数值表示`BigInt`。
  * 不与`Number`混用。

**示例** ：

    
    
    let bigInt = 123456789012345678901234567890n;
    console.log(bigInt + 1n); // 输出123456789012345678901234567891n
    

## [ES6](https://so.csdn.net/so/search?q=ES6&spm=1001.2101.3001.7020)的新特性

ES6（ECMAScript 2015）是JavaScript的一个重要版本

#### 1\. 块级作用域和 `let`/`const`

ES6 引入了 `let` 和 `const` 两种新的变量声明方式，具有块级作用域，相比 `var` 更加安全。

  * **`let`** ：声明可重新赋值的变量。
  * **`const`** ：声明只读的常量。

**示例** ：

    
    
    function testBlockScope() {
        if (true) {
            let x = 10;
            const y = 20;
            console.log(x, y); // 输出10, 20
        }
        // console.log(x, y); // 抛出ReferenceError，因为x和y超出块作用域
    }
    testBlockScope();
    

#### 2\. 箭头函数

箭头函数提供了更简洁的函数表达方式，并自动绑定 `this` 到外层上下文。

**示例** ：

    
    
    const add = (a, b) => a + b;
    console.log(add(3, 4)); // 输出7
    
    // 箭头函数自动绑定this
    const obj = {
        value: 42,
        getValue: () => this.value // 这里的this指向全局作用域，不是obj本身
    };
    console.log(obj.getValue()); // 输出undefined
    

#### 3\. 模板字符串

模板字符串用反引号（``）包围，支持多行文本和嵌入变量。

**示例** ：

    
    
    const name = "John";
    const greeting = `Hello, ${name}!`;
    console.log(greeting); // 输出Hello, John!
    

#### 4\. 解构赋值

解构赋值使得从数组或对象中提取值并赋值给变量更加简洁。

**示例** ：

    
    
    // 数组解构
    const [first, second] = [10, 20];
    console.log(first, second); // 输出10, 20
    
    // 对象解构
    const user = { name: "Alice", age: 25 };
    const { name, age } = user;
    console.log(name, age); // 输出Alice, 25
    

#### 5\. 扩展运算符

扩展运算符 (`...`) 可以解构数组或对象，并合并数据结构。

**示例** ：

    
    
    // 数组扩展
    const arr1 = [1, 2, 3];
    const arr2 = [...arr1, 4, 5];
    console.log(arr2); // 输出[1, 2, 3, 4, 5]
    
    // 对象扩展
    const obj1 = { a: 1, b: 2 };
    const obj2 = { ...obj1, c: 3 };
    console.log(obj2); // 输出{a: 1, b: 2, c: 3}
    

#### 6\. 类

ES6引入了类的语法糖，使面向对象编程更加简洁。

**示例** ：

    
    
    class Animal {
        constructor(name) {
            this.name = name;
        }
    
        speak() {
            console.log(`${this.name} makes a noise.`);
        }
    }
    
    class Dog extends Animal {
        speak() {
            console.log(`${this.name} barks.`);
        }
    }
    
    const dog = new Dog('Rover');
    dog.speak(); // 输出Rover barks.
    

#### 7\. Promise

`Promise` 用于简化异步操作，解决回调地狱的问题。

**示例** ：

    
    
    function fetchData() {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve('Data received');
            }, 1000);
        });
    }
    
    fetchData().then(data => {
        console.log(data); // 输出Data received
    });
    

#### 8\. 模块

ES6引入了模块化语法，使用 `import` 和 `export` 进行模块的导入与导出。

**示例** ：  
// module.js

    
    
    // 导出
    export const value = 42;
    export function greet() {
        console.log('Hello, World!');
    }
    

// main.js

    
    
    // 导入
    import { value, greet } from './module.js';
    console.log(value); // 输出42
    greet(); // 输出Hello, World!
    

## vue值传递的方式

Vue.js提供了多种方式来传递数据，主要用于组件之间的数据交互。下面是Vue中几种常见的值传递方式：

#### 1\. Props 和 Events（父子组件通信）

  * **Props** ：父组件向子组件传递数据。Props 是单向数据流，只能从父组件流向子组件。
  * **Events** ：子组件向父组件发送消息。子组件使用 `$emit` 触发事件，并可传递数据给父组件。

**示例** ：

    
    
    <!-- 父组件 -->
    <template>
      <div>
        <child-component :parentData="data" @childEvent="handleChildEvent"/>
      </div>
    </template>
    
    <script>
    import ChildComponent from './ChildComponent.vue';
    
    export default {
      components: {
        ChildComponent
      },
      data() {
        return {
          data: 'Data from parent'
        }
      },
      methods: {
        handleChildEvent(data) {
          console.log(data); // 接收子组件传递的数据
        }
      }
    }
    </script>
    
    <!-- 子组件 -->
    <template>
      <div>
        <button @click="sendToParent">Send to Parent</button>
      </div>
    </template>
    
    <script>
    export default {
      props: ['parentData'],
      methods: {
        sendToParent() {
          this.$emit('childEvent', 'Data from child');
        }
      }
    }
    </script>
    

#### 2\. Event Bus（跨组件通信）

Event Bus 是一种使用 Vue 实例作为中央事件总线，在不相关的组件之间通信的技术。

**示例** ：

    
    
    // eventBus.js
    import Vue from 'vue';
    export const EventBus = new Vue();
    
    // 组件A 发送数据
    EventBus.$emit('update', data);
    
    // 组件B 接收数据
    EventBus.$on('update', data => {
      console.log(data);
    });
    

#### 3\. Vuex（全局状态管理）

Vuex 是 Vue 的官方状态管理库，适用于复杂的组件结构，需要全局状态管理的场景。

**示例** ：

    
    
    // store.js
    import Vue from 'vue';
    import Vuex from 'vuex';
    
    Vue.use(Vuex);
    
    export default new Vuex.Store({
      state: {
        data: null
      },
      mutations: {
        updateData(state, data) {
          state.data = data;
        }
      },
      actions: {
        setData({ commit }, data) {
          commit('updateData', data);
        }
      }
    });
    
    // 组件中使用
    this.$store.dispatch('setData', 'New data');
    

#### 4\. Provide / Inject（祖孙组件通信）

这是一种在组件树中深层传递数据的方法，而不必在每层组件间显式传递。

**示例** ：

    
    
    // 祖先组件
    <template>
      <div>
        <descendant-component/>
      </div>
    </template>
    
    <script>
    export default {
      provide: {
        sharedData: 'Data from ancestor'
      }
    }
    </script>
    
    // 孙组件
    <template>
      <div>{{ sharedData }}</div>
    </template>
    
    <script>
    export default {
      inject: ['sharedData']
    }
    </script>
    

## 浏览器三种本地存储的区别

主流浏览器提供了三种常用的本地存储方式：Cookies、localStorage 和 sessionStorage。

#### 1\. Cookies

Cookies 最初被设计来存储少量的用户和服务器间的会话数据。它们存储在用户的设备上，并且每次向同一服务器发送请求时，都会将 Cookie 发送到服务器。

  * **存储大小** ：一般限制为 4KB。
  * **有效期** ：可以设置过期时间。如果不设置过期时间，Cookie 会在浏览器关闭时被删除（会话Cookie）；如果设置了过期时间，数据可以持久保存。
  * **发送请求时** ：每次HTTP请求都会携带在header中，这可能会影响传输效率。
  * **安全性** ：由于每次请求都会发送，故有安全风险。可以通过设置`HttpOnly`属性来增强安全性，使得JavaScript无法读取Cookie。

#### 2\. localStorage

localStorage 提供了更大的存储空间，并且其数据在页面会话间是持久保存的，即使浏览器关闭也不会丢失。

  * **存储大小** ：最大可支持5MB。
  * **有效期** ：数据永久存储，除非被清除（如用户手动清除或通过代码清除）。
  * **与服务器的交互** ：数据保存在本地，不会随着HTTP请求发送到服务器。
  * **使用场景** ：适用于需要大量数据本地存储，且不需要在每次请求时发送到服务器的场景。

#### 3\. sessionStorage

sessionStorage 的用法和 localStorage
类似，但它的存储范围限定在了页面会话中。当页面会话结束（页面被关闭）时，存储的数据也会被清空。

  * **存储大小** ：同样最大可支持5MB。
  * **有效期** ：仅在当前会话中有效，关闭页面或浏览器后数据被清除。
  * **与服务器的交互** ：数据不会随着HTTP请求发送到服务器。
  * **使用场景** ：适用于数据仅在单个会话中需要保持的情况，如表单填写的半途数据。

## vuex和localStorage的区别

#### Vuex

Vuex 是 Vue.js 的官方状态管理库，它主要用于管理 Vue 应用中组件的状态。其设计目的是为了解决复杂组件间的状态共享问题。

  * **数据管理** ：Vuex 通过集中式存储管理所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化。
  * **实时性和响应性** ：Vuex 的状态存储是响应式的，当状态改变时，依赖这些状态的组件会自动重新渲染。
  * **用途** ：适用于大型应用，可以集中管理多个组件的状态，特别是当多个视图依赖于同一状态时。
  * **生命周期** ：Vuex 存储的数据在页面刷新时会丢失，除非进行持久化处理。

#### localStorage

localStorage 是 Web 存储 API 提供的一个接口，允许网站在用户的浏览器中存储数据。它主要用于在本地保存键值对数据。

  * **数据存储** ：提供持久化存储，即使关闭浏览器或重启设备，保存的数据也不会丢失。
  * **容量** ：通常可以存储大约 5MB 的数据。
  * **用途** ：适合于存储少量不经常变动的数据，如用户设置、大型字符串等。
  * **实时性和响应性** ：localStorage 不是响应式的，数据更新不会自动反映到视图上。

#### 核心区别

  * **数据持久性** ：localStorage 提供持久化存储，而 Vuex 默认情况下不提供数据持久化。
  * **用途和复杂性** ：Vuex 用于复杂的状态管理，特别是在多个组件间共享状态的场景；localStorage 更多用于保存用户的偏好设置或其他不需要实时响应的数据。
  * **响应式支持** ：Vuex 支持响应式更新，这是它与 localStorage 的一个重要区别。

##
普通函数和[箭头函数](https://so.csdn.net/so/search?q=%E7%AE%AD%E5%A4%B4%E5%87%BD%E6%95%B0&spm=1001.2101.3001.7020)的区别

以下是普通函数和箭头函数的几个主要区别：

#### 1\. `this` 关键字的绑定

  * **普通函数** ：`this` 的值取决于函数的调用方式。如果是作为对象的方法调用，`this` 指向该对象。如果单独调用函数，`this` 将指向全局对象（在非严格模式下）或者是`undefined`（在严格模式下）。
  * **箭头函数** ：不绑定自己的 `this`，而是捕获其所在上下文的 `this` 值作为自己的 `this`，常称为“词法作用域”或“静态作用域”。这使得箭头函数特别适合用于那些需要维护上下文状态的场景，例如在回调函数中。

#### 2\. 构造函数

  * **普通函数** ：可以用作构造函数，与 `new` 关键字一起使用时，将创建一个新的对象实例。
  * **箭头函数** ：不能用作构造函数，尝试与 `new` 关键字一起使用会抛出错误。

#### 3\. `arguments` 对象

  * **普通函数** ：拥有自己的 `arguments` 对象，这是一个类数组对象，对应于传递给函数的参数。
  * **箭头函数** ：没有自己的 `arguments` 对象，但可以访问外围函数的 `arguments` 对象。

#### 4\. 显式返回值

  * **普通函数** ：需要使用 `return` 语句来显式返回值，除非是构造函数，否则没有返回语句时默认返回 `undefined`。
  * **箭头函数** ：如果函数体只包含一个表达式，则可以省略 `return` 关键字和大括号，直接返回该表达式的结果。如果函数体有多行代码，仍需使用大括号和 `return` 语句。

#### 5\. 使用场景和语法简洁性

  * **普通函数** ：更适合需要动态上下文或需要作为构造函数的场合。
  * **箭头函数** ：由于简洁的语法和处理 `this` 的方式，它非常适合用于需要封装某个作用域内的 `this` 值的情况，如处理事件、定时器或任何需要简洁函数体的回调函数。

## vue compute和watch的区别和使用场景

在 Vue.js 中，计算属性（computed properties）和侦听器（watchers）都是响应式的方法，用来根据组件的状态变化来执行代码。

#### 计算属性（Computed Properties）

**特点** ：

  * 计算属性是基于它们的依赖进行缓存的。只有当一个计算属性依赖的响应式属性发生变化时，它才会重新计算。
  * 通常用于派生一些状态。例如，根据购物车内商品的数量计算总价格。

**使用场景** ：

  * 当需要根据组件的状态计算新的值，并且这些计算值需要频繁重用时，非常适合使用计算属性。这样可以避免在每次访问时都重新执行计算，从而提高效率。
  * 当计算的结果需要依赖于组件内的一个或多个响应式数据源，并且这些数据源更改可能频繁触发重新计算时。

**示例** ：

    
    
    export default {
      data() {
        return {
          cart: [{ price: 5, quantity: 2 }, { price: 15, quantity: 3 }]
        };
      },
      computed: {
        total() {
          return this.cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
        }
      }
    }
    

#### 侦听器（Watchers）

**特点** ：

  * 侦听器适用于观察 Vue 实例上的数据变动，然后执行某个操作，如调用方法或异步操作。
  * 它们不具备缓存功能，数据每次变化时都会执行。

**使用场景** ：

  * 当你需要在数据变化响应时执行更复杂的操作，比如异步或开销较大的操作时，使用侦听器更合适。
  * 当你需要根据状态的变化来做一些事情，如发送 AJAX 请求或更改其他非响应式状态时。

## js事件循环，宏任务微任务

#### JavaScript 事件循环基本原理

JavaScript 是单线程的，意味着在同一时间内只能执行一个任务。为了管理多个任务（尤其是 I/O 密集型或耗时任务），JavaScript
使用事件循环（Event Loop）机制。

事件循环的作用是监视调用栈和任务队列。如果调用栈为空，它会检查任务队列中是否有待处理的任务。如果有，事件循环就会从队列中取出一个任务到调用栈中执行。这个循环机制保证了
JavaScript 可以继续执行而不会被阻塞。

#### 宏任务（Macro-tasks）

宏任务是一种可以分配到 JavaScript 任务队列中的任务类型。每个宏任务完成后，浏览器可以在执行下一个宏任务之前进行渲染操作。

**常见的宏任务包括：**

  * `setTimeout`
  * `setInterval`
  * `setImmediate` (非标准，Node.js 环境中使用)
  * `I/O` 操作
  * `UI 渲染`

#### 微任务（Micro-tasks）

微任务是另一种任务类型，它的执行时机要早于宏任务。在每个宏任务执行完毕后，如果存在微任务队列，那么这些微任务会在下一个宏任务执行之前全部执行完毕。

**常见的微任务包括：**

  * `Promise.then`、`Promise.catch`、`Promise.finally`
  * `process.nextTick` (Node.js 环境中)
  * `MutationObserver`

#### 事件循环的执行顺序

  1. **执行当前宏任务** ：从宏任务队列中取出一个任务执行。
  2. **执行所有微任务** ：在当前宏任务执行完后，立即执行所有排队的微任务。
  3. **渲染UI** ：如果需要，渲染页面。
  4. **重复以上步骤** 。

## 前端性能优化指标

#### 1\. 首字节时间 (Time to First Byte, TTFB)

**概念** ：从用户发出请求到接收到服务器的首字节数据的时间。

**重要性** ：TTFB 指标较低可以反映服务器的响应速度和网络延迟情况。优化 TTFB 主要涉及服务器端的架构、CDN（内容分发网络）以及网络传输优化。

#### 2\. 首次内容绘制 (First Contentful Paint, FCP)

**概念** ：页面首次绘制任何内容的时间，例如文本、图像或 SVG。

**重要性** ：FCP 提供了用户可感知页面内容加载的时间。优化该指标可以减少用户等待的时间，提升页面的首屏加载速度。

#### 3\. 可交互时间 (Time to Interactive, TTI)

**概念** ：页面主要内容完全加载并且可以响应用户交互的时间。

**重要性** ：TTI 是用户体验的关键指标之一。它代表页面从视觉上可用到可以进行交互的时间段，反映页面的整体可用性。通常，长时间的 JavaScript
执行或繁重的计算任务可能会延迟 TTI。

#### 4\. 页面加载时间 (Load Time)

**概念** ：浏览器完全加载页面、包括外部资源（如样式表、图片和脚本）的时间。

**重要性** ：虽然页面完全加载通常不意味着页面可交互，但这可以反映出整体资源下载和解析时间。该指标可以用于检测未优化的资源或外部依赖项的影响。

#### 5\. 累计布局偏移 (Cumulative Layout Shift, CLS)

**概念** ：衡量页面在整个生命周期中视觉稳定性的问题。

**重要性** ：CLS 指标高表示页面在加载或交互期间发生了布局偏移，可能造成用户体验不佳。减少 CLS
可以提供更好的视觉稳定性，防止内容突然移动或跳跃。

#### 6\. 网络请求数量与体积

**概念** ：页面加载时发出的网络请求数量和总请求数据量。

**重要性** ：通过减少不必要的请求和资源体积，页面加载时间可以显著缩短。可通过合并文件、按需加载、压缩资源等方式优化。

## 前端跨域请求问题

在前端开发中，跨域请求问题是一个常见的挑战，尤其是在处理从不同源或域请求数据时。这里是几种常用的解决跨域问题的策略，我会从面试官的角度详细解释每种方法的原理及实际应用场景：

#### 1\. **CORS（跨源资源共享）**

**原理** ：CORS 是一个 W3C 标准，允许服务器通过设置一系列 HTTP 响应头来控制哪些客户端可以访问其资源。

**实践** ：在服务器端设置响应头，如 `Access-Control-Allow-Origin`，来指定哪些域名可以访问资源。例如，将此头设置为 `*`
允许所有域名的访问，或者指定具体域名来限制访问。

#### 2\. **JSONP（JSON with Padding）**

**原理** ：利用 `<script>` 标签没有跨域限制的特点，通过动态创建 `<script>` 标签的方式进行跨域请求。服务器需要以
JavaScript 可执行的形式返回数据。

**实践** ：主要用于 GET 请求。服务器返回的响应是一个函数调用，其参数是 JSON 数据。前端需提前定义好这个函数。由于 JSONP 不支持
POST 请求，且安全性较低（容易受到XSS攻击），现已较少使用。

#### 3\. **代理服务器**

**原理**
：通过配置或创建一个中间服务器来转发请求。这个服务器作为客户端和远程服务器之间的代理，从客户端接收请求后转发到目标服务器，然后将响应返回给客户端。

**实践** ：在开发环境中，可以使用 Webpack Dev Server 的代理功能，配置 `proxy` 选项来实现请求转发。在生产环境，可以使用
Nginx 或 Node.js 等技术设置代理服务。

