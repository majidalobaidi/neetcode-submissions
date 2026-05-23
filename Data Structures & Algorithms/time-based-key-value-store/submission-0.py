import collections

class TimeMap:
    def __init__(self):
        self.value_dict = collections.defaultdict(list)
        self.time_dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time_dict.get(key, [])) - 1

        while l <= r:
            mid = (l + r) // 2
            current_ts = self.time_dict[key][mid]
            if current_ts == timestamp:
                return self.value_dict[key][mid]
            elif current_ts > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return self.value_dict[key][r] if r >= 0 else ""

# Example usage:
kv = TimeMap()
kv.set("foo", "bar", 1)
print(kv.get("foo", 1))   # Output: "bar"
print(kv.get("foo", 3))   # Output: "bar"
kv.set("foo", "bar2", 4)
print(kv.get("foo", 4))   # Output: "bar2"
print(kv.get("foo", 5))   # Output: "bar2"

