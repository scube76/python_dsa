# ROOT = 0 , Child, Leaf nodes, LEVELS, height and depth

# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.children = []
#         self.parent = None
    
#     def add_child(self,child):
#         child.parent = self
#         # print(self)
#         self.children.append(child)
    
#     def get_level(self):
#         level =0
#         while self.parent:
#             self = self.parent
#             level +=1
#         return level 
        

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 2 
#         prefix = spaces + '|__' if self.parent else ''
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
        
        
# def build_tree():
#     root_node  = TreeNode('Electronics')

#     laptop_node = TreeNode('Laptops')
#     phone_node = TreeNode('Phones')
#     tablet_node = TreeNode('Tablets')

#     root_node.add_child(laptop_node)
#     # print('Inside build tree', root_node)
#     root_node.add_child(phone_node)
#     root_node.add_child(tablet_node)

#     laptop_node.add_child(TreeNode('Dell'))
#     laptop_node.add_child(TreeNode('hp'))
#     laptop_node.add_child(TreeNode('asus'))

#     phone_node.add_child(TreeNode('Iphone'))
#     phone_node.add_child(TreeNode('Samsung'))
#     phone_node.add_child(TreeNode('GioNee'))

#     tablet_node.add_child(TreeNode('Ipad'))
#     tablet_node.add_child(TreeNode('Notepad'))
#     tablet_node.add_child(TreeNode('Thinkpad'))

#     # print(phone_node.get_level())

#     return root_node


# if __name__ == '__main__':
#     root = build_tree()
#     root.print_tree()


# 1. Exercise solution 

# class TreeNode:
#     def __init__(self,name,designation):
#         self.name = name
#         self.designation = designation
#         self.data = f"{name} ({designation})"
#         self.children = []
#         self.parent = None
    
#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
    
#     def get_level(self):
#         level =0
#         while self.parent:
#             self = self.parent
#             level +=1
#         return level 
        

#     def print_tree(self,option):
#         if option == 1:
#             spaces = ' ' * self.get_level() * 2 
#             prefix = spaces + '|__' if self.parent else ''
#             print(prefix + self.name)
#             if self.children:
#                 for child in self.children:
#                     child.print_tree(1)

#         elif option == 2:
#             spaces = ' ' * self.get_level() * 2 
#             prefix = spaces + '|__' if self.parent else ''
#             print(prefix + self.designation)
#             if self.children:
#                 for child in self.children:
#                     child.print_tree(2)
#         else:
#             spaces = ' ' * self.get_level() * 2 
#             prefix = spaces + '|__' if self.parent else ''
#             print(prefix + self.data)
#             if self.children:
#                 for child in self.children:
#                     child.print_tree(3)
        
# def build_tree():
#     root_node = TreeNode('Nipul','CEO')

#     cto_node = TreeNode('Chinmay','CTO')
#     root_node.add_child(cto_node)

#     infrastructure_head_node = TreeNode('Vishwa','Infrastructure Head')
#     infrastructure_head_node.add_child(TreeNode('Dhaval','Cloud Manager'))
#     infrastructure_head_node.add_child(TreeNode('Abhijeet','App Manager'))
#     cto_node.add_child(infrastructure_head_node)
#     cto_node.add_child(TreeNode('Aamir','Application Head'))

#     hr_node = TreeNode('Gels','HR')
#     root_node.add_child(hr_node)
#     hr_node.add_child(TreeNode('Peter','Policy Manager'))
#     hr_node.add_child(TreeNode('Waqas','Recruitment Manager'))

#     return root_node

# if __name__ == '__main__':
#     print("Options available")
#     print("1. name tree\n2. designation tree\n3. name and designation tree\n")
#     print('Option chossen',3)
#     print()
#     root = build_tree()
#     root.print_tree(3)


# Exercise 2

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []  
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level =0
        while self.parent:
            self = self.parent
            level +=1
        return level 
        
    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 2 
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
    
def build_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root = build_tree()
    root.print_tree(1)



