#快速排序
def quick_sort(lists,left,right):
    #递归过程中，发现left和right一致时，停止递归，直接返回列表
    if left >= right:
        print("左边%s大于等于右边%s,直接返回数组"%(left,right) )
        return lists

    #定义游标
    low = left
    print("定义游标low为left%s"% left)
    high = right
    print("定义游标high为right%s"% right)

    #取参考标志，最左边的元素
    key = lists[low]
    print("设置参考标志key%s为最左边的元素 lists[low%s]"% (key,low))
    while low < high:
        print("当low%s小于high%s"% (low,high))
        #从最右侧向左，依次和标志元素对比，如果右侧的元素大于标志元素
        while low < high and lists[high] >= key:
            print("当low%s 小于 high%s 并且 lists[high%s]%s 大于等于 key%s" % (low, high, high, lists[high], key))
            #右侧减1
            print("右侧high%s减一" % high)
            high -= 1
            print("赋值给high%s"% high)
        #否则low赋high值
        lists[low] = lists[high]
        print("否则low%s赋high%s值"%(low,high))

        #从最左侧向右，依次和标志元素对比，如果左侧的元素小于标志元素
        while low < high and lists[low] <= key:
            print("当low%s 小于 high%s 并且 lists[low%s]%s 小于等于 key%s" % (low, high, low, lists[low], key))
            #左侧加1
            print("左侧low%s加一" % low)
            low += 1
            print("赋值给low%s"% low)
        #否则high赋low值
        lists[high] = lists[low]
        print("否则high%s赋low%s值"%(high,low))

    #最后给high位置赋值
    lists[high] = key
    print("最后给high%s位置赋key%s值" % (high,key))

    #处理左侧元素
    print("处理左侧元素")
    quick_sort(lists,left, low - 1)
    #处理右侧元素
    print("处理右侧元素")
    quick_sort(lists, low + 1,right)
    return lists

alist = [0,10,88,19,9,1,7]
print(quick_sort(alist,0,6))