# Pass 319/320 test cases, not effecient enough, read through solutions (dynamic programming)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        '''
        Initial Solution that shows my thinking, second one is a more data effecient method


        # Constructing the bucket
        bucket = []
        max_height = 0
        try:
            max_height = max(height)
        except:
            return 0
        
        for a in range(0, max_height):
            layer = []
            for b in range(0, height.__len__()):
                layer.append(" ")
            bucket.append(layer)
        for a in range(0, height.__len__()):
            for b in range(0, height[a]):
                bucket[b][a] = "■"
        
        rain = 0
        for a in range(0, bucket.__len__()):
            occurrences = bucket[a].count("■")
            if occurrences >= 2:
                first = -1
                last = -1
                for b in range(0, bucket[a].__len__()):
                    if first == -1 and bucket[a][b] == "■":
                        first = b
                    elif bucket[a][b] == "■":
                        last = b
                # print("(" + str(first) + ", " + str(last) + ")")
                debris_count = 0
                rain += bucket[a][first:last].count(" ")
        
        # for a in range(bucket.__len__()-1, -1, -1):
        #    print(bucket[a])
        
        '''
        
        rain = 0
        max_height = 0
        try:
            max_height = max(height)
        except:
            return 0
        for a in range(0, max_height):
            if sum(height) == 0:
                break
            occurrences = height.__len__() - height.count(0)
            if occurrences > 1:
                first = -1
                last = -1
                for a in range(0, height.__len__()):
                    if first == -1 and height[a] != 0:
                        first = a
                    elif height[a] != 0:
                        last = a
                rain += height[first:last].count(0)
                for b in range(0, height.__len__()):
                    if height[b] != 0:
                        height[b] -= 1
                
        return rain