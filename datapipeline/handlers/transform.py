from datapipeline.schema.data_schema import data_schema

class Transformer:
    def __init__(self, data):
        self.data = data


    def transform(self):
        print("Transforming data")
        transformed = []
        for d in self.data:
            transformed.append(self.clean_value(d))
        return transformed


    def clean_value(self, input):
        for k, v in input.items():
            if(not v):
                input[k] = None
            elif(isinstance(v, dict)):
                input[k] = self.clean_value(v)
            elif(isinstance(v, str)):
                v = self.trim(v)
                v = self.to_lower(v)
                v = self.format(k,v)
                input[k] = v
            else:
                input[k] = self.format(k,v)
        return input


    def trim(self, value):
        return value.strip()


    def format(self, key, value):
        return eval(f"{data_schema[key]}('{value}')")

    def to_lower(self, value):
        return value.lower()

