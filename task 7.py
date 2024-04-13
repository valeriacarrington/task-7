def max_candies(pinatas):
    n = len(pinatas)
    max_candies = 0

    for i in range(n):
        candies = pinatas[i-1] * pinatas[i] * pinatas[i+1] if i > 0 and i < n - 1 else pinatas[i] * pinatas[i]
        max_candies = max(max_candies, candies)

    return max_candies

# Example usage
pinatas = [1, 2, 3, 4, 5]
print("Maximum amount of candies:", max_candies(pinatas))
