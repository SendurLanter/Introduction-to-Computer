HEAPSIZE = 500000
class Node:
    def __init__(self):
        self.key = 0
        self.element = []

class Heap:
    def __init__(self):
        self.size=0
        self.ary=[]

    def printArray(self):
        print("(Index, Key, Element)")
        for i in range(len(self.ary)):
            print("({},{},{})".format(str(i),str((self.ary)[i].key),str((self.ary)[i].element)))

    def isempty(self):
        #我改了下 因為我覺得self.size這變數是多此一舉
        return (len(self.ary)==0)

    def printByPopping(self):
        while not (self.isempty()):
            print(self.pop(),end='')
        print("")

    def getTopKey(self):
        return (self.ary)[0].key

    def swap(self,i,j):
        (self.ary)[i], (self.ary)[j] = (self.ary)[j], (self.ary)[i] 


    def push(self,key,element):
        #todo
        new=Node()
        new.key=key
        new.element=element
        self.ary.append(new)

        index = len(self.ary)-1

        #往上檢查
        while index!=0:
            #(index-1)/2=parent
            if(self.ary[int((index-1)/2)].key > key):
                self.swap(index,int((index-1)/2))
                index = int((index-1)/2)
            else:
                break

        self.balancing()
        return

    def pop(self):
        #todo
        if(len(self.ary)==0):
            return
        #將min(root)砍掉並回傳
        mini=self.ary.pop(0)
        #如果heap空了
        if(len(self.ary)==0):
            return mini.element
        #複製最後一個node提到0當新root
        self.ary.insert(0,self.ary[-1])
        #砍掉剛剛那node原本的位置
        self.ary.pop(-1)
        #因root換了 重新檢查heap並排序
        self.balancing()
        return mini.element

    #檢查heap中的每個node是否符合規則
    def balancing(self):
        size = len(self.ary)-1

        def check(index):
            left=2*index+1
            right=2*index+2
            if left <= size and self.ary[index].key > self.ary[left].key :
                s=left
            else:
                s=index

            if right <= size and self.ary[s].key > self.ary[right].key :
                s=right
            if s!=index:
                self.swap(s,index)
                check(s)
            else:
                return
        #從root開始檢查
        check(0)