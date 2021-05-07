import numpy as np
class stack:
    """
    class stack for linear data structure
    """
    def __init__(self):
        """
        constructor
        """
        self.arr = np.ndarray([])
    def push(self,data):
        """
        common push method. Add element to the top
        """
        self.arr = np.append(self.arr,data)
    def pop(self):
        """
        common pop method. Removes top element
        """
        self.arr=self.arr[:-1]
    def __str__(self):
        retval = '[ '
        for a in self.arr[1:]:
            retval+=str(a)+' '
        retval+=']'
        return retval
    def __len__(self):
        return len(self.arr)-1
