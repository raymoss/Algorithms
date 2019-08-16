from collections import defaultdict
class TreeNode:
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None

def helper(start_index, end_index, dp):
    if start_index == end_index:
        return [None]
    temp_result = []
    if (start_index, end_index) in dp.keys():
        return dp[start_index, end_index]
    for i in range(start_index, end_index):
        left_node_list = helper(start_index, i, dp)
        right_node_list = helper(i + 1, end_index, dp)
        for j in left_node_list:
            for k in right_node_list:
                node = TreeNode(i)
                node.left = j
                node.right = k
                temp_result.append(node)
    dp[start_index, end_index] = temp_result
    return temp_result

def unique_binary_search_trees_2(input_num):
    if input_num == 0:
        return []
    dp = {}
    return helper(1, input_num + 1,dp)

print(unique_binary_search_trees_2(3))