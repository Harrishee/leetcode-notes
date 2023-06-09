
# [刷题笔记 Overview](README.md)

# 主题

Pracetice some basics in the [Playground](playground/practice.py)

- 高频：
    - 宽度优先搜索（BFS）
    - 深度优先搜索（DFS）
    - 二分法（Binary Search）
    - 双指针（2 Pointer）
    - 堆、栈、队列、哈希表（Heap，Stack，Heap，HashMap）
    - 链表（LinkedList）
    - 二叉树（Binary Tree）
    - 二叉搜索树（Binary Search Tree）
    - 前缀和（Prefix Sum）
    - 快速排序与归并排序（Quick Sort/ Merge Sort）

- 中频：
    - 动态规划（DP）
    - 字典树（Trie）
    - 并查集（Union Find）
    - 位运算（Bit Manipulation）
    - 单调栈与单调队列（Monotone Stack/ Queue）
    - 扫描线（Sweep Line）
    - TreeMap

---

# [基础](基础.md)
### 思想
* 排序
* 二分: `显式二分法，隐式二分法：左闭右闭，左闭右开`
* 双指针: `同向双指针，相向双指针`
* 单调栈 / 单调队列
* heapq
* 前缀和

### 链表
* 基础操作: `快慢指针，反转链表，虚拟头节点`
* 排序、插入、删除、反转、合并，需要在脑里抽象出来节点操作的样子

### 二叉树
* 基础操作: `前中后序遍历`
* 层序遍历: `需要记录层数或者不需要记录层数`
* 迭代写法
* 完全二叉树，BST特性

### 回溯
* 回溯类型: 
    - `需要记录路径，不需要返回值`
    - `不需要记录路径，但需要记录某些特征的返回值`
* 记忆化搜索: `需要返回值`

### 图
* 简单图 dfs
* 简单图 bfs:
    - `需要或者不需要记录层数`
    - `最短路径长度，注意是长度而不是具体的路径`
    - `多源bfs`
* 隐式图 word xxx `一般bfs / 双向bfs`
* 有向图 自己构造
* Topology: `返回值：是否可排序 / 排序后的数组 / 拓扑层数`
* 权重图 最短路径
* 最小生成树

### 动态规划
* 01背包 - 每个物品用一次
    - 2d: `dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])`
    - 1d: `dp[j] = max(dp[j], dp[j - w[i]] + v[i])` 内循环背包反向遍历
    - 组合类: `dp[j] += dp[j - nums[i]]`
* 完全背包 - 每个物品无限用
    - 1d: `dp[j] = max(dp[j], dp[j - w[i]] + v[i])` 内循环背包正向遍历
    - 求组合数: 外层for循环遍历物品，内层for遍历背包
    - 求排列数: 外层for循环遍历背包，内层for遍历物品
* 打家劫舍
* 股票问题
* 子序列问题

### 其他
* 树:
    - 前缀树
    - 并查集
* 位运算

---

