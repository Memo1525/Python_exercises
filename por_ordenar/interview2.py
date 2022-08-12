def frequencySort(nums):
    num_dict = {}
    for k in nums:
        if k not in num_dict:
            num_dict[k] = 1
        else:
            num_dict[k] = num_dict[k] + 1



    num_dict = sorted(num_dict.items(), key=lambda x: (x[1], x[0]))
    print(num_dict)
    num_dict.sort(key=lambda i: i[1], reverse=False)
    res = []
    for key, value in num_dict:
        res += [key] * value
    return res


numeros=[4,5,6,5,4,3]
print(frequencySort(numeros))
