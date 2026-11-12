class TimeMap:

    def __init__(self):
        self.my_map = {}# {key, [(val, time)]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.my_map.get(key):
            self.my_map[key].append((value, timestamp))
        else:
            self.my_map[key] = [(value, timestamp)]
        # print(self.my_map)

    def get(self, key: str, timestamp: int) -> str:
        nums = self.my_map.get(key, [])
        r = len(nums)-1
        l = 0
        mid = 0
        while l <= r:
            mid = (l + r)//2
            # print(mid, l, r)
            if nums[mid][1] == timestamp:
                return nums[mid][0]
            if timestamp < nums[mid][1]:
                r = mid - 1
            else:
                l = mid + 1
        # print(nums, timestamp, mid, l, r)
        if len(nums) == 0:
            return ""
        if mid >= len(nums):
            return nums[len(nums)-1][0] 
        if mid == 0 and nums[mid][1] > timestamp:
            return ""
        if nums[mid][1] > timestamp:
            return nums[mid-1][0]
        return nums[mid][0]
