+++
title = '兴业数金-外包-福州'
date = 2024-12-11T10:40:25+08:00
draft = false
+++
{{< katex >}}

# 笔试题（只记录我没答上来的题目）
## 1. 外语类
### 外语完型
- 全是蒙的，几乎一个都没答上来
## 2. 算法
### 给定二叉树的一个后序和中序遍历结果，确定前序遍历结果
要确定二叉树的前序遍历结果，可以按照以下步骤进行：

1. **后序遍历的最后一个节点是根节点**：从后序遍历结果中找到最后一个节点，这个节点就是二叉树的根节点。
2. **在中序遍历中找到根节点的位置**：在中序遍历结果中找到这个根节点的位置，这样可以将中序遍历结果分成左子树和右子树两部分。
3. **递归构建左子树和右子树**：
   - 对于左子树，使用中序遍历结果的左部分和后序遍历结果的前部分（去掉最后一个节点）。
   - 对于右子树，使用中序遍历结果的右部分和后序遍历结果的中间部分（去掉最后一个节点）。
4. **组合前序遍历结果**：根节点 + 左子树的前序遍历结果 + 右子树的前序遍历结果。

### 给定一个满二叉树，求深度为n的二叉树叶节点有多少个？
对于一个深度为n的满二叉树，其叶节点的数量为 \\(2^{(n-1)}\\)。

这是因为满二叉树的每一层节点数是前一层节点数的两倍，而叶节点位于最后一层。

## 3. 数学题
### 排列组合题
这他妈都高中的知识，高考完早扔了

题目描述：

已知：有ABCDEFG七个元素

1. 希望A一直在B的左侧（两个元素可以不挨着），有几种排列方式？
1. 希望A一直在B的左侧（两个元素必须紧挨），有几种排列方式？

对于这两个问题，我们可以用组合数学的方法来解决。

1. 当A必须在B的左侧但两者不必紧挨着时：

我们有7个不同的元素，所以如果没有其他限制条件，这7个元素可以以7!（7的阶乘）种方式排列。但是这里有一个限制条件：A必须在B的左侧。对于A和B来说，它们只有两种相对位置——要么A在B的左边，要么B在A的左边。由于这两种情况是等可能的，并且只有一种符合我们的要求，所以我们只需要计算出所有排列的一半即可得到答案。因此，总的排列方式为7! / 2。

\\( \text{总排列数} = \frac{7!}{2} = \frac{5040}{2} = 2520 \\)

2. 当A必须在B的左侧且两者必须紧挨着时：

我们可以把A和B看作一个整体（AB），这样就变成了6个“元素”（AB, C, D, E, F, G）的排列问题。6个不同元素的排列方式为6!。由于A和B在这个情况下只能以一种顺序出现（即AB，不能BA），我们不需要再做额外的除法或乘法。

\\( \text{总排列数} = 6! = 720 \\)

综上所述：
- 在第一种情况下，有2520种排列方式。
- 在第二种情况下，有720种排列方式。

其他的题目暂时回忆不起来，都是一些基础题，背一背就好了

# 面试题（20min左右）
不具备参考价值，看看就行，挺水的：
- 自我介绍
- 项目讲述
- 场景题：链式调用API的问题

这个最终还是拒了，首先宁可饿死也不会选这家企业，黑幕比较多，甲乙方公司都有非常严重的问题，而且福州这个城市宜居度还是比较差的，我只是拿这个面试刷刷自己的熟练度，没想到会水成这个样子