alist = [0,1,10,88,19,9,1,7]

def binary_search(arr,start,end,hkey):
    if start > end:
        print("如果传入的开始下标%s比结束下标%s大，则直接返回-1，表示不合法，不进行排序查找" % (start,end))
        return -1

    mid = start + (end - start) / 2
    mid = int(mid)
    print("对传入的开始下标%s和结束下标%s进行二分，加上开始下标%s,获得二分查找下标%s" % (start, end, start,mid))
    print("mid:%s" % mid)

    if arr[mid] > hkey:
        print("如果二分查找下标的值%s大于查找值%s" % (arr[mid],hkey))
        return binary_search(arr,start,mid -1 ,hkey)
    if arr[mid] < hkey:
        print("如果二分查找下标的值%s小于查找值%s" % (arr[mid], hkey))
        return binary_search(arr, mid + 1, end, hkey)
    print("返回被查找值的下标%s" % mid)
    return mid

print("-------------未经排序的查找------------------")
print("alist:%s"% alist)
print("binary_search(alist,0,7,9):%s"% binary_search(alist,0,7,9))

print("-------------经排序后的查找------------------")
alist = sorted(alist)
print("alist:%s"% alist)
print("binary_search(alist,0,7,9):%s"% binary_search(alist,0,7,9))

print("-------------倒排后的查找------------------")
alist = sorted(alist,reverse=True)
print("alist:%s"% alist)
print("binary_search(alist,0,7,9):%s"% binary_search(alist,0,7,9))