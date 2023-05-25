import pytest
import heapq
import collections


class Practice:
    """
    1. QUICK SORT
    """
    def quick_sort(self, nums):
        pytest.skip("PRACTICE")


    """
    2. MERGE SORT
    """
    def merge_sort(self, nums):
        pytest.skip("PRACTICE")


    """
    3. BINARY SEARCH @ LC 34
    """
    def binary_search(self, nums, target):
        pytest.skip("PRACTICE")


    """
    4. HEAPQ @ LC 973
        points = [[1, 3], [-2, 2]], k = 1 => [[-2, 2]] 
    """
    def k_closest_points(self, points, k):
        pytest.skip("PRACTICE")


    """
    5. REVERSE LINKED LIST 1 @LC 206
        head = [1,2,3,4,5] => [5,4,3,2,1]
    """
    def reverse_linked_list(self, head):
        pytest.skip("TODO")


    """
    6. REVERSE LINKED LIST 2 @LC 92
        head = [1,2,3,4,5], left = 2, right = 4 => [1,4,3,2,5]
    """
    def reverse_linked_list2(self, head, left, right):
        pytest.skip("TODO")


    """
    7. PREORDER TRAVERSAL @LC 144
        root = [1,null,2,3] => [1,2,3]
    """
    def preorderTraversal(self, root):
        pytest.skip("TODO")


    """
    8. INORDER TRAVERSAL @LC 94
        root = [1,null,2,3] => [1,3,2]
    """
    def inorderTraversal(self, root):
        pytest.skip("TODO")


    """
    9. POSTORDER TRAVERSAL @LC 145
        root = [1,null,2,3] => [3,2,1]
    """
    def postorderTraversal(self, root):
        pytest.skip("TODO")


    """
    10. TOPOLOGICAL SORT @LC 210
        numCourses = 2, prerequisites = [[1,0]], (cur, pre) => [0,1]
    """
    def findOrder(self, numCourses, prerequisites):
        pytest.skip("TODO")


    """
    11. 0-1 KNAPSACK 2D
        0-1 knapsack 1D space optimized
        bag_size = 4, weight = [2,1,3], value = [4,2,3] => 6
    """
    def knapsack_01_2d(self, bag_size, weight, value):
        pytest.skip("TODO")


    def knapsack_01_1d(self, bag_size, weight, value):
        pytest.skip("TODO")


# END *************** END *************** END *************** END *************** END

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
