+++
title = '自研移动端安全产品-指掌易-大连-面试经验'
date = 2024-12-10T14:58:28+08:00
draft = false
+++

# 0. 结果
没啥戏

# 1. 面试

## 1. **技术栈和项目经验**：
### 你在之前的项目中使用了哪些技术栈？
### 描述一下你最近做的AI答题应用系统。

## 2. **AI模型选择**：
### 在选型过程中是如何选择用哪一个AI模型（如通义AI、OpenAI等）？

## 3. **Spring Boot配置与操作**：
### 如果想将Spring Boot默认的嵌入式服务器换成其他的应该怎么做？
### 如何在Spring Boot启动时执行特定的代码逻辑？

## 4. **异常处理**：
### 你是如何实现全局异常处理的？

## 5. **加密机制**：
### 对controller返回值进行加密的方法有哪些？

## 6. **事务管理**：
### @Transactional注解在什么情况下会失效？
- 方法不是 public 的：@Transactional 只能应用于 public 方法。
- 方法被 final 修饰：Spring AOP 代理无法代理 final 方法。
- 类被 final 修饰：Spring AOP 代理无法代理 final 类。
- 方法在同一个类中被调用：如果在同一个类中调用带有 @Transactional 注解的方法，事务不会生效，因为 Spring AOP 代理不会拦截内部方法调用。
- 事务管理器配置错误：如果事务管理器配置不正确，事务也不会生效。
- 异常类型不匹配：默认情况下，只有未检查异常（继承自 RuntimeException）才会触发事务回滚。如果抛出的是检查异常（继承自 Exception），事务不会回滚，除非在 @Transactional 注解中明确指定。

## 7. **MySQL索引**：
### MySQL的索引在什么情况下会失效？
- 使用了函数：在索引列上使用了函数或表达式，例如 WHERE UPPER(column) = 'value'。
- 类型不匹配：查询条件中的数据类型与索引列的数据类型不一致。
- 使用了通配符：在LIKE查询中，如果通配符在前面，例如 LIKE '%value'。
- 隐式转换：查询中导致索引列进行隐式类型转换，例如字符串和数字比较。
- OR条件：在WHERE子句中使用OR条件且OR两边的列没有同时使用索引。
- 不等于操作：使用!=或<>操作符。
- IS NULL或IS NOT NULL：在索引列上使用IS NULL或IS NOT NULL。
- 前缀索引：在前缀索引中，查询条件未使用前缀的全部长度。
- 范围查询：在复合索引中，使用范围查询（如BETWEEN、<、>）后面的列索引失效。
- 数据量小：表的数据量太小，MySQL可能会选择全表扫描而不是使用索引。

## 8. **Linux服务器操作**：
### 你平时对Linux服务器有具体的操作吗？比如部署程序后CPU占用率特别高，如何排查这个问题?
要排查部署程序后CPU占用率特别高的问题，可以按照以下步骤进行
- 监控和日志：首先查看系统监控工具（如Windows的任务管理器或Linux的top命令）和应用程序日志，确定哪个进程占用了大量的CPU资源。
- 分析代码：检查代码中是否有死循环、递归调用、密集计算等可能导致高CPU占用的部分。
- 性能分析工具：使用性能分析工具（如Visual Studio Profiler、Perf、JProfiler等）对应用程序进行性能分析，找出CPU热点。
- 优化代码：根据性能分析的结果，优化代码，减少不必要的计算和资源占用。
- 检查依赖：检查第三方库或依赖项是否存在性能问题，尝试更新或替换它们。
- 配置调整：调整应用程序的配置参数，如线程池大小、缓存设置等，以优化性能。
- 硬件资源：确保服务器硬件资源（如CPU、内存）充足，必要时考虑升级硬件。
通过以上步骤，可以逐步排查和解决CPU占用率高的问题。

## 9. **Java内存分析**：
### Java程序内存占用高时，如何dump一个内存文件出来？
要在Java程序内存占用高时dump一个内存文件，可以使用以下几种方法：

1. **使用jmap工具**：
   jmap是JDK自带的工具，可以用来生成Java堆的转储文件。命令如下：
   ```sh
   jmap -dump:live,format=b,file=heapdump.hprof <pid>
   ```
   其中，`<pid>`是Java进程的ID，可以通过`jps`命令获取。

2. **使用jcmd工具**：
   jcmd也是JDK自带的工具，可以用来生成Java堆的转储文件。命令如下：
   ```sh
   jcmd <pid> GC.heap_dump heapdump.hprof
   ```
   其中，`<pid>`是Java进程的ID。

3. **使用VisualVM**：
   VisualVM是一个可视化的工具，可以用来监控和分析Java应用程序的性能。可以通过以下步骤生成堆转储文件：
   - 打开VisualVM并连接到目标Java进程。
   - 在“监视”选项卡中，点击“堆转储”按钮。

