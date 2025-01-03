![doutub_gif](https://i-blog.csdnimg.cn/blog_migrate/e9413fcd109f2f3d7297192eab0c0b2a.gif)

## 华为OD面试真题精选

🌟 强烈推荐：华为OD技术面试真题精选 🌟

大家好！今天我给大家推荐一份备受赞誉的华为OD技术面试精选题目。
所有题目均为华为od实际面试过程中出现的问题。这些面试题主要涉及到编程八股文、职业态度以及独特的个性特点。让我们一起深入了解这个精心整理的面试题集吧！😊
希望这些问题能够帮助你在面试中脱颖而出，展现出你的技术实力和独特魅力。加油！💪💼

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)

## 1\. 请详细解释一下CSS中的盒模型概念

CSS盒模型（Box
Model）是CSS布局的基础，它描述了元素在网页布局中所占的空间方式。每个HTML元素可以看作是一个盒子，由四个部分组成：内容（Content）、内边距（Padding）、边框（Border）和外边距（Margin）。

  1. 内容（Content）：这是元素的实际内容，如文本、图片等。

  2. 内边距（Padding）：内容周围的空白区域，内边距是透明的。

  3. 边框（Border）：围绕在内边距和内容外的边界，边框是可见的。

  4. 外边距（Margin）：边框外部的空白区域，用于分隔元素与其他元素，外边距是透明的。

盒模型的总宽度和总高度计算方式如下：

总宽度 = 左边距 + 左边框 + 左内边距 + 内容宽度 + 右内边距 + 右边框 + 右边距  
总高度 = 上边距 + 上边框 + 上内边距 + 内容高度 + 下内边距 + 下边框 + 下边距

需要注意的是，CSS有两种盒模型：标准模型和IE模型（又称怪异模型）。两者的主要区别在于宽度和高度的计算方式不同。在标准模型中，width和height指的是内容的宽度和高度；而在IE模型中，width和height包含了内容、内边距和边框的宽度和高度。可以通过box-
sizing属性来指定使用哪种盒模型，如box-sizing: content-box表示使用标准模型，box-sizing: border-
box表示使用IE模型。

## 2.请列举哪些CSS属性可以使元素脱离文档流

  1. 使用float属性：当元素被设置为float（如float: left或float: right）时，它会脱离文档流，并向左或向右浮动。其他文档流中的元素会围绕它流动。需要注意的是，浮动元素之后通常需要清除浮动，以防止布局混乱。

  2. 使用position属性：当元素的position属性被设置为absolute或fixed时，元素会脱离文档流。绝对定位元素的位置相对于最近的已定位祖先元素（如果没有则相对于初始包含块），固定定位元素的位置相对于视口。

  3. 使用display属性：当元素的display属性被设置为flex或grid时，其子元素会脱离文档流，而按照弹性布局或网格布局进行排列。

示例代码：

    
    
    /* 使用float属性 */
    .float-element {
        float: left;
    }
    
    /* 使用position属性 */
    .position-element {
        position: absolute;
        top: 0;
        left: 0;
    }
    
    /* 使用display属性 */
    .display-element {
        display: flex;
    }
    

## 3\. JavaScript 堆和栈在内存中的存储方式及其区别。

  1. 堆（Heap）：堆是用于存储对象（如对象、数组和函数）的内存区域。当你在JavaScript中创建一个对象时，JavaScript引擎会在堆中为这个对象分配内存。堆中的内存分配和回收是动态的，即对象可以在任何时候被创建和删除，内存的使用没有严格的规则。

  2. 栈（Stack）：栈是用于存储基本类型（如数字、字符串、布尔值）和指向堆中对象的引用的内存区域。与堆不同，栈有严格的规则，遵循LIFO（后进先出）原则，即最后进入栈的元素会首先被取出。此外，栈中的内存分配和回收是自动的，当函数调用结束时，函数的局部变量会自动从栈中移除。

总的来说，堆和栈的主要区别在于存储的数据类型和内存管理方式。堆主要用于存储复杂的数据类型（如对象），内存的分配和回收是动态的；而栈主要用于存储基本类型和引用，内存的分配和回收是自动的，遵循LIFO原则。

## 4.JavaScript中的原型和原型链是什么

  1. 原型（Prototype）：在JavaScript中，每个对象都有一个特殊的内部属性[[Prototype]]，通常被称为原型。这个原型本身也是一个对象，包含了可以被特定类型的所有实例共享的属性和方法。例如，所有的数组都共享Array.prototype中的方法，如push，pop等。

  2. 原型链（Prototype Chain）：当试图访问一个对象的属性时，JavaScript会首先在该对象本身的属性中查找。如果没有找到，那么JavaScript会继续在该对象的原型（即[[Prototype]]属性指向的对象）中查找，这个过程会一直持续到原型对象为null为止。这种由原型对象构成的链状结构就被称为原型链。

