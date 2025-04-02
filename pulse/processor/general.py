import torch


class ListSampler:
    def __init__(self):
        pass
    
    def __call__(self, ls):
        i = torch.randint(0, len(ls), size=(1,)).tolist()[0]
        return ls[i]


class TextFormater:
    def __init__(self, template):
        self.template = template
        
    def __call__(self, *args, **kwargs):
        args = tuple(str(i) for i in args) + tuple(str(kwargs[i]) for i in kwargs)
        return self.template % args


class ListPacker:
    def __init__(self):
        pass
    
    def __call__(self, *args, **kwargs):
        ls = list(i for i in args) + list(kwargs[i] for i in kwargs)
        return ls
