class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBegin(self, data):
        node = Node(data,self.head)
        self.head = node
    
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        itr = self.head
        resultant = ""
        while itr:
            resultant += str(itr.data) +"-->"
            itr = itr.next
        return resultant+"null"
    
    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)
    
    def insertList(self,list):
        self.head = None
        for data in list:
            self.insertAtEnd(data)
    def getLength(self):
        count =0
        itr =self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def removeAt(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while count < index-1:
            count +=1
            itr=itr.next
        itr.next = itr.next.next

    def inssertAt(self,index,data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.insertAtBegin(data)
        if index==self.getLength()-1:
            self.insertAtEnd(data)
        itr = self.head
        count=0
        while count<index-1:
            itr = itr.next
            count +=1
        next = itr.next
        itr.next = Node(data,next)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            raise Exception("Empty linked list")
        
        itr =self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                return
            itr = itr.next 

        print("No such value exists")
    
    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("Empty linked list")

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise Exception("no such value exists")





if __name__ == '__main__':
    ll1 =LinkedList()
    # ll1.insertAtBegin(24)
    # ll1.insertAtBegin(25)
    # ll1.insertAtBegin(26)
    # ll1.insertAtBegin(27)
    # ll1.insertAtEnd(23)
    # ll1.insertAtEnd(22)
    # ll1.insertAtEnd(21)
    # print(ll1.printLinkedList())
    # print(ll1.getLength())
    # ll1.insertList([1,2,3,2,4,5,3,4])
    # print(ll1.printLinkedList())
    # print(ll1.getLength())
    ll1.insertList([0,1,2,3,4,5,6,7])
    # ll1.removeAt(2)
    # ll1.inssertAt(7,"Jims")
    # ll1.insert_after_value(5,"Jims")
    ll1.remove_by_value(5)
    print(ll1.printLinkedList())
