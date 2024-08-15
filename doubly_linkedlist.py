class Node:
    def __init__(self,prev=None,data=None,next=None):
        self.prev =prev
        self.data =data
        self.next =next
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def printForward(self):
        if self.head is None:
            print("Empty DLL")
            return
        itr =self.head
        res_str = ""
        while itr:
            res_str +=str(itr.data)+"<-->"
            itr = itr.next
        print(res_str)
    
    def printBackwards(self):
        if self.head is None:
            print("Empty DLL")
            return
        itr =self.getLastNode()
        res_str=""
        while itr:
            res_str +=str(itr.data)+"<-->"
            itr = itr.prev
        print(res_str)

    def getLastNode(self):
        itr =self.head
        while itr.next:
            itr = itr.next
        return itr
    
    def getLength(self):
        itr = self.head
        count =0
        while itr:
            itr =itr.next
            count +=1
        return count
    
    def insertAtStart(self,data):
        if self.head is None:
            node = Node(None,data,self.head)
            self.head =node
        else:
            node = Node(None,data,self.head)
            self.head.prev=node
            self.head =node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(None,data,None)
        else:
            lastNode = self.getLastNode()
            lastNode.next = Node(lastNode,data,None)

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr =itr.next
        return count

        
    def insertAt(self,index,data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Length")
        if index==0:
            self.insertAtStart(data)
        if index==self.getLength()-1:
            self.insertAtEnd(data)
        itr = self.head
        count = 0
        while count <index-1:
            count +=1
            itr=itr.next
        next = itr.next
        itr.next = Node(itr,data,next) 

    def removeAt(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Length")
        if index==0:
            self.head=self.head.next
            self.head.prev=None #can be skipped as its default value is already null
            return

        itr = self.head
        count = 0
        # while count <index-1:
        #     count +=1
        #     itr=itr.next
        # itr.next = itr.next.next
        # itr.next.next.prev = itr
    # ABove code fails for last element removal
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)




if __name__ == '__main__':
    dll1=DoublyLinkedList()
    dll1.insertAtStart(5)
    dll1.insertAtStart(6)
    dll1.insertAtStart(7)
    dll1.insertAtStart(8)
    dll1.insertAtEnd(4)
    dll1.insertAtEnd(3)
    dll1.insertAtEnd(2)
    dll1.printForward()
    # dll1.printBackwards()
    dll1.insertAt(2,66)
    dll1.printForward()
    dll1.removeAt(7)
    dll1.printForward()
    dll1.insert_values([1,2,3,4,5,6,7,8,10])
    dll1.printForward()
            

    