class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n-1):
            count, say = 1, ""
            for i in range(len(result)):
                if i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                else:
                    # print(result[i])
                    say += str(count)+result[i]
                    count = 1
                # print(say)
            result = say
        # print(result)
        return result

if __name__ == "__main__":
    s = Solution()
    s.countAndSay(4)