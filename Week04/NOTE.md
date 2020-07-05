## 第二周学习总结


#### 深度优先搜索和广度优先搜索

深度优先搜索代码模板

```
visited = set()
def dfs(node, visited):
   visited.add(node)
   # process current node here.
   ...
   for next_node in node.children():
     if not next_node in visited:
        dfs(next node, visited)
```

广度优先搜索代码模板

```
def BFS(graph, start, end):
   queue = []
   queue.append([start])
   visited.add(start)
   while queue:
     node = queue.pop()
     visited.add(node)
     process(node)
     nodes = generate_related_nodes(node)
     queue.push(nodes)
```


#### 贪心算法

贪心算法也是用于解决最优解问题，通过局部最优解得到全局最优解。

在实际应用中，贪心算法一般不能够真正得到最优解，但是如果能够得到最优解，贪心解法往往是最高效的。另外可以使用贪心算法来获取近似最优解。


#### 二分查找

适用条件：
>   - 函数具有单调性
>   - 具有上下边界
>   - 可以通过索引访问

代码模板：
```
left, right = 0, len(array) - 1
while left <= right:
   mid = (left + right) / 2
   if array[mid] == target:
      # find the target!!
      break or return result
   elif array[mid] < target:
      left = mid + 1
   else:
right = mid - 1
```