4. **在代码中触发堆转储**：
   可以在Java代码中使用`com.sun.management.HotSpotDiagnosticMXBean`来生成堆转储文件。示例如下：
   ```java
   import com.sun.management.HotSpotDiagnosticMXBean;
   import java.lang.management.ManagementFactory;

   public class HeapDump {
       public static void dumpHeap(String filePath, boolean live) throws Exception {
           HotSpotDiagnosticMXBean mxBean = ManagementFactory.getPlatformMXBean(HotSpotDiagnosticMXBean.class);
           mxBean.dumpHeap(filePath, live);
       }

       public static void main(String[] args) throws Exception {
           dumpHeap("heapdump.hprof", true);
       }
   }
   ```

通过以上方法，可以在Java程序内存占用高时生成堆转储文件，以便进行进一步的分析。

## 10. **Redis持久化和哨兵模式**：
### Redis的持久化方式有哪些？
- RDB（Redis Database）：将数据集的快照在指定的时间间隔保存到磁盘上。适合做数据备份和灾难恢复。
- AOF（Append Only File）：通过记录每个写操作来实现持久化。可以更频繁地保存数据，提供更高的数据安全性。
### 介绍一下Redis的哨兵模式
Redis的哨兵模式（Sentinel）是一种用于管理Redis集群的高可用性解决方案。它的主要功能包括：

1. **监控（Monitoring）**：哨兵会持续检查主服务器和从服务器是否正常工作。
2. **通知（Notification）**：当被监控的Redis服务器出现问题时，哨兵会通过API向系统管理员或其他应用程序发送通知。
3. **自动故障转移（Automatic Failover）**：当主服务器出现故障时，哨兵会自动将一个从服务器提升为新的主服务器，并将其他从服务器重新配置为复制新的主服务器。
4. **配置提供者（Configuration Provider）**：客户端可以连接到哨兵来获取当前Redis集群的主服务器地址。

### 哨兵模式好处
- **高可用性**：通过自动故障转移，确保Redis服务的高可用性。
- **监控和通知**：实时监控Redis实例的状态，并在出现问题时及时通知。
- **自动化管理**：减少了人工干预，提升了系统的可靠性和稳定性。
- **扩展性**：可以轻松地添加更多的哨兵实例来提高系统的容错能力。

哨兵模式使得Redis在生产环境中更加可靠和易于管理。

### 主观下线和客观下线的概念是什么？
在 Redis 集群中，主观下线和客观下线是两种不同的节点故障检测机制：

1. **主观下线（Subjective Down, SDOWN）**：
   - 当一个节点认为另一个节点不可用时，就会将其标记为主观下线。
   - 这是一个单个节点的判断，可能是由于网络分区、节点故障等原因导致的。
   - 主观下线的判断是由节点自身的检测机制（如心跳检测）决定的。

2. **客观下线（Objective Down, ODOWN）**：
   - 当集群中多数节点（通常是超过半数）都认为某个节点不可用时，该节点会被标记为客观下线。
   - 客观下线是通过集群中的节点之间相互通信和投票机制决定的。
   - 一旦节点被标记为客观下线，集群会进行故障转移（failover），将该节点的主节点角色转移到其他从节点上。

这两种机制共同作用，确保 Redis 集群能够在节点故障时快速响应并进行相应的处理。
## 11. **消息队列MQ**：
### 使用的消息队列工作模式是什么？
消息队列的工作模式有多种，常见的包括以下几种：

1. **点对点模式（P2P）**：消息从一个生产者发送到一个消费者。每条消息只能被一个消费者消费。

2. **发布/订阅模式（Pub/Sub）**：消息从一个生产者发送到多个消费者。每条消息可以被多个消费者消费。

3. **工作队列模式（Work Queue）**：消息从一个生产者发送到多个消费者，但每条消息只能被一个消费者消费。常用于任务分发。

4. **广播模式（Fanout）**：消息从一个生产者发送到所有绑定到该队列的消费者。每条消息会被所有消费者消费。

5. **主题模式（Topic）**：消息根据主题发送到不同的消费者。消费者可以订阅感兴趣的主题，只有匹配的消息才会被消费。

不同的消息队列系统（如RabbitMQ、Kafka、ActiveMQ等）可能会有不同的实现和特性。
### 如何防止消息丢失？(已背过)
### 如果MQ挂了但消息还未被消费，怎么办？
如果消息队列（MQ）崩溃了但消息还未被消费，可以采取以下措施来处理这种情况：

1. **消息持久化**：确保消息在发送到队列时被持久化到磁盘，这样即使MQ崩溃，重启后也能恢复未消费的消息。例如，RabbitMQ可以使用持久化队列和持久化消息来实现这一点。

2. **消息确认机制**：使用消息确认机制（Acknowledgment），确保只有在消费者确认收到并处理了消息后，消息才会从队列中删除。如果MQ崩溃，未确认的消息会在重启后重新投递给消费者。

3. **高可用性配置**：配置MQ的高可用性（HA），例如使用集群或镜像队列，确保即使一个节点崩溃，其他节点仍能继续提供服务。

4. **死信队列（DLQ）**：配置死信队列，将无法处理或多次投递失败的消息转移到死信队列中，以便后续分析和处理。

5. **监控和报警**：设置监控和报警机制，及时发现MQ的异常情况，并快速响应和处理。