# [1. 链表](链表.md)
1. [设计链表](链表.md#设计链表) [707](https://leetcode-cn.com/problems/design-linked-list)
2. [LRU缓存](链表.md#LRU缓存) [146](https://leetcode-cn.com/problems/lru-cache/)
3. [链表排序](链表.md#链表排序) [148](https://leetcode-cn.com/problems/sort-list) merge sort
4. [反转链表 II](链表.md#反转链表-ii) [92](https://leetcode.cn/problems/reverse-linked-list-ii)
5. [奇偶链表](链表.md#奇偶链表) [328](https://leetcode-cn.com/problems/odd-even-linked-list)
6. [链表相交](链表.md#链表相交) [160](https://leetcode-cn.com/problems/intersection-of-two-linked-lists)
7. [环形链表和入口](链表.md#环形链表和入口) [142](https://leetcode-cn.com/problems/linked-list-cycle-ii)
8. [两两交换链表中的节点](链表.md#两两交换链表中的节点) [24](https://leetcode-cn.com/problems/swap-nodes-in-pairs)
9. [删除排序链表中的重复元素 II](链表.md#删除排序链表中的重复元素-ii) [82](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii)
10. [重排链表](链表.md#重排链表) [143](https://leetcode-cn.com/problems/reorder-list)
11. [K 个一组翻转链表](链表.md#k个一组翻转链表) [25](https://leetcode-cn.com/problems/reverse-nodes-in-k-group)
12. [合并 K 个升序链表](链表.md#合并-k-个升序链表) [23](https://leetcode-cn.com/problems/merge-k-sorted-lists) heapq
13. [旋转链表](链表.md#旋转链表) [61](https://leetcode-cn.com/problems/rotate-list)
14. [复制带随机指针的链表](链表.md#复制带随机指针的链表) [138](https://leetcode-cn.com/problems/copy-list-with-random-pointer)
15. [分隔链表](链表.md#分隔链表) [86](https://leetcode-cn.com/problems/partition-list)
16. [从链表中删去总和值为零的连续节点](链表.md#从链表中删去总和值为零的连续节点) [1171](https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list)

---

# [2. 二叉树](二叉树.md)
### 二叉树属性
1. [是否对称](二叉树.md#是否对称) [101](https://leetcode-cn.com/problems/symmetric-tree)
2. [最大深度](二叉树.md#最大深度) [104](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree)
3. [最小深度](二叉树.md#最小深度) [111](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree)
4. [最大宽度](二叉树.md#二叉树的最大宽度) [662](https://leetcode-cn.com/problems/maximum-width-of-binary-tree) 二叉树性质
5. [平衡二叉树](二叉树.md#平衡二叉树) [110](https://leetcode-cn.com/problems/balanced-binary-tree)
6. [二叉树的直径](二叉树.md#二叉树的直径) [543](https://leetcode-cn.com/problems/diameter-of-binary-tree)
7. [二叉树的坡度](二叉树.md#二叉树的坡度) [563](https://leetcode-cn.com/problems/binary-tree-tilt)
8. [完全二叉节点数量](二叉树.md#完全二叉节点数量) [222](https://leetcode-cn.com/problems/count-complete-tree-nodes) 二叉树性质

### 二叉树操作和遍历
1. [根到叶路径上的不足节点](二叉树.md#根到叶路径上的不足节点) [1080](https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths)
2. [路径总和](二叉树.md#路径总和) [112](https://leetcode-cn.com/problems/path-sum)
3. [路径总和II](二叉树.md#路径总和2) [113](https://leetcode-cn.com/problems/path-sum-ii)
4. [二叉树中的最大路径和](二叉树.md#二叉树中的最大路径和) [124](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum)
5. [翻转二叉树](二叉树.md#翻转二叉树) [226](https://leetcode-cn.com/problems/invert-binary-tree)
6. [合并二叉树](二叉树.md#合并二叉树) [617](https://leetcode-cn.com/problems/merge-two-binary-trees)
7. [树左下角值](二叉树.md#树左下角值) [513](https://leetcode-cn.com/problems/find-bottom-left-tree-value)
8. [左叶子和](二叉树.md#左叶子和) [404](https://leetcode-cn.com/problems/sum-of-left-leaves)
9. [另一棵树的子树](二叉树.md#另一棵树的子树) [572](https://leetcode-cn.com/problems/subtree-of-another-tree)
10. [二叉树的最近公共祖先](二叉树.md#二叉树的最近公共祖先) [236](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree)

### BST属性
1. [二叉搜索树的最小绝对差](二叉树.md#二叉搜索树的最小绝对差) [530](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst)
2. [二叉搜索树中的众数](二叉树.md#二叉搜索树中的众数) [501](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree)
3. [二叉搜索树中第K小的元素](二叉树.md#二叉搜索树中第K小的元素) [230](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst)

### BST操作和遍历
1. [二叉搜索树中的搜索](二叉树.md#二叉搜索树中的搜索) [700](https://leetcode-cn.com/problems/search-in-a-binary-search-tree)
2. [二叉搜索树的插入操作](二叉树.md#二叉搜索树的插入操作) [701](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree)
3. [二叉搜索树的删除](二叉树.md#二叉搜索树的删除) [450](https://leetcode-cn.com/problems/delete-node-in-a-bst)
4. [修建二叉搜索树](二叉树.md#修建二叉搜索树) [669](https://leetcode-cn.com/problems/trim-a-binary-search-tree)
5. [二叉搜索树的范围和](二叉树.md#二叉搜索树的范围和) [938](https://leetcode-cn.com/problems/range-sum-of-bst)
6. [把二叉搜索树转换为累加树](二叉树.md#把二叉搜索树转换为累加树) [538](https://leetcode-cn.com/problems/convert-bst-to-greater-tree)
7. [二叉搜索树的最近公共祖先](二叉树.md#二叉搜索树的最近公共祖先) [235](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree)

### 二叉树构造
1. [最大二叉树](二叉树.md#最大二叉树) [654](https://leetcode-cn.com/problems/maximum-binary-tree)
2. [前序中序构造二叉树](二叉树.md#前序中序构造二叉树) [105](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)
3. [中序后序构造二叉树](二叉树.md#中序后序构造二叉树) [106](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal)
4. [前序后序构造二叉树](二叉树.md#前序后序构造二叉树) [889](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal)
5. [将有序数组转换为二叉搜索树](二叉树.md#将有序数组转换为二叉搜索树) [108](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree)
6. [序列化和反序列化二叉搜索树](二叉树.md#序列化和反序列化二叉搜索树) [449](https://leetcode-cn.com/problems/serialize-and-deserialize-bst) TODO
7. [二叉树的序列化与反序列化](二叉树.md#二叉树的序列化与反序列化) [297](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree) TODO


### 其他
1. [删点成林](二叉树.md#删点成林) [1110](https://leetcode-cn.com/problems/delete-nodes-and-return-forest)

---

# [3. 回溯算法](回溯.md)
### 子集组合排列问题
1. [子集](回溯.md#子集) [78](https://leetcode-cn.com/problems/subsets)
2. [子集 II](回溯.md#子集-ii) [90](https://leetcode-cn.com/problems/subsets-ii)

3. [组合](回溯.md#组合) [77](https://leetcode-cn.com/problems/combinations)
4. [组合总和](回溯.md#组合总和) [39](https://leetcode-cn.com/problems/combination-sum)
5. [组合总和 II](回溯.md#组合总和-ii) [40](https://leetcode-cn.com/problems/combination-sum-ii)
6. [组合总和 III](回溯.md#组合总和-iii) [216](https://leetcode-cn.com/problems/combination-sum-iii)
7. [电话号码组合](回溯.md#电话号码组合) [17](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number)

8. [全排列](回溯.md#全排列) [46](https://leetcode-cn.com/problems/permutations)
9. [全排列 II](回溯.md#全排列-ii) [47](https://leetcode-cn.com/problems/permutations-ii)

10. [分割回文串](回溯.md#分割回文串) [131](https://leetcode-cn.com/problems/palindrome-partitioning)
11. [复原IP地址](回溯.md#复原ip地址) [93](https://leetcode-cn.com/problems/restore-ip-addresses)

### 棋盘问题
1. [N皇后](回溯.md#n皇后) [51](https://leetcode-cn.com/problems/n-queens)
2. [解数独](回溯.md#解数独) [37](https://leetcode-cn.com/problems/sudoku-solver)

### 其他
1. [递增子序列](回溯.md#递增子序列) [491](https://leetcode-cn.com/problems/increasing-subsequences) TODO
2. [重新安排行程](回溯.md#重新安排行程) [331](https://leetcode-cn.com/problems/reconstruct-itinerary) TODO
3. [目标和](回溯.md#目标和) [494](https://leetcode-cn.com/problems/target-sum) memo / dp
4. [单词拆分](回溯.md#单词拆分) [139](https://leetcode-cn.com/problems/word-break) memo / dp

---

# [4. 图论](图论.md)
### BFS 节点操作
1. [墙与门](图论.md#墙与门) [286](https://leetcode-cn.com/problems/walls-and-gates)
2. [岛屿数量](图论.md#岛屿数量) [200](https://leetcode-cn.com/problems/number-of-islands)
3. [克隆图](图论.md#克隆图) [133](https://leetcode-cn.com/problems/clone-graph)

### BFS 到终点最小层数
1. [进击的骑士](图论.md#进击的骑士) [1197](https://leetcode-cn.com/problems/minimum-knight-moves)
2. [获取食物的最短路径](图论.md#获取食物的最短路径) [1730](https://leetcode-cn.com/problems/shortest-path-to-get-food)
3. [迷宫中离入口最近的出口](图论.md#迷宫中离入口最近的出口) [1926](https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze)
4. [腐烂的橘子](图论.md#腐烂的橘子) [994](https://leetcode-cn.com/problems/rotting-oranges)
5. [迷宫](图论.md#迷宫) [490](https://leetcode-cn.com/problems/the-maze)
6. [迷宫 II](图论.md#迷宫-ii) [505](https://leetcode-cn.com/problems/the-maze-ii)

### 多源 BFS
1. [01 矩阵](图论.md#01矩阵) [542](https://leetcode-cn.com/problems/01-matrix)
2. [太平洋大西洋水流问题](图论.md#太平洋大西洋水流问题) [417](https://leetcode-cn.com/problems/pacific-atlantic-water-flow)

### 隐式 BFS
1. [单词接龙](图论.md#单词接龙) [127](https://leetcode-cn.com/problems/word-ladder)
2. [打开转盘锁](图论.md#打开转盘锁) [752](https://leetcode-cn.com/problems/open-the-lock)
3. [单词接龙 II](图论.md#单词接龙-ii) [126](https://leetcode-cn.com/problems/word-ladder-ii) TODO
4. [无向图中连通分量的数目](图论.md#无向图中连通分量的数目) [323](https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph)
    
### DFS基本操作
1. [迷宫](图论.md#迷宫dfs) [490](https://leetcode-cn.com/problems/the-maze)
2. [所有可能的路径](图论.md#所有可能的路径) [797](https://leetcode-cn.com/problems/all-paths-from-source-to-target)

### 拓扑排序
1. [课程表](图论.md#课程表) [207](https://leetcode-cn.com/problems/course-schedule)
2. [课程表 II](图论.md#课程表-ii) [210](https://leetcode-cn.com/problems/course-schedule-ii)

---

# [5. 动态规划](动规.md)
### 基础题目
1. [斐波那契数列](动规.md#斐波那契数列) [509](https://leetcode-cn.com/problems/fibonacci-number)
2. [爬楼梯](动规.md#爬楼梯) [70](https://leetcode-cn.com/problems/climbing-stairs)
3. [使用最小花费爬楼梯](动规.md#使用最小花费爬楼梯) [746](https://leetcode-cn.com/problems/min-cost-climbing-stairs)
4. [不同路径](动规.md#不同路径) [62](https://leetcode-cn.com/problems/unique-paths)
5. [不同路径 II](动规.md#不同路径-ii) [63](https://leetcode-cn.com/problems/unique-paths-ii)
6. [整数拆分](动规.md#整数拆分) [343](https://leetcode-cn.com/problems/integer-break)

### 背包问题
0/1背包
1. [分割等和子集](动规.md#分割等和子集) [416](https://leetcode-cn.com/problems/partition-equal-subset-sum)
2. [最后一块石头的重量 II](动规.md#最后一块石头的重量-ii) [1049](https://leetcode-cn.com/problems/last-stone-weight-ii)
3. [目标和](动规.md#目标和) [494](https://leetcode-cn.com/problems/target-sum)
4. [一和零](动规.md#一和零) [474](https://leetcode-cn.com/problems/ones-and-zeroes)

完全背包
1. [零钱兑换 II](动规.md#零钱兑换ii) [518](https://leetcode.cn/problems/coin-change-ii/)
2. [组合总和 IV](动规.md#组合总和iv) [377](https://leetcode-cn.com/problems/combination-sum-iv)
3. [爬楼梯](动规.md#爬楼梯kp) [70](https://leetcode-cn.com/problems/climbing-stairs) 背包版本
4. [零钱兑换](动规.md#零钱兑换) [322](https://leetcode-cn.com/problems/coin-change)
5. [完全平方数](动规.md#完全平方数) [279](https://leetcode-cn.com/problems/perfect-squares)
6. [单词拆分](动规.md#单词拆分) [139](https://leetcode-cn.com/problems/word-break) memo / dp

### 打家劫舍
1. [打家劫舍](动规.md#打家劫舍) [198](https://leetcode-cn.com/problems/house-robber)
2. [打家劫舍 II](动规.md#打家劫舍-ii) [213](https://leetcode-cn.com/problems/house-robber-ii)
3. [打家劫舍 III](动规.md#打家劫舍-iii) [337](https://leetcode-cn.com/problems/house-robber-iii) memo / dp

### 股票问题
1. [买卖股票的最佳时机](动规.md#买卖股票的最佳时机) [121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock)
2. [买卖股票的最佳时机 II](动规.md#买卖股票的最佳时机-ii) [122](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii)
3. [买卖股票的最佳时机 III](动规.md#买卖股票的最佳时机-iii) [123](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii) TODO
4. [买卖股票的最佳时机 IV](动规.md#买卖股票的最佳时机-iv) [188](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv) TODO
5. [买卖股票的最佳时机含手续费](动规.md#买卖股票的最佳时机含手续费) [714](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) TODO

### 子序列问题
不连续子序列
1. [最长递增子序列](动规.md#最长递增子序列) [300](https://leetcode-cn.com/problems/longest-increasing-subsequence)
2. [最长公共子序列](动规.md#最长公共子序列) [1143](https://leetcode-cn.com/problems/longest-common-subsequence)
3. [不相交的线](动规.md#不相交的线) [1035](https://leetcode-cn.com/problems/uncrossed-lines)

连续子序列
1. [最长连续递增子序列](动规.md#最长连续递增子序列) [674](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence)
2. [最长重复子数组](动规.md#最长重复子数组) [718](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray)
3. [最大子序和](动规.md#最大子序和) [53](https://leetcode-cn.com/problems/maximum-subarray)

编辑距离
1. [判断子序列](动规.md#判断子序列) [392](https://leetcode-cn.com/problems/is-subsequence)
2. [不同的子序列](动规.md#不同的子序列) [115](https://leetcode-cn.com/problems/distinct-subsequences)
3. [两个字符串的删除操作](动规.md#两个字符串的删除操作) [583](https://leetcode-cn.com/problems/delete-operation-for-two-strings)
4. [编辑距离](动规.md#编辑距离) [72](https://leetcode-cn.com/problems/edit-distance)

回文
1. [回文子串](动规.md#回文子串) [647](https://leetcode-cn.com/problems/palindromic-substrings)
2. [最长回文子序列](动规.md#最长回文子序列) [516](https://leetcode-cn.com/problems/longest-palindromic-subsequence)

---

# [刷题杂记](README.md)

    * 不需要额外空间的方法，就往位运算上想

    * 一般来说哈希表都是用来快速判断一个元素是否出现集合里

    * 回溯的本质是穷举，如果想高效一些，可以加一些剪枝的操作，但也改不了回溯法就是穷举的本质

    * 二叉树的构造，无论普通二叉树还是二叉搜索树一定前序，都是先构造中节点

    * 普通二叉树的属性，一般是后序，一般要通过递归函数的返回值做计算

    * 二叉搜索树的属性，一定是中序了，要不白瞎了有序性

    * 中序遍历二叉搜索树等于遍历有序数组

    * 前序+中序 / 中序+后序 确定一颗二叉树

    * 动规五步曲：
        1. 确定dp数组（dp table）以及下标的含义
        2. 确定递推公式
        3. dp数组如何初始化
        4. 确定遍历顺序
        5. 举例推导dp数组