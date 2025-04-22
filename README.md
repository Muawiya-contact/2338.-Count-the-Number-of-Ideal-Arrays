# 🧠 LeetCode Hard: 2338. Count the Number of Ideal Arrays

## 📌 Problem Description

You are given two integers `n` and `maxValue`, which define the properties of an **ideal array**. An array is considered **ideal** if:

1. Every element is between `1` and `maxValue`, inclusive.
2. Every element is divisible by its previous element (i.e., `arr[i] % arr[i-1] == 0` for all `i > 0`).

### 🔁 Objective

Return the number of distinct ideal arrays of length `n`.  
Since the answer can be very large, return it **modulo** `10^9 + 7`.

---

## 🧪 Example 1

**Input:**
n = 2, maxValue = 5
**Output:**
10

**Explanation:**
The ideal arrays are:
- Starting with `1`: [1,1], [1,2], [1,3], [1,4], [1,5]
- Starting with `2`: [2,2], [2,4]
- Starting with `3`: [3,3]
- Starting with `4`: [4,4]
- Starting with `5`: [5,5]

---

## 💡 Approach

We use **Dynamic Programming** with **Divisor Expansion**:

- Let `dp[x]` be the number of ideal arrays starting with `x`.
- For each array length from `2` to `n`, we expand possible values based on their divisors.
- We use a bottom-up DP approach and take modulo `10^9 + 7` at every step.

This efficiently computes all valid sequences without generating each one explicitly.

---

## 🚀 Solution (Python)

```python
class Solution(object):
    def idealArrays(self, n, maxValue):
        """
        :type n: int
        :type maxValue: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [0] * (maxValue + 1)

        for x in range(1, maxValue + 1):
            dp[x] = 1

        for length in range(2, n + 1):
            new_dp = [0] * (maxValue + 1)
            for x in range(1, maxValue + 1):
                for multiple in range(x, maxValue + 1, x):
                    new_dp[multiple] = (new_dp[multiple] + dp[x]) % MOD
            dp = new_dp

        return sum(dp) % MOD
```
        return sum(dp) % MOD
# 📊 Time and Space Complexity
Metric | Complexity
Time | O(n × log(maxValue))
Space | O(maxValue)

# ✅ Constraints
+ 2 <= n <= 10^4

+ 1 <= maxValue <= 10^4

  
# 👨‍💻 Author

**Muawiya – AI Student & Mathematician**  
Founder of [⚡ Coding Moves](https://www.youtube.com/@Coding_Moves)  
> *Passionate about building intelligent systems and mastering the art of programming.*



#📢 Stay Connected
🔹 YouTube: <a href ="https://www.youtube.com/@Coding_Moves">@Coding_Moves </a>
🔹 GitHub: <a href="https://github.com/Muawiya-contact">Muawiya-contact</a>
🔹 LinkedIn: <a href="https://www.linkedin.com/in/contactmuawia">Muawiya's Profile</a>



