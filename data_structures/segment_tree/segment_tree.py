class SegmentTree:
    """A implementation of a naive segmentation tree.
    >>> tree = SegmentTree([10, 11, 12, 13, 14])
    >>> tree.build(0,4,1)
    >>> tree.array
    {8: 10, 9: 11, 4: 21, 5: 12, 2: 33, 6: 13, 7: 14, 3: 27, 1: 60}
    >>> tree.getSum(2,4,0,4,1)
    39
    >>> tree.getSum(0,2,0,4,1)
    33
    """    
    def build(self, left, right, pivot):
        if left == right:
            # print(left)
            self.array[pivot] = self.data[left]
            return
        # print(pivot) 
        mid = left + (right - left)//2 
        self.build(left, mid,2*pivot)
        self.build(mid + 1, right, 2*pivot + 1)
        self.array[pivot] = self.array[2*pivot] + self.array[2* pivot +1]

    def getSum(self,qleft,qright,start,end,pivot):
        if (qleft <= start and end <= qright):
            return self.array[pivot]
        mid = start + ((end - start) // 2)
        if (pivot in self.change):
            self.array[pivot * 2] = self.change[pivot] * (mid - start + 1), 
            self.array[pivot * 2 + 1] = self.change[pivot] * (end - mid),
            self.change[pivot * 2] = self.change[pivot * 2 + 1] = self.change[pivot]
            self.change[pivot] = 0        
        sum = 0
        if qleft <= mid:
            sum += self.getSum(qleft,qright,start, mid, pivot*2)
        if mid < qright:
            sum += self.getSum(qleft,qright,mid + 1, end, (pivot * 2) + 1)
        return sum


    # void update(int l, int r, int c, int s, int t, int p) {
    #   if (l <= s && t <= r) {
    #     d[p] = (t - s + 1) * c, b[p] = c;
    #     return;
    #   }
    #   int m = s + ((t - s) >> 1);
    #   if (b[p]) {
    #     d[p * 2] = b[p] * (m - s + 1), d[p * 2 + 1] = b[p] * (t - m),
    #           b[p * 2] = b[p * 2 + 1] = b[p];
    #     b[p] = 0;
    #   }
    #   if (l <= m) update(l, r, c, s, m, p * 2);
    #   if (r > m) update(l, r, c, m + 1, t, p * 2 + 1);
    #   d[p] = d[p * 2] + d[p * 2 + 1];
    # }
    def update(self, uleft, uright, toChange, start, end,pivot):
        if (uleft <= start and end <= uright):
            self.array[pivot] = (end - start + 1) * toChange
            self.change[pivot] = toChange
            return 
        mid = start + ((end - start) // 2)
        if (pivot in self.change):
            self.array[pivot * 2] = self.change[pivot] * (mid - start + 1), 
            self.array[pivot * 2 + 1] = self.change[pivot] * (end - mid),
            self.change[pivot * 2] = self.change[pivot * 2 + 1] = self.change[pivot]
            self.change[pivot] = 0
        if uleft <= mid:
            self.update(uleft,uright,start, mid, pivot*2)
        if mid < uright:
            self.update(uleft,uright,mid + 1, end, (pivot * 2) + 1)
        return sum

if __name__ == "__main__":
    from doctest import testmod
    testmod()