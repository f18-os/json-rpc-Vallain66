class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0


    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children:
            c.show(level + 1)

    def todict(self):
        return {"name": self.name, "children": self.children, "val": self.val}


    def treetodict(self):
        child = []
        for c in self.children:
    	       child.append(c.todict())

        self.children = child
        self = self.todict()
        return self
