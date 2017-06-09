class SegmentTree(object):
    def __init__(self, inputArray):
        arraySize = len(inputArray)
        self.pSize = 1
        while(self.pSize < arraySize):
            self.pSize = self.pSize * 2 
        self.tree = [0] * (2 * self.pSize + 1)
        self.index = [0] * (2 * self.pSize + 1)
        for i in range(arraySize):
            self.tree[self.pSize + i] = inputArray[i]
            self.index[self.pSize + i] = i
        for i in range(self.pSize - 1, 0, -1):
            if(self.tree[i * 2] < self.tree[i * 2 + 1]):
                self.index[i] = self.index[i * 2]
            else:
                self.index[i] = self.index[2 * i + 1]
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])
    def minNum(self, s, t):
        s = s + self.pSize - 1
        t = t + self.pSize + 1
        res = 10000000000
        index = -1
        while(s^t^1):
            if(~s&1):
                if(res > self.tree[s^1]):
                    res = self.tree[s^1]
                    index = self.index[s^1]
            if(t&1):
                if(res > self.tree[t^1]):
                    res = self.tree[t^1]
                    index = self.index[t^1]
            s = s >> 1
            t = t >> 1
        return res, index
class Solution(object):
    def largest(self, heights, tree, left, right):
        stack = [(left, right)]
        maxValue = -1
        while(stack):
            left, right = stack.pop()
            if(left > right):
                continue
            elif(left == right):
                maxValue = max(maxValue, heights[left])
            else:
                minValue, mid = tree.minNum(left, right)
                maxValue = max(maxValue, minValue * (right -left + 1))
                stack.append(left, mid -1)
                stack.append(mid + 1, right)
    def largestRectangleArea(self, heights):
        length = len(heights)
        if(length == 0):
            return 0
        tree = SegmentTree(heights)
        return self.largest(tree, 0, length - 1)
