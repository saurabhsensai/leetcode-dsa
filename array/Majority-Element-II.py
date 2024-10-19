hashm = {}
arr = [1,2]
for i in range(0, len(arr)):
    if arr[i] not in hashm:
        hashm[arr[i]] = 1
    else:
        hashm[arr[i]] += 1
final = []
for item, value in hashm.items():
    if value > (len(arr)//3):
        final.append(item)

print(final)

