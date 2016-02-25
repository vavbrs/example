
class Cacher(object):
    def __init__(self, func):
        self.func = func
        self.cache = dict()
    
    def __call__(self, *args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in self.cache:
            return self.cache[key]
        res = self.func(*args, **kwargs)
        self.cache[key] = res
        return res
    
cached = Cacher

@cached
def func(a, b, m=1):
    return m * (a + b)

print func(1, 2)
print func(1, 2, 3)
print func(1, 2, m=3)
print func(2, 3)

print func.cache