原型和原型链的关系：原型链是通过链接原型对象来实现的。每个对象的原型可以指向另一个对象，这样就形成了一个链状结构。当JavaScript引擎查找属性或方法时，它会沿着这个链状结构向上查找，直到找到相应的属性或方法，或者到达链条的末端。

这种原型和原型链的机制使得JavaScript中的对象可以共享代码，实现属性和方法的继承，同时也支持了JavaScript的动态性，使得我们可以在运行时添加或修改对象的属性和方法。

## 5\. JavaScript中的var、let和const关键字的区别，并给出它们各自的使用场景。

在JavaScript中，var、let和const都是用于声明变量的关键字，但它们在作用域、提升（hoisting）和重新赋值等方面有一些重要的区别。

  1. var：var声明的变量的作用域是它当前的执行上下文，即它被定义在函数内部时，作用域是整个函数；在函数外部定义时，作用域是全局的。var声明的变量会被提升，即它们会在编译阶段被移动到它们所在的作用域的顶部。var声明的变量可以被重新赋值和重新声明。

  2. let：let声明的变量的作用域是块级的，即它只在声明它的代码块（及任何包含该代码块的代码块）中有效。let声明的变量也会被提升，但是在变量声明之前的代码区域（通常被称为“暂时性死区”）中访问它们会导致错误。let声明的变量可以被重新赋值，但不能被重新声明。

  3. const：const声明的也是块级作用域的变量，和let类似。const声明的变量也会被提升，且在声明之前的代码区域中访问它们也会导致错误。不过，const声明的变量既不能被重新赋值，也不能被重新声明。

总的来说，var、let和const的主要区别在于它们的作用域、提升行为和是否可以被重新赋值或声明。在现代JavaScript开发中，推荐使用let和const，因为它们的块级作用域更符合大多数编程语言的作用域规则，而且可以避免一些由于var的提升行为和函数作用域导致的问题。

## 6\. JavaScript中的箭头函数和普通函数的主要区别，并给出它们各自的使用场景？

在JavaScript中，箭头函数和普通函数（也称为函数声明或函数表达式）在语法、this绑定、arguments对象等方面有一些重要的区别。

  1. 语法：箭头函数有更简洁的语法。例如，一个没有参数和函数体的普通函数可以写成`function() {}`，而一个箭头函数可以简写成`() => {}`。

  2. this绑定：在普通函数中，this的值在函数被调用时确定，取决于函数的调用方式。而在箭头函数中，this在函数定义时就被绑定，指向定义箭头函数时的上下文。这使得箭头函数在处理事件监听器或回调函数时非常有用，因为它们可以访问定义它们的上下文的this值。

  3. arguments对象：普通函数有自己的arguments对象，包含了函数被调用时传入的参数。而箭头函数没有自己的arguments对象，但它可以访问定义它的上下文的arguments对象。

  4. 构造函数：普通函数可以用作构造函数，可以使用new关键字创建新的对象实例。而箭头函数不能用作构造函数，如果尝试使用new关键字调用箭头函数，会抛出错误。

  5. 原型：由于普通函数可以用作构造函数，所以它们有自己的prototype属性。而箭头函数不可以用作构造函数，所以它们没有prototype属性。

总的来说，箭头函数和普通函数的主要区别在于它们的语法、this绑定、arguments对象、是否可以用作构造函数和是否有prototype属性。在需要使用简洁语法、固定的this绑定或访问外部的arguments对象时，箭头函数是一个很好的选择。而在需要使用构造函数、自己的arguments对象或prototype属性时，应该使用普通函数。

## 7\. 当我们有一个用户名输入框需要进行已存在性校验时，你会如何设计和实现这个功能？

实现用户名已存在性校验的功能，通常需要前端和后端的配合。

  1. 用户在前端的输入框中输入用户名后，前端代码会监听这个输入事件。

  2. 当输入完成后，前端代码会向后端发送一个异步请求，请求中包含了用户输入的用户名。

  3. 后端收到请求后，会在数据库中查找是否已经存在这个用户名。如果用户名已存在，后端会返回一个表示用户名已存在的响应；如果用户名不存在，后端会返回一个表示用户名可用的响应。

  4. 前端收到后端的响应后，会根据响应的内容更新页面。如果用户名已存在，前端可以在输入框下方显示一个错误消息，提示用户需要输入一个新的用户名。如果用户名可用，前端可以在输入框下方显示一个确认消息，告诉用户这个用户名可以使用。

这种方案的关键是异步请求和响应的处理。在JavaScript中，可以使用Fetch
API或者Axios等库来发送异步请求。在后端，具体的实现会依赖于你使用的技术栈，但大多数的后端框架都会提供处理HTTP请求和访问数据库的工具。

需要注意的是，这种方案可能会导致频繁的网络请求，特别是在用户输入用户名时。为了优化性能，可以使用防抖（debounce）技术，即只在用户停止输入一段时间后才发送请求。

