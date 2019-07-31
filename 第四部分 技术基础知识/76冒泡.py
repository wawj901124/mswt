#冒泡排序
def bubble_sort(lists):
    #获取数组长度
    count = len(lists) -1
    itemrange = range(count,0,-1)
    #N个元素遍历N次
    for index in itemrange:
        print("index:%s"% index)
        #第i个和第i+1个依次对比
        for sub_index in range(index):
            print("sub_index:%s" % sub_index)
            #大的元素冒上去
            if lists[sub_index] > lists[sub_index+1]:
                print("lists[%s] 大于lists[%s+1]" % (sub_index,sub_index))
                lists[sub_index],lists[sub_index+1] = lists[sub_index+1],lists[sub_index]
                print("lists[%s] 和lists[%s+1]对换值" % (sub_index, sub_index))
    return lists

alist = [0,10,88,19,9,1]
print(bubble_sort(alist))