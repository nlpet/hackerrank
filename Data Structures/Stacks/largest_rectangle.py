
def largest_rectangle(height):
    increasing, area, i = [], 0, 0
    while i <= len(height):
        if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
            increasing.append(i)
            i += 1
        else:
            last = increasing.pop()
            if not increasing:
                area = max(area, height[last] * i)
            else:
                area = max(area, height[last] * (i - increasing[-1] - 1 ))
    return area


if __name__ == "__main__":
    print largest_rectangle([1, 3, 5, 2, 1, 4, 6])
