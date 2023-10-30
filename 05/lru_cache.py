class LRUCache:
    def __init__(self, limit=42):
        self.limit = limit
        self.values = {}
        self.order = []

    def __update_order(self, key):
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        if len(self.order) > self.limit:
            deleted_key = self.order.pop(0)
            del self.values[deleted_key]

    def get(self, key):
        if key not in self.values:
            return None

        val = self.values[key]
        self.__update_order(key)
        return val

    def set(self, key, value):
        self.values[key] = value
        self.__update_order(key)
