+++
title = '易宝软件-外派达摩院AIGC项目组-面试（只有一次/回忆版本）'
date = 2024-11-28T14:15:13+08:00
draft = false
+++

# 0. 面试结果
凉凉，差点以为能过，面试官当时对我印象不错，意难平，决定分享

# 1. 自我介绍(1min)
面试解析：[普通人面试指南2024版](https://www.bilibili.com/video/BV1Yx4y1p7fd/?spm_id_from=..search-card.all.click)

# 2. 项目相关描述(15min)
提问点来自简历一部分内容，基本上都是在聊简历有关话题

印象最深的就是为何不使用WebSocket，而是使用SSE？
> 熟悉了SSE技术后，对比上述前后端实时通讯方案。
1）主动轮询其实是一种伪实时，比如每3 秒轮询请求一次，结果后端在 0.1秒就返回了数据，还
要再等 2.9 秒，存在延迟。
2）WebSocket 和 SSE虽然都能实现服务端推送，但Websocket 会更复杂些，且是二进制协议，调
试不方便。AI对话只需要服务器单向推送即可，不需要使用双向通信，所以选择文本格式的SSE。

项目中，鱼皮的AI问答系统，我直接给包装成了公司项目，反正一个隐私问题，不允许泄密就可以糊弄过去，反正以前我司做过类似项目，各类型都做过，大到给某央企保险公司做，小到大湾区某高校做，正好高校有个AI项目，多一个又何妨?

说句实话，我司的项目还是比较垃圾，学不到啥东西，做的几乎是CURD和工具类边角料，特别核心的也没接触，所有又学了点鱼皮的项目开始补充自己简历

# 3. 代码部分(30min)
~~手撕定长缓存，符合LRU，且确保是线程安全的，我就不展示代码，讲讲思路（不对的地方我可以改）（要求用伪代码，怎么写都行，最好按照你擅长的语言来写）
首先，先定义一个带有时间戳的value类
其次，定义这个缓存（我用Map模拟的），这两个成员变量
    一个Map<String, Value>缓存
    还有个限制容量
最后开始完善写法，有两点注意事项
 记得在读取的时候要更新时间，可以把更新时间这部分开另一个线程异步上锁
然后在写的时候记得上锁，这部分才是体现LRU算法的部分~~
上面全是胡说八道，瞎鸡巴想的，我这里给出参考答案
> LRU缓存: https://www.mianshiya.com/question/1824426914736001026?shareCode=l35fjd
# 4. 项目外问题(3min)
- Spring的拦截器和过滤器有啥区别（这个一时没答上来）
- Spring注入Bean的一些方法（举例说明的）
- QPS和TPS定义（瞎j8答）
- 瞎聊
# 5. 你还有什么问题(2min)
当时和面试官吐槽了一个问题，我以为达摩院的AI和通义家的AI是一套体系，我还说，你们的SDK封装挺难用的（叠个甲，我可不是这么说的，我只是表述这个意思），结果得到的就是它们是两家体系，555