class DataProcessUnit:
    def __init__(self, processor, input_params={}, output_params=(), parse_output_dict=False, extra_input_kwargs={}):
        self.processor = processor
        self.input_params = input_params
        self.output_params = output_params
        self.parse_output_dict = parse_output_dict
        self.extra_input_kwargs = extra_input_kwargs
        
    def __call__(self, data: dict):
        input_params = {name: data[self.input_params[name]] for name in self.input_params}
        input_params.update(self.extra_input_kwargs)
        raw_output = self.processor(**input_params)
        if self.parse_output_dict:
            data.update(raw_output)
        else:
            if not isinstance(raw_output, tuple):
                raw_output = (raw_output,)
            for name, output in zip(self.output_params, raw_output):
                data[name] = output
        return data