class solution:
    
    
    def __init__(self, string):
        self.string = string

    def ends_with(self, ending):
        return self.string.endswith(ending)


s = solution('abc')

print(s.ends_with('bc'))  # returns True

print(s.ends_with('d'))   # returns False
