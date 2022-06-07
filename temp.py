def highest_even(li):
    li.sort()
    li.reverse()
    for i in li:
        if i % 2 == 0:
            return i
            break

print(highest_even([10,12,1,23,4,8,11]))