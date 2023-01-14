print("******** PROGRAMMED BY ********")
print("****** Charlotte Quezada ******")
print("********** BSCOE 2-2 **********")
print("*** Sir Danilo Madrigalejos ***\n")


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # Node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    print("* * * Sample Trial * * *")
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)
    print("Given List for Binary Tree:", countries)
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    print("\n* * * Using the letters in your full name as the content of the Binary Tree * * *")
    name = ["C", "H", "A", "R", "L", "O", "T", "T", "E", "M", "Q", "U", "E", "Z", "A", "D", "A"]
    name_tree = build_tree(name)
    print("Given List for Binary Tree:", name)
    print("Is the given letter M in the list?", name_tree.search("M"))
    print("Is the given letter B in the list?", name_tree.search("B"))
    print(name_tree.pre_order_traversal())
    print(name_tree.in_order_traversal())
    print(name_tree.post_order_traversal())

    # User Input
    def get_letter():  # Asks user input for the letter the user wants to search on the list
        search_letter = input(str("Please enter the letter you want to search in the list: "))
        print("Is the given letter "f"{search_letter} in the list?", user_name_tree.search(search_letter))

    print("\n* * * Asking for User Input as the content of the Binary Tree * * *")
    user_name = input(str("Please enter your full name with space in between each letter: "))
    user_name_list = user_name.split()
    user_name_tree = build_tree(user_name_list)
    print("Given List for Binary Tree:", user_name_list)
    get_letter()
    get_letter()
    print(user_name_tree.pre_order_traversal())
    print(user_name_tree.in_order_traversal())
    print(user_name_tree.post_order_traversal())
