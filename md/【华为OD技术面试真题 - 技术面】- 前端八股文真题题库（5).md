## 华为OD面试真题精选

专栏：[华为OD面试真题精选](https://blog.csdn.net/banxia_frontend/category_12436481.html)  
目录:
[2024华为OD面试手撕代码真题目录以及八股文真题目录](https://blog.csdn.net/banxia_frontend/article/details/138131520)

#### 文章目录

  * 华为OD面试真题精选
  * 1\. Cookie、Storage、InnoDB的区别
  *     *       * 1\. **Cookie**
      * 2\. **Storage (localStorage 和 sessionStorage)**
      * 3\. **InnoDB**
      * 4\. 补充：*IndexedDB*
  * 2\. 前端开发涉及到的网络协议
  *     *       * 1\. **HTTP/HTTPS（超文本传输协议/安全超文本传输协议）**
      * 2\. **WebSocket**
      * 3\. **HTTP/2**
      * 4\. **DNS（域名系统）**
      * 5\. **TLS/SSL（传输层安全协议/安全套接层协议）**
      * 6\. **CDN（内容分发网络）**
  * 3\. 说说你知道的前端性能优化
  * 4\. 谈谈你知道的Dom修改
  *     *       * **DOM 操作的基本概念**
      * **常见的 DOM 修改方法**
      * **DOM 修改的性能影响**
      * **优化 DOM 操作的策略**
  * 5\. 浅拷贝和深拷贝
  * 6\. 对Set、Map两种数据结构的理解
  *     *       * **Set**
      *         * **Set 的特性与方法：**
        * **Set 的使用场景：**
      * **Map**
      *         * **Map 的特性与方法：**
        * **Map 的使用场景：**
  * 7\. 数据量很大，有什么优化查询方法，你在项目中使用了哪些优化方法

![封面](https://i-blog.csdnimg.cn/blog_migrate/044c13f12b7b05fa860f365d481b03ab.png)

## 1\. Cookie、Storage、InnoDB的区别

#### 1\. **Cookie**

  * **用途** ：用于在客户端存储少量数据，可以在不同页面之间共享，并且数据会在 HTTP 请求中自动发送到服务器。常用于会话管理、用户跟踪等。
  * **容量** ：通常每个 Cookie 大小限制为约 4KB。
  * **存储位置** ：客户端浏览器。
  * **生命周期** ：可以设置过期时间，默认为会话结束后失效。
  * **安全性** ：由于会在每次请求中发送到服务器，因此不适合存储敏感信息。可以通过 `HttpOnly` 和 `Secure` 标记增加安全性。
  * **访问方式** ：通过 JavaScript 的 `document.cookie` 接口进行读写，或在服务器端进行设置。

#### 2\. **Storage (localStorage 和 sessionStorage)**

  * **用途** ：用于在客户端存储较大数据，可以通过 JavaScript 进行本地数据存储和访问，不会自动发送到服务器。通常用于本地持久化用户数据。
  * **容量** ： 
    * `localStorage`：每个域名通常有 5MB 到 10MB 的存储空间。
    * `sessionStorage`：与 `localStorage` 类似，但数据仅在页面会话期间可用（页面关闭后数据即被清除）。
  * **存储位置** ：客户端浏览器。
  * **生命周期** ： 
    * `localStorage`：持久化存储，直到手动删除。
    * `sessionStorage`：仅在当前会话内有效，页面关闭后数据消失。
  * **安全性** ：仅在客户端存储，不会自动发送到服务器，但数据仍然可以被 JavaScript 访问，因此不适合存储高度敏感的信息。
  * **访问方式** ：通过 JavaScript 的 `localStorage` 或 `sessionStorage` 接口进行读写。

#### 3\. **InnoDB**

  * **用途** ：`InnoDB` 是 MySQL 数据库中的一种存储引擎，与前端开发直接关联较少。通常用于在服务器端的数据库中管理和存储数据，支持事务、外键等高级特性。适用于需要持久化、结构化存储的数据。
  * **容量** ：理论上容量仅受限于服务器的硬件资源。
  * **存储位置** ：服务器端数据库。
  * **生命周期** ：数据的生命周期由数据库的设计和操作决定，可以是永久存储。
  * **安全性** ：通过数据库权限控制和网络安全措施来保障数据的安全性，适合存储高度敏感的数据。
  * **访问方式** ：通过 SQL 查询和数据库连接进行访问。

#### 4\. 补充： _IndexedDB_

`IndexedDB` 是一个功能强大的浏览器数据库，适用于需要在客户端存储和检索大量数据的场景。它超越了简单的键值对存储机制，如
`localStorage` 和 `sessionStorage`，并提供了对结构化数据的高级支持。

  * **用途** ：

    * 适合用于需要在客户端存储大量数据的应用，如离线应用、PWA（渐进式Web应用）等。
    * 可以存储复杂的数据结构，包括对象、文件、Blob 等，远超出 `localStorage` 或 `sessionStorage` 所支持的简单键值对存储。
  * **特性** ：

    * **大容量** ：`IndexedDB` 的存储容量相对较大，通常可以存储数百 MB 甚至更多的数据。
    * **事务支持** ：`IndexedDB` 提供了对事务的支持，确保数据的完整性和一致性。
    * **索引** ：可以为数据创建索引，以提高查询效率。
    * **异步操作** ：所有操作都是异步的，以避免阻塞浏览器的主线程。
    * **结构化克隆算法** ：使用结构化克隆算法存储对象，因此可以保存复杂对象（包括循环引用的对象）。
  * **使用场景** ：

    * 离线应用：在用户断网时依然能够正常使用的应用。
    * 大量数据存储：需要在浏览器中存储和管理大量数据的场景，例如缓存文件、数据分析等。
  * **API** ：

    * 通过 JavaScript 提供的 API 进行交互，主要包括 `open`、`transaction`、`objectStore` 等方法。需要注意的是，由于其异步特性，通常会使用回调函数或 Promises 来处理操作的结果。
  * **安全性** ：`IndexedDB` 存储在浏览器的沙箱环境中，并且只能由同源脚本访问，因此安全性相对较高。

## 2\. 前端开发涉及到的网络协议

#### 1\. **HTTP/HTTPS（超文本传输协议/安全超文本传输协议）**

  * **HTTP** ：超文本传输协议，是前端与服务器之间进行通信的基础协议。HTTP 是无状态的，即每次请求都是独立的，不保留任何上下文信息。常见的 HTTP 方法包括 `GET`、`POST`、`PUT`、`DELETE`、`PATCH` 等。
  * **HTTPS** ：在 HTTP 基础上增加了 SSL/TLS 加密层，确保数据在传输过程中不会被窃取或篡改。HTTPS 是现代 Web 应用的标准，尤其在涉及用户隐私和敏感数据时尤为重要。

#### 2\. **WebSocket**

  * **WebSocket** ：一种全双工通信协议，允许客户端与服务器之间进行实时的双向通信。与 HTTP 不同，WebSocket 在初次握手后会保持连接开放，从而能够高效地进行数据交换，常用于实时聊天、在线游戏、实时更新等场景。

#### 3\. **HTTP/2**

  * **HTTP/2** ：是 HTTP 协议的升级版本，提供了多路复用、头部压缩、服务器推送等功能，旨在提高 Web 应用的性能。前端开发中，HTTP/2 带来的性能改进对于优化资源加载、提高用户体验非常重要。

#### 4\. **DNS（域名系统）**

  * **DNS** ：负责将人类可读的域名（如 `example.com`）解析为 IP 地址。前端开发中，了解 DNS 解析的过程有助于理解网络请求的延迟，并采取措施（如 DNS 预取）来优化页面加载速度。

#### 5\. **TLS/SSL（传输层安全协议/安全套接层协议）**

  * **TLS/SSL** ：用于加密 HTTP 数据传输，确保数据的保密性和完整性。TLS 是 SSL 的升级版本，现已成为 HTTPS 的标准加密协议。

#### 6\. **CDN（内容分发网络）**

  * **CDN** 不是一个独立的协议，但它涉及多个网络协议的使用，包括 HTTP/HTTPS 和 DNS。CDN 通过将内容缓存到全球各地的服务器上，加速了用户访问静态资源的速度，是现代前端性能优化的关键技术之一。

## 3\. 说说你知道的前端性能优化

  1. **资源优化**

     * **图片优化** ：使用现代格式如 WebP 替代传统格式，压缩图片大小，减少带宽占用。还可以根据屏幕尺寸提供不同分辨率的图片（响应式图片）。
     * **懒加载** ：对于非关键资源（如图片、视频等），可以使用懒加载技术，即用户滚动到相关内容时才加载资源，以减少页面初次加载时间。
     * **合并与压缩资源** ：将多个 CSS 和 JavaScript 文件合并，减少 HTTP 请求；通过压缩工具（如 Uglify、Terser、CSSNano）减少文件体积。
  2. **减少 HTTP 请求**

     * **使用雪碧图（CSS Sprites）** ：将多个小图标合并到一张图片中，减少 HTTP 请求。
     * **内联关键 CSS** ：将渲染关键路径中的小部分 CSS 直接嵌入到 HTML 文件中，减少 CSS 文件的请求数并提高首屏渲染速度。
  3. **代码分割**

     * 使用 Webpack 等构建工具进行代码分割，将应用拆分成更小的 JavaScript 包。按需加载这些包，以减少初始加载时间。这对大型单页应用（SPA）尤为重要。
  4. **缓存**

     * **HTTP 缓存** ：设置合理的缓存策略，如 `Cache-Control` 和 `ETag`，使得浏览器能够缓存静态资源，减少重复请求。
     * **服务端渲染（SSR）缓存** ：在使用 SSR 时，可以缓存生成的 HTML 页面，减少服务器计算压力，提升响应速度。
  5. **使用 CDN**

     * 将静态资源（如图片、CSS、JS 文件）分发到全球各地的 CDN 节点，用户能够从最近的节点获取资源，从而降低加载时间。
  6. **减少渲染阻塞**

     * **异步加载 JavaScript** ：使用 `async` 或 `defer` 属性，避免 JavaScript 阻塞页面渲染。
     * **最小化 CSS 阻塞** ：将关键 CSS 直接嵌入到页面中，其他 CSS 文件则可以延迟加载，以避免页面渲染被 CSS 阻塞。
  7. **优先加载关键内容**

     * **首屏优化** ：确保首屏内容的优先加载，使得用户在最短时间内看到页面的主要内容。可以通过减少不必要的外部依赖、使用骨架屏等手段来优化首屏体验。
     * **预加载与预取** ：使用 `preload` 和 `prefetch` 标签提前加载即将使用的资源，减少后续的加载等待时间。
  8. **减少 JavaScript 执行时间**

     * **去除未使用的代码** ：通过工具（如 Webpack 的 Tree Shaking）去除未使用的代码，减少 JavaScript 文件的体积。
     * **减少重绘与重排** ：在 DOM 操作时，应尽量减少对页面的频繁修改，避免导致页面重绘或重排，从而提升性能。
  9. **性能监控**

     * 使用 Lighthouse、PageSpeed Insights 等工具监控页面性能，识别性能瓶颈，定期优化。通过分析 `Time to First Byte`（TTFB）、`First Contentful Paint`（FCP）、`Largest Contentful Paint`（LCP）等指标，逐步提升用户体验。

## 4\. 谈谈你知道的Dom修改

#### **DOM 操作的基本概念**

DOM（文档对象模型）是浏览器呈现 HTML 文档的方式，允许开发者通过 JavaScript 动态修改页面的内容、结构和样式。DOM
操作是昂贵的，因为它可能触发浏览器的重排（reflow）和重绘（repaint），这会影响页面的响应速度和用户体验。

#### **常见的 DOM 修改方法**

  1. **直接修改** ：通过 JavaScript 直接添加、删除或更改 DOM 节点。
    
        let element = document.getElementById('myElement');
    element.textContent = 'New Content'; // 修改内容
    element.style.color = 'red'; // 修改样式
    

  2. **批量更新** ：通过批量修改 DOM 来减少重排次数。
    
        let fragment = document.createDocumentFragment();
    for (let i = 0; i < 1000; i++) {
        let newElement = document.createElement('div');
        newElement.textContent = `Item ${i}`;
        fragment.appendChild(newElement);
    }
    document.getElementById('container').appendChild(fragment);
    

  3. **使用虚拟 DOM** ：在 React、Vue 等框架中，虚拟 DOM 通过比较前后的差异（diffing）来减少直接操作真实 DOM，从而提高性能。

#### **DOM 修改的性能影响**

  1. **重排（Reflow）** ：

     * 当页面布局或几何属性（如大小、位置）发生变化时，浏览器会重新计算元素的位置和大小，称为重排。
     * 重排是性能消耗最大的操作之一，尤其是在页面上有大量元素时。因此，尽量减少频繁的重排是优化性能的关键。
  2. **重绘（Repaint）** ：

     * 当元素的外观发生变化（如颜色、背景），但没有影响到布局时，浏览器会触发重绘。虽然重绘的开销小于重排，但频繁的重绘依然会影响性能。

#### **优化 DOM 操作的策略**

  1. **批量 DOM 操作** ：

     * 使用 `DocumentFragment` 或离线节点（将节点从文档中移除进行操作）来批量处理 DOM 变化，减少重排次数。
     * 例如，在向列表中添加大量元素时，先将这些元素添加到 `DocumentFragment`，再一次性将其添加到 DOM 中。
  2. **避免强制同步布局** ：

     * 在读取元素的几何属性（如 `offsetWidth`、`offsetHeight`、`getBoundingClientRect()`）后立即修改 DOM，会导致浏览器为了获取最新的几何信息而强制重排。这种情况称为强制同步布局，应该尽量避免。
     * 可以将读取和写入操作分开，确保在需要获取几何信息时，DOM 状态已经稳定。
  3. **使用`requestAnimationFrame`**：

     * 当需要频繁更新 UI 时（如动画效果），可以使用 `requestAnimationFrame` 来确保 DOM 操作与屏幕刷新同步，从而避免卡顿。
    
        function updateElement() {
        element.style.left = (parseInt(element.style.left) + 1) + 'px';
        requestAnimationFrame(updateElement);
    }
    requestAnimationFrame(updateElement);
    

  4. **虚拟 DOM 与 Diff 算法** ：

     * 在使用 React、Vue 等框架时，利用虚拟 DOM 和 Diff 算法，可以大幅减少不必要的 DOM 操作。虚拟 DOM 只会更新必要的部分，避免了直接操作真实 DOM 带来的性能问题。
  5. **减少 DOM 大小与深度** ：

     * DOM 树越大，浏览器处理重排和重绘的开销就越大。尽量减少不必要的 DOM 节点和层级，可以有效提升页面性能。

## 5\. 浅拷贝和深拷贝

常见题目：秒了

## 6\. 对Set、Map两种数据结构的理解

在前端开发中，`Set` 和 `Map` 是 ES6 引入的两种重要数据结构。

#### **Set**

`Set` 是一种集合数据结构，用于存储唯一值。与数组不同的是，`Set` 中的值不能重复。`Set` 的值可以是任何类型，包括原始值和对象引用。

##### **Set 的特性与方法：**

  1. **唯一性** ：`Set` 自动去重，不允许重复的值。
  2. **类型灵活** ：可以存储任何类型的值，包括基本类型和引用类型。
  3. **顺序性** ：`Set` 会按照插入顺序保留元素顺序，因此可以用 `for...of` 或 `forEach` 进行遍历。

常用方法：

  * `add(value)`：向 `Set` 添加一个值，如果值已经存在则不会添加。
  * `has(value)`：检查 `Set` 中是否存在某个值。
  * `delete(value)`：删除 `Set` 中的某个值。
  * `clear()`：清空 `Set` 中的所有值。
  * `size`：返回 `Set` 中元素的数量。

    
    
    let mySet = new Set();
    mySet.add(1);
    mySet.add(5);
    mySet.add(5); // 由于重复，这个值不会被添加
    
    console.log(mySet.has(1)); // true
    console.log(mySet.size); // 2
    mySet.delete(1);
    console.log(mySet.has(1)); // false
    

##### **Set 的使用场景：**

  * **数组去重** ：快速去除数组中的重复元素。
  * **集合操作** ：如交集、并集、差集等运算，这些在数学上常见的集合操作可以轻松用 `Set` 实现。
  * **唯一值存储** ：需要存储一组唯一值时，`Set` 是首选。

    
    
    // 数组去重
    let arr = [1, 2, 2, 3, 4, 4];
    let uniqueArr = [...new Set(arr)];
    

#### **Map**

`Map` 是一种键值对的数据结构，与对象类似，但 `Map` 的键可以是任何类型（包括对象）。`Map`
保留了键值对的插入顺序，且相较于普通对象，`Map` 在处理大量键值对时的性能通常更好。

##### **Map 的特性与方法：**

  1. **键的类型灵活** ：`Map` 的键可以是任何类型，而对象的键只能是字符串或符号。
  2. **顺序性** ：`Map` 会按照插入顺序保留键值对的顺序。
  3. **性能优化** ：由于 `Map` 专门为存储键值对而设计，相对于对象来说，在存储和查找大量键值对时性能更好。

常用方法：

  * `set(key, value)`：设置键值对，如果键已存在则更新其值。
  * `get(key)`：获取键对应的值，如果键不存在则返回 `undefined`。
  * `has(key)`：检查 `Map` 中是否存在某个键。
  * `delete(key)`：删除 `Map` 中的某个键值对。
  * `clear()`：清空 `Map` 中的所有键值对。
  * `size`：返回 `Map` 中键值对的数量。

    
    
    let myMap = new Map();
    myMap.set('key1', 'value1');
    myMap.set({}, 'value2');
    
    console.log(myMap.get('key1')); // 'value1'
    console.log(myMap.size); // 2
    myMap.delete('key1');
    console.log(myMap.has('key1')); // false
    

##### **Map 的使用场景：**

  * **数据映射** ：需要用复杂类型（如对象、函数）作为键时，`Map` 是最佳选择。
  * **频繁增删查操作** ：由于 `Map` 在处理大量键值对时性能更优，适用于频繁进行增删查操作的场景。
  * **按顺序存储数据** ：在需要保留插入顺序的键值对存储场景中使用 `Map`。

    
    
    // 使用 Map 来存储 DOM 节点的状态
    let nodeStateMap = new Map();
    let node = document.getElementById('myNode');
    nodeStateMap.set(node, { clicked: true });
    

## 7\. 数据量很大，有什么优化查询方法，你在项目中使用了哪些优化方法

  1. **惰性加载 (Lazy Loading) 和分页 (Pagination)：**

     * **惰性加载** ：在数据量非常大的情况下，一次性加载所有数据会消耗大量资源。可以考虑使用惰性加载技术，只在用户需要时加载数据。
     * **分页** ：将数据按页加载，用户只会看到当前页的数据，减少了前端需要处理的数据量，提高了响应速度。
  2. **本地缓存 (Local Caching)：**

     * 在浏览器中使用 `LocalStorage`、`SessionStorage` 或者 `IndexedDB` 来缓存经常访问的数据，避免频繁的网络请求，减少服务器的负载，并加快数据读取速度。
     * **Memoization** ：对函数返回的结果进行缓存，避免对相同输入的重复计算，从而加快数据查询速度。
  3. **Web Workers：**

     * 使用 Web Workers 将数据处理工作移到主线程之外，避免大数据处理时阻塞 UI 渲染，提高页面的响应速度和用户体验。
  4. **虚拟滚动 (Virtual Scrolling)：**

     * 当展示大量数据时，使用虚拟滚动技术，只渲染用户当前视口中的数据，其他数据仅在用户滚动时才动态加载。这样可以显著减少 DOM 元素的数量，提高页面性能。
  5. **分片处理 (Chunking)：**

     * 如果必须一次处理大量数据，可以将其分成小块，并在多个事件循环中处理。这样可以避免阻塞主线程，保证页面的响应性。

