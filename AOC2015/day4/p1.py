from hashlib import md5

seed = 'ckczppom'
for i in range(1000000000):
    if md5((seed + str(i)).encode()).hexdigest()[:5] == '00000':
        print(i)
        break
