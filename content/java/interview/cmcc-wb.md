+++
title = '移动外派-杭州'
date = 2024-12-10T11:26:45+08:00
draft = false
+++
# 0. 结论
疑似刷KPI，因为我和HR核实，大约面试就20分钟，不过线上面试，可以拿来练手

# 1. 面试题（20min+）
- 自我介绍
- 项目介绍
- Controller 与 RestController的区别（一个是单独注解，另一个是合并注解，后者是ResponseBody与Controller的合并）
- 问我如何对SQL调优
- 问我如何解决Redis穿透的问题，缓存搭建的问题
- 重复性的恶意请求，如果这个缓存就是不存在，且数据库查不到，如何解决？（没答上来，做个参考）
    - 请求速率限制：使用速率限制（Rate Limiting）来限制每个IP地址在一定时间内的请求次数。可以使用Nginx、API Gateway等工具来实现。
    - 验证码：在关键操作或频繁请求时，要求用户输入验证码，以防止自动化的
    - IP黑名单：将频繁发送恶意请求的IP地址加入黑名单，阻止其访问。
    - 缓存空结果：对于不存在的数据，可以将空结果缓存一段时间，防止短时间内重复查询数据库。
    - 请求签名：对请求进行签名验证，确保请求的合法性，防止伪造请求。
    - 监控和报警：设置监控和报警机制，及时发现和处理异常请求。
- 策略模式
- 配置Gateway的方法：yaml，必要三个条件：服务名称、端口号和api前缀
- 已知如果需要动态配置，除了环境变量手段以外，如何用Nacos实现这个过程？
    - 参考1：[Nacos自定义环境变量](https://nacos.io/docs/v3.0/plugin/custom-environment-plugin/)
    - 参考2：[Nacos 配置统一管理、热部署、多环境配置共享](https://blog.csdn.net/CYK_byte/article/details/131445399?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EOPENSEARCH%7EPaidSort-1-131445399-blog-120451801.235%5Ev43%5Epc_blog_bottom_relevance_base4&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EOPENSEARCH%7EPaidSort-1-131445399-blog-120451801.235%5Ev43%5Epc_blog_bottom_relevance_base4&utm_relevant_index=1)