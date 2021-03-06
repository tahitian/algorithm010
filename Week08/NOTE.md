## 第八周学习总结


### 位运算

指定位置的位运算

- 将x最右边的n位清零:x&(~0<<n)
- 获取x的第n位值(0或者1):(x>>n)&1
- 获取x的第n位的幂值:x&(1<<n)
- 仅将第n位置为1:x|(1<<n)
- 仅将第n位置为0:x&(~(1<<n))
- 将x最高位至第n位(含)清零:x&((1<<n)-1)
- 将第n位至第0位(含)清零:x&(~((1<<(n+1))-1))

实战位运算要点

- 判断奇偶:  
    x%2==1 —>(x&1)==1  
    x%2==0 —>(x&1)==0
- x>>1—>x/2.  
    即: x=x/2; —> x=x>>1;  
    mid=(left+right)/2; —> mid=(left+right)>>1;
- X=X&(X-1)清零最低位的1
- X&-X=>得到最低位的 1
- X&~X=>0


### 布隆过滤器

一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索一个元素是否在一个集合中。  

优点是空间效率和查询时间都远远超过一般的算法，缺点是有一定的误识别率和删除困难。

当元素在布隆过滤器中命中的时候，元素可能在集合中；当没有命中的时候，则一定不在集合中。

实践中通常作为缓存使用。


### LRU cache

使用哈希表和双链表的组合数据结构实现的最近最少使用缓存功能。

O(1)的查询、修改、更新的时间复杂度。


### 排序算法

#### 比较排序

时间复杂度为 O(n^2) 的排序算法：
- 冒泡排序
- 插入排序
- 选择排序

时间复杂度为 O(nlogn) 的排序算法：
- 快速排序
- 归并排序
- 堆排序

时间复杂度为 O(n^k)(1<k<2) 的排序算法：
- 希尔排序

#### 非比较排序
- 基数排序
- 桶排序
- 基数排序
