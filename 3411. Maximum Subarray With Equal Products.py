class Solution(object):
    def maxLength(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        ans = 1

        for i in range(n):
            prod = 1
            g = 0
            lc = 1

            for j in range(i, n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                lc = lcm(lc, nums[j])

                if prod == g * lc:
                    ans = max(ans, j - i + 1)

        return ans