## 8\. 你能详细描述一下在CSS中实现元素的垂直和水平居中有哪些方法吗？

  1. 使用margin: auto;：这是一种常见的方法，适用于块级元素，需要知道元素的宽度，并且父元素需要有足够的高度。例如：

    
    
    .center {
      width: 100px;
      margin: auto;
    }
    

  2. 使用flex布局：这是一种现代的布局方法，可以轻松实现元素的垂直和水平居中。例如：

    
    
    .center {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    

  3. 使用position和transform：这种方法适用于不知道元素尺寸的情况。例如：

    
    
    .center {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    

  4. 使用grid布局：这也是一种现代的布局方法，可以轻松实现元素的垂直和水平居中。例如：

    
    
    .center {
      display: grid;
      place-items: center;
    }
    

  5. 使用table-cell和vertical-align：这种方法适用于旧的浏览器，可以实现垂直居中。例如：

    
    
    .center {
      display: table-cell;
      vertical-align: middle;
    }
    

## 9\. 你能详细解释一下什么是XSS攻击和CSRF攻击吗？它们各自的攻击原理是什么，以及我们如何防范这两种攻击？

XSS（Cross-Site Scripting）和CSRF（Cross-Site Request Forgery）都是常见的网络攻击手段。

  1. XSS攻击：XSS攻击是指攻击者在网页中注入恶意脚本，当其他用户浏览这个网页时，注入的脚本会被执行，从而达到攻击的目的。XSS攻击通常用于窃取用户的cookie，进行身份冒充等恶意行为。防范XSS攻击的主要手段是对用户输入的数据进行严格的过滤或转义，确保插入到网页中的代码是安全的。

  2. CSRF攻击：CSRF攻击是指攻击者诱导用户去点击一个链接或者提交一个请求，这个链接或请求中包含了攻击者预设的、向其他网站发送的恶意请求。由于浏览器会自动带上用户对这个网站的cookie，所以如果用户在这个网站上有权限，那么这个恶意请求就会以用户的名义成功执行。防范CSRF攻击的主要手段是使用CSRF Token，或者进行SameSite Cookie设置，确保即使攻击者构造出恶意请求，也无法成功执行。

总的来说，防范XSS和CSRF攻击需要我们在编写代码时始终保持警惕，对所有的用户输入进行严格的检查和处理，对所有的请求进行严格的验证。

## 10\. 在前端开发中，移动端和PC端开发的主要区别是什么？。

  1. 屏幕尺寸和分辨率：移动设备的屏幕尺寸和分辨率通常都比PC小，这就需要我们在设计和布局时要考虑到这一点，确保网页在不同设备上都能正确显示。我们可以使用响应式设计，通过CSS媒体查询来根据设备的屏幕尺寸调整布局。

  2. 用户交互方式：PC端主要通过鼠标和键盘进行操作，而移动端主要通过触摸屏进行操作。这就意味着我们需要考虑到触摸事件，例如滑动、长按等，而这些在PC端是不需要的。

  3. 网络环境：移动设备通常使用的是蜂窝数据网络，而PC则通常使用的是有线网络。蜂窝数据网络的速度和稳定性通常都不如有线网络，所以在移动端开发时，我们需要更加注意网页的加载速度和数据的优化。

  4. 浏览器兼容性：移动端和PC端的浏览器种类和版本也有所不同，可能会存在一些兼容性问题。我们需要测试在不同浏览器和设备上的表现，确保网页能够正常工作。

  5. 性能优化：由于移动设备的硬件性能通常不如PC，所以在移动端开发时，我们需要更加注意性能优化，例如减少DOM操作，减少HTTP请求，使用CSS3动画等。

在设计和实现过程中，我们需要根据以上的差异来进行适当的调整和优化，以确保我们的网页在不同的设备上都能提供良好的用户体验。

#### 文章目录

  * 华为OD面试真题精选
  * 1\. 请详细解释一下CSS中的盒模型概念
  * 2.请列举哪些CSS属性可以使元素脱离文档流
  * 3\. JavaScript 堆和栈在内存中的存储方式及其区别。
  * 4.JavaScript中的原型和原型链是什么
  * 5\. JavaScript中的var、let和const关键字的区别，并给出它们各自的使用场景。
  * 6\. JavaScript中的箭头函数和普通函数的主要区别，并给出它们各自的使用场景？
  * 7\. 当我们有一个用户名输入框需要进行已存在性校验时，你会如何设计和实现这个功能？
  * 8\. 你能详细描述一下在CSS中实现元素的垂直和水平居中有哪些方法吗？
  * 9\. 你能详细解释一下什么是XSS攻击和CSRF攻击吗？它们各自的攻击原理是什么，以及我们如何防范这两种攻击？
  * 10\. 在前端开发中，移动端和PC端开发的主要区别是什么？。

