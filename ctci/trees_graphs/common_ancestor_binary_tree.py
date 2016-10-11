class common_ancestor(object):
    def __init__(self):
        self.path_p = []
        self.path_q = []

    def find_common(self, root = None, p = None, q = None):
        if root:
            if self.find_path(root, p, type="first") and self.find_path(root, q, type="second"):
                print self.find_common_ancestor(root).data
            else:
                print "One or both of nodes not found"
        else:
            print "Invalid Input"

    def find_path(self, root, node, type = "first"):
        if root.data == node.data:
            if type == "first":
                self.path_p.append(node)
            else:
                self.path_q.append(node)
            return True
        elif root.left:
            self.find_path(root.left, node, type)
        elif root.right:
            self.find_path(root.right, node, type)
        else:
            return False

    def find_common_ancestor(self, root):
        if len(self.path_p) > len(self.path_q):
            return self.path_p[- (len(self.path_p) - len(self.path_q))]
        elif len(self.path_p) < len(self.path_q):
            return self.path_q[- (len(self.path_q) - len(self.path_p))]
        else:
            return root

if __name__ == '__main__':
    c = common_ancestor()
    root, p, q = None, None, None
    c.find_common(root, p , q)