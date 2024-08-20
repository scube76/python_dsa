# Hashmap == dictionary
# https://youtu.be/ea8BRGxGmlA?si=agKSn7LD1WRAKUc3
# for example map1 = {"movie1":4,"movie2":3.2,"movie3":5,"movie4":2,"movie5":3}
# map1["movie3"]  ---hashfunction----Using asII method-----> 5   

# Collision Handling --> When the hash function is poorly written and more than 1 key generates the same hash number
# Method 1 Chaining --> Generating linkedlist in the same empty slot
# Method 2 Linear Probing --> Searching for an empty slot in allocated memory

class HashTable:
    def __init__(self):
        self.MAX =100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0 
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] =None

if __name__ == '__main__':
    t1 = HashTable()
    t1['Harry'] = 40
    t1['Billy'] = 80
    t1['Hew'] = 60
    print(t1['Hew'])
    print(t1.get_hash('Harry'))



