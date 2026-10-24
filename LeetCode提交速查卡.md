# LeetCode 提交速查卡

> 放在 `C:\Users\18259\Desktop\LeetCode\` 里，做完题对着走一遍。

---

## 每题固定 4 步

### 第 1 步 · 建文件

路径：`LeetCode\<专题>\<题号>_<英文名>.py`

例：`string\389_find_the_difference.py`

内容模板（复制 `_template.py` 改）：

```
"""
<题号>. <中文名>
https://leetcode.cn/problems/<slug>/
难度：简单 / 中等 / 困难

思路：
    1.
    2.

复杂度：时间 O( )，空间 O( )
"""


class Solution:
    def xxx(self, ...) -> ...:
        pass
```

### 第 2 步 · 更新 README

在表格末尾加一行：

```
| 389 | 找不同 | 简单 | 哈希表 | 26 位计数数组，减到负数即答案 | 2026-10-24 |
```

### 第 3 步 · 打开终端

打开 `C:\Users\18259\Desktop\LeetCode` 文件夹 →
**地址栏点一下 → 输入 `cmd` → 回车**

确认黑窗口里显示的是：

```
C:\Users\18259\Desktop\LeetCode>
```

不是这个路径就是走错了。

### 第 4 步 · 三条命令

```
git add .
git commit -m "feat: 389 找不同"
git push
```

- `git add .` 回车后**没有输出**，正常
- `git commit` 显示 `N files changed` 才对
- `git push` 显示 `main -> main` 才成功

---

## 三条命令在干嘛

| 命令 | 作用 | 类比 |
| --- | --- | --- |
| `git add .` | 把改动装进箱子 | 打包 |
| `git commit -m "..."` | 封箱贴单 | 贴快递单 |
| `git push` | 送到 GitHub | 发快递 |

只 add 不 commit → 没封箱；只 commit 不 push → 没发货。

---

## 报错对照表

| 报错 | 原因 | 解决 |
| --- | --- | --- |
| `'git' 不是内部或外部命令` | Git 没装好 / 终端没重启 | 关掉窗口重开；还不行重装 Git |
| `nothing to commit` | 文件没保存，或不在当前文件夹 | 确认文件已保存、路径正确 |
| `fatal: not a git repository` | 打开的位置不对 | 必须进到 `Desktop\LeetCode` |
| `Authentication failed` | 登录失效 | 重新 `git push`，浏览器授权 |
| `rejected ... fetch first` | 网页上改过文件，本地落后 | 先 `git pull --rebase origin main` 再 push |

---

## 快速自检

敲 `git status`：

- `nothing to commit, working tree clean` → 已提交干净
- 列出一堆红色文件 → 忘了 `git add .`
- `Your branch is ahead of 'origin/main' by 1 commit` → 忘了 `git push`

---

## 什么时候才该去问 AI

- 出现上面表里没有的报错，**截图发过去**
- 想理解某个命令的**原理**（不是怎么做）
- 想优化结构、写注释、review 代码

「怎么传」这个问题，第三次之后就不该再问了。
