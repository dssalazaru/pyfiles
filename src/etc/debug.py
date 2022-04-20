class Debug:
    def __init__(self, enabled):
        self.enabled = enabled
        self.path = 'C:\\data\\test\\'

    def isEnabled(self):
        if self.enabled : 
            print (f'[{__name__}] DEBUG MODE is Enabled | TestPath: {self.path}')
            return self.enabled
    
    def testpath(self):
        if self.enabled : 
            return self.path