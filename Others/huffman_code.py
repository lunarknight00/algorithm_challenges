from collections import Counter
import heapq
class TreeNode:
    def __init__(self,key,val,isJoin=False):
        self.key = key
        self.val = val
        self.isJoin = isJoin
        self.left = None
        self.right = None

    def __lt__(self,others):
        return self.val < others.val

def huffmanCode(string:str):
    # compute frequency
    frenq = Counter(string)
    pq = list()
    for k, v in frenq.items():
        heapq.heappush(pq,(v,TreeNode(k,v)))
    while len(pq) > 1:
        v1,node1 = heapq.heappop(pq)
        v2,node2 = heapq.heappop(pq)
        node = TreeNode(None,v1+v2,isJoin=True)
        node.left = node1
        node.right = node2
        heapq.heappush(pq,(v1+v2,node))
    return pq[0][1]

def preorder(root):
    if not root:
        return
    if not root.key:
        print("Join node: ",end=" ")
    else:
        print("Character node: ",root.key,end=" ")
    print(root.val)
    if root.left: preorder(root.left)
    if root.right: preorder(root.right)

if __name__ == "__main__":
    node = huffmanCode("abracadabra")
    preorder(node)
