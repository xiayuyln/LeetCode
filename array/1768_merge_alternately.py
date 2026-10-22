"""
1768. 交替合并字符串
https://leetcode.cn/problems/merge-strings-alternately/
难度：简单

思路：双指针 i、j 分别遍历两个字符串，每轮先取 word1[i]、再取 word2[j]，
      某一方越界就跳过，只追加另一方剩下的字符。

复杂度：时间 O(m+n)，空间 O(m+n)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i = j = 0

        ans = []
        while i < m or j < n:
            if i < m:
                ans.append(word1[i])
                i += 1
            if j < n:
                ans.append(word2[j])
                j += 1

        return "".join(ans)
