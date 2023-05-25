import pytest
import copy
import solution
import practice


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestSolution:
    def setup_method(self):
        self.sol = solution.Solution()
        self.yourCode = practice.Practice()
        self.sort_test_cases = [
            # nums
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1, 3, 2, 4, 5],
            [1, 1, 1, 1, 1],
            [1],
            [],
            list(range(300, 0, -1)),
            [0] * 100,
            [-1, 0, 1] * 333 + [-1],
            [1, -1] * 100,
            [0, -0, 0, -0, 0],
        ]

        self.search_test_cases = [
            # nums, target
            [[5,7,7,8,8,10], 8],
            [[5,7,7,8,8,10], 6],
            [[], 0],
            [[1], 1],
            [[1], 0],
            [[1]*200 + [2]*200, 2],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1],
            [[-100] + [0]*99 + [100]*100, -100],
            [[-100] + [0]*99 + [100]*100, 0],
            [[-100] + [0]*99 + [100]*100, 100],
            [[-100]*111 + [0]*222 + [100]*333, -101],
        ]

        self.heapq_test_cases = [
            # points, k
            [[[1, 3], [-2, 2]], 1],
            [[[3, 3], [5, -1], [-2, 4]], 2],
            [[[0, 1], [1, 0]], 2],
            [[[-2, -4], [3, 3], [2, -1]], 1],
            [[], 0],
            [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], 3],
            [[[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5]], 4],
            [[[0, 10], [10, 0], [-10, 0], [0, -10]], 2],
            [[[0, 0], [100, 100], [-100, -100], [200, 200], [-200, -200]], 5],
            [[[-3, -4], [-1, -2], [0, 0], [1, 2], [3, 4]], 2],
            [[[1, 3], [2, -2], [4, 1], [1, -3], [3, 2]], 4],
            [[[0, 0], [1, 1], [-1, -1], [2, 2], [-2, -2]], 5],
        ]

        self.reverse_test_cases = [
            # head
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(2)),
            ListNode(1),
            None,
            ListNode(9, ListNode(4, ListNode(11, ListNode(3, ListNode(5, ListNode(7)))))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))))))),
        ]

        self.reverse2_test_cases = [
            # head, left, right
            [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4],
            [ListNode(1, ListNode(2)), 1, 2],
            [ListNode(1), 1, 1],
            [None, 1, 1],
            [ListNode(9, ListNode(4, ListNode(11, ListNode(3, ListNode(5, ListNode(7)))))), 2, 5],
            [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))))))), 3, 6],
        ]

        self.tree_test_cases = [
            # root
            TreeNode(1, None, TreeNode(2, TreeNode(3))),
            TreeNode(1),
            None,
            TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5)), TreeNode(6, None, TreeNode(7, TreeNode(8)))),
            TreeNode(1, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5))))),
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7, TreeNode(8, TreeNode(9, TreeNode(10)))))))))),
            TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))),
            TreeNode(9, TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8))), TreeNode(13, TreeNode(11), TreeNode(15))),
        ]

        self.topo_test_cases = [
            # numCourses, prerequisites
            [2, [[1, 0]]],
            [4, [[1, 0], [2, 0], [3, 1], [3, 2]]],
            [3, [[1, 0], [2, 1], [0, 2]]],
            [2, [[0, 1], [1, 0]]],
            [1, []],
            [0, []],
            [5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]]],
        ]

        self.knapsack_01_test_cases = [
            # bag_size, weight, value
            [4, [2, 1, 3], [4, 2, 3]],
            [6, [3, 5, 6], [2, 3, 4]],
            [9, [3, 5, 6, 7], [2, 3, 4, 5]],
            [176, [79, 58, 86, 11, 28, 62, 15, 68], [83, 14, 54, 79, 72, 52, 48, 62]],
        ]


    def test_quick_sort(self):
        for i, input in enumerate(self.sort_test_cases):
            expected = self.sol.quick_sort(input)
            assert self.yourCode.quick_sort(input) == expected


    def test_merge_sort(self):
        for i, input in enumerate(self.sort_test_cases):
            expected = self.sol.merge_sort(input)
            assert self.yourCode.merge_sort(input) == expected
    

    def test_binary_search(self):
        for i, input in enumerate(self.search_test_cases):
            nums, target = input
            expected = self.sol.binary_search(nums, target)
            assert self.yourCode.binary_search(nums, target) == expected
    

    def test_heapq(self):
        for i, input in enumerate(self.heapq_test_cases):
            points, k = input
            expected = self.sol.k_closest_points(points, k)
            assert self.yourCode.k_closest_points(points, k) == expected


    def linked_list_to_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result


    def test_reverse_linked_list(self):
        for i, input in enumerate(self.reverse_test_cases):
            head = input
            expected = self.sol.reverse_linked_list(copy.deepcopy(head))
            result = self.yourCode.reverse_linked_list(copy.deepcopy(head))
            assert self.linked_list_to_list(result) == self.linked_list_to_list(expected)


    def test_reverse_linked_list2(self):
        for i, input in enumerate(self.reverse2_test_cases):
            head, left, right = input
            expected = self.sol.reverse_linked_list2(copy.deepcopy(head), left, right)
            result = self.yourCode.reverse_linked_list2(copy.deepcopy(head), left, right)
            assert self.linked_list_to_list(result) == self.linked_list_to_list(expected)
    

    def test_preorder_traversal(self):
        for i, input in enumerate(self.tree_test_cases):
            root = input
            expected = self.sol.preorderTraversal(copy.deepcopy(root))
            result = self.yourCode.preorderTraversal(copy.deepcopy(root))
            assert result == expected
    
    def test_inorder_traversal(self):
        for i, input in enumerate(self.tree_test_cases):
            root = input
            expected = self.sol.inorderTraversal(copy.deepcopy(root))
            result = self.yourCode.inorderTraversal(copy.deepcopy(root))
            assert result == expected
    
    def test_postorder_traversal(self):
        for i, input in enumerate(self.tree_test_cases):
            root = input
            expected = self.sol.postorderTraversal(copy.deepcopy(root))
            result = self.yourCode.postorderTraversal(copy.deepcopy(root))
            assert result == expected

    def test_topo_sort(self):
        for i, input in enumerate(self.topo_test_cases):
            numCourses, prerequisites = input
            expected = self.sol.findOrder(numCourses, copy.deepcopy(prerequisites))
            result = self.yourCode.findOrder(numCourses, copy.deepcopy(prerequisites))
            assert result == expected


    def test_knapsack_01_2d(self):
        for i, input in enumerate(self.knapsack_01_test_cases):
            bag_size, weight, value = input
            expected = self.sol.knapsack_01_2d(bag_size, weight, value)
            result = self.yourCode.knapsack_01_2d(bag_size, weight, value)
            assert result == expected
    
    def test_knapsack_01_1d(self):
        for i, input in enumerate(self.knapsack_01_test_cases):
            bag_size, weight, value = input
            expected = self.sol.knapsack_01_1d(bag_size, weight, value)
            result = self.yourCode.knapsack_01_1d(bag_size, weight, value)
            assert result == expected

if __name__ == '__main__':
    pytest.main(['-v', __file__])