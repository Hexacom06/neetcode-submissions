class TimeMap:

    def __init__(self):
        self.umap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.umap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        lo, hi, res  = 0, len(self.umap[key])-1, ""
        while lo <= hi:
            mid = (lo+hi)//2
            if self.umap[key][mid][0] <= timestamp: 
                res = self.umap[key][mid][1] 
                lo = mid+1
            else: hi = mid-1
        return res


        