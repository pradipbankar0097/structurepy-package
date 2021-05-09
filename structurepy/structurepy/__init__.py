import numpy as np
class stack:
    """
    class stack for linear data structure
    """
    def __init__(self):
        """
        basic constructor
        """
        self.arr = np.ndarray([1,])
    def __init__(self,array):
        __init__(self)
        np.append(self.arr,array)
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


class queue:
    """
    class queue for linear data structure
    """
    def __init__(self):
        """
        basic constructor
        """
        self.arr = np.ndarray([1,])
    def __init__(self,array):
        """
        parameterized constructor
        """
        __init__(self)
        np.append(self.arr,array)
    def push(self,data):
        """
        common push method. Add element to the rear
        """
        self.arr = np.append(self.arr,data)
    def pop(self):
        """
        common pop method. Removes front element
        """
        self.arr=self.arr[2:]
    def __str__(self):
        retval = '[ '
        for a in self.arr[1:]:
            retval+=str(a)+' '
        retval+=']'
        return retval
    def __len__(self):
        return len(self.arr)-1


