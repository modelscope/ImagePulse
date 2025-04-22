import random, torch, json


class AnyText:
    def __init__(self, path, shuffle=True, seed=None, num_data=1000000, multi_prompt=False, num_prompt=1):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            prompt_list = []
            for i in data["data_list"]:
                prompt_list.append(i["caption"])
        self.data = prompt_list
        if shuffle:
            if seed is None:
                seed = torch.randint(0, 10**9, size=(1,)).tolist()[0]
            random.seed(seed)
            random.shuffle(self.data)
        self.num_data = num_data
        self.multi_prompt = multi_prompt
        self.num_prompt = num_prompt
    
    def __getitem__(self, i):
        if self.multi_prompt:
            return {"prompt": self.data[i * self.num_prompt: i * self.num_prompt + self.num_prompt]}
        else:
            return {"prompt": self.data[i]}
    
    def __len__(self):
        return self.num_data // self.num_prompt