以下是一个简单的RabbitMQ配置示例，展示了如何启用消息持久化和确认机制：

```java
import com.rabbitmq.client.*;

public class MQExample {
    private final static String QUEUE_NAME = "exampleQueue";

    public static void main(String[] argv) throws Exception {
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        try (Connection connection = factory.newConnection();
             Channel channel = connection.createChannel()) {
            // 声明持久化队列
            boolean durable = true;
            channel.queueDeclare(QUEUE_NAME, durable, false, false, null);

            String message = "Hello World!";
            // 发送持久化消息
            channel.basicPublish("", QUEUE_NAME, MessageProperties.PERSISTENT_TEXT_PLAIN, message.getBytes());
            System.out.println(" [x] Sent '" + message + "'");

            // 消费者
            DeliverCallback deliverCallback = (consumerTag, delivery) -> {
                String receivedMessage = new String(delivery.getBody(), "UTF-8");
                System.out.println(" [x] Received '" + receivedMessage + "'");
                // 确认消息
                channel.basicAck(delivery.getEnvelope().getDeliveryTag(), false);
            };
            boolean autoAck = false; // 关闭自动确认
            channel.basicConsume(QUEUE_NAME, autoAck, deliverCallback, consumerTag -> { });
        }
    }
}
```

通过上述配置，即使RabbitMQ崩溃，未被确认的消息也会在重启后重新投递给消费者。

## 12. **分布式锁**：
### 分布式锁的自动续期是怎么做的？
好的，以下是使用Redisson实现分布式锁自动续期的示例代码：

```java
import org.redisson.Redisson;
import org.redisson.api.RLock;
import org.redisson.api.RedissonClient;
import org.redisson.config.Config;

import java.util.concurrent.TimeUnit;

public class DistributedLockExample {

    private static RedissonClient redissonClient;

    public static void main(String[] args) {
        // 配置Redisson
        Config config = new Config();
        config.useSingleServer().setAddress("redis://127.0.0.1:6379");
        redissonClient = Redisson.create(config);

        // 获取锁
        RLock lock = redissonClient.getLock("myLock");

        try {
            // 尝试获取锁，等待时间为100毫秒，锁过期时间为10秒
            if (lock.tryLock(100, 10, TimeUnit.SECONDS)) {
                try {
                    // 执行需要加锁的任务
                    System.out.println("Lock acquired, executing task...");
                    Thread.sleep(15000); // 模拟任务执行时间
                } finally {
                    lock.unlock();
                    System.out.println("Lock released.");
                }
            } else {
                System.out.println("Failed to acquire lock.");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            redissonClient.shutdown();
        }
    }
}
```

在这个示例中，`Redisson` 提供了自动续期的功能，当你获取锁时，Redisson会自动在后台线程中续期锁的过期时间，直到显式释放锁。这样可以确保锁在任务执行期间不会过期。

### 悲观锁和乐观锁的区别，并举例说明Java中的用法。
悲观锁和乐观锁是两种并发控制策略，它们的主要区别在于对待并发冲突的态度不同。

1. **悲观锁**：
   - **态度**：假设会发生并发冲突，因此在操作数据之前先加锁，以确保只有一个线程能够访问数据。
   - **实现**：在Java中，悲观锁通常通过`synchronized`关键字或`ReentrantLock`来实现。
   - **示例**：
     ```java
     public class PessimisticLockExample {
         private final ReentrantLock lock = new ReentrantLock();

         public void performTask() {
             lock.lock();
             try {
                 // 需要同步的代码
             } finally {
                 lock.unlock();
             }
         }
     }
     ```

2. **乐观锁**：
   - **态度**：假设不会发生并发冲突，因此不加锁，而是在提交操作时检查是否有冲突，如果有则重试。
   - **实现**：在Java中，乐观锁通常通过`java.util.concurrent.atomic`包中的原子变量（如`AtomicInteger`）或版本号机制来实现。
   - **示例**：
     ```java
     import java.util.concurrent.atomic.AtomicInteger;

     public class OptimisticLockExample {
         private final AtomicInteger value = new AtomicInteger(0);

         public void performTask() {
             int oldValue, newValue;
             do {
                 oldValue = value.get();
                 newValue = oldValue + 1;
             } while (!value.compareAndSet(oldValue, newValue));
         }
     }
     ```

总结：
- 悲观锁适用于写操作多、冲突概率高的场景。
- 乐观锁适用于读操作多、冲突概率低的场景。

## 13. **安全性考虑**：
### 提供对外接口时从安全性的角度考虑了哪些方面？
- 单一认证机制（肌肉记忆，因为经常做，所以在说的时候容易被忽视）
- 敏感信息加密
- 线程安全
- etc.

## 14. **性能优化与故障排查**：
### 当页面访问变慢时，你会从哪些方面去排查？
- 慢SQL
- 若涉及API，看是不是API的问题，要不要加超时机制
- 文件上传

## 15. **自主提问**：
### 公司主要用到的技术栈是什么？（Java, SpringBoot, Netty, etc.）
### 入职后可能会做哪些类型的工作？(开发)
### 关于产品的愿景和发展方向是怎样的？（官网）