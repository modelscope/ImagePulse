import random, pandas, torch


class DiffusionDB:
    def __init__(self, path, shuffle=True, seed=None, num_data=1000000):
        self.data = pandas.read_parquet(path)["prompt"].tolist()
        if shuffle:
            if seed is None:
                seed = torch.randint(0, 10**9, size=(1,)).tolist()[0]
            random.seed(seed)
            random.shuffle(self.data)
        self.num_data = num_data
    
    def __getitem__(self, i):
        return {"prompt": self.data[i]}
    
    def __len__(self):
        return self.num_data
