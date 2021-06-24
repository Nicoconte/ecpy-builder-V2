class Utils:
    
    def __init__(self):
        pass

    @staticmethod
    def get_dict(keys, values) -> dict:
        dictionary = {}

        for i in range(len(keys)):
            dictionary.update(dict([( str(keys[i]), values[i])]))

        return dictionary


