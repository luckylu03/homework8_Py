# Ghost objects are given a random color attribute 
# of white" or "yellow" or "purple" or "red" when instantiated

class Ghost(object):
    count = 0
    def __init__(self, color = ['white', 'yellow', 'purple', 'red']):
            self.color = color[Ghost.count]
            if Ghost.count < len(color)-1:
                Ghost.count+=1
            else:
                Ghost.count = 0