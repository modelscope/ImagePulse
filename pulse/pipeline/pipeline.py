class DataPipeline:
    def __init__(self, units=()):
        self.units = units
        self.error_log = [0] * len(units)
        self.drop_log = [0] * len(units)
    
    def __call__(self, data, ignore_errors=False, debug_mode=False):
        for unit_id, unit in enumerate(self.units):
            if ignore_errors:
                try:
                    data = unit(data)
                except:
                    self.error_log[unit_id] += 1
                    return None
            else:
                data = unit(data)
            if debug_mode:
                print("-" * 200)
                for key in data:
                    print(key, data[key])
                print("-" * 200)
        return data
    
    def report_log(self):
        for unit_id, unit in enumerate(self.units):
            print(f"Unit id: {unit_id} Processor name: {unit.processor.__class__.__name__} Errors: {self.error_log[unit_id]} Drops: {self.drop_log[unit_id]}")
