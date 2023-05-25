import heapq
import collections


class Solution:

    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        left, right = [], []

        for i in range(1, len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


    def merge_sort(self, nums):
        def merge(left, right):
            res = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res += left[i:]
            res += right[j:]

            return res
        
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return merge(left, right)


    def binary_search(self, nums, target):
        def get_left():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    ans = mid
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def get_right():
            left, right = 0, len(nums) - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2
                if target == nums[mid]:
                    ans = mid
                    left = mid + 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans
        
        return [get_left(), get_right()]
    

    def k_closest_points(self, points, k):
        h, ans = [], []
        for pair in points:
            heapq.heappush(h, (pair[0] ** 2 + pair[1] ** 2, pair))
        
        for pair in range(k):
            ans.append(heapq.heappop(h)[1])

        return ans
    

    def reverse_linked_list(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre

            pre = cur
            cur = tmp
        return pre


    def reverse_linked_list2(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        for _ in range(left - 1):
            pre = pre.next
        
        cur = pre.next
        for _ in range(right - left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp

        return dummy.next


    def preorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


    def inorderTraversal(self, root):
        if not root:
            return []
        
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:     
                stack.append(cur)
                cur = cur.left
            else:		
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right	
        return result
    

    def postorderTraversal(self, root):
        if not root:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
    

    def findOrder(self, numCourses, prerequisites):
        graph = {t: [] for t in range(numCourses)}
        for nex, pre in prerequisites:
            graph[pre].append(nex)
        
        def topo(graph):
            indeg = {node: 0 for node in graph}
            for node in graph:
                for nei in graph[node]:
                    indeg[nei] += 1
            
            q = collections.deque()
            ans = []
            for node in indeg:
                if indeg[node] == 0:
                    q.append(node)
            
            while q:
                node = q.popleft()
                ans.append(node)
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return ans if len(ans) == len(graph) else []
        return topo(graph)


    def knapsack_01_2d(self, bag_size, weight, value):
        ROW, COL = len(weight), bag_size + 1
        dp = [[0] * COL for _ in range(ROW)]

        for j in range(1, COL):
            if j >= weight[0]:
                dp[0][j] = value[0]
        
        for i in range(1, ROW):
            for j in range(1, COL):
                if j < weight[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

        return dp[-1][-1]
    

    def knapsack_01_1d(self, bag_size, weight, value):
        # dp[j]表示背包容量为j时，能装的最大价值
        # bag_size + 1，因为背包容量为0时，价值为0
        dp = [0] * (bag_size + 1)

        # 从后往前遍历，因为dp[j]依赖于dp[j-weight[i]]
        # 先遍历物品，再遍历背包（大到小）
        # (1, len(weight))，从1开始，因为dp[0] = 0，不需要更新
        # (bag_size, weight[i] - 1, -1)，从bag_size开始，因为dp[bag_size]依赖于dp[bag_size-weight[i]]
        for i in range(1, len(weight)):
            for j in range(bag_size, weight[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
        return dp[-1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right