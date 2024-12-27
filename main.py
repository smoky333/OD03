mas = [6, 9, 3, 1, 8, 2, 7, 5, 4]
n = len(mas)
for run in range(n-1):
    for i in range(n-1):
        if mas[i] > mas[i+1]:
            mas[i], mas[i+1] = mas[i+1], mas[i]
print(mas)



def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = list(filter(lambda x: x < element, s[1:]))
    centre = [i for i in s if i==element]
    right = list(filter(lambda x: x > element, s[1:]))

    return quick_sort(left) + centre + quick_sort(right)


print(quick_sort([8, 9, 3, 1, 6, 2, 7, 6, 1]))





      
      












