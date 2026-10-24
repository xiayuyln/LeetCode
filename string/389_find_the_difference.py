"""
389. 找不同
https://leetcode.cn/problems/find-the-difference/
难度：简单

思路：用长度 26 的数组统计 s 里每个字母出现次数，再遍历 t 逐个减一。
      某个字母减到负数，说明它在 t 里多出来一个，就是答案。

复杂度：时间 O(n)，空间 O(1)（26 个计数器是常数级）
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - 97] += 1
        for ch in t:
            idx = ord(ch) - 97
            cnt[idx] -= 1

            if cnt[idx] < 0:
                return ch