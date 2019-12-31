r = 0

def main():
    data, K, M = get_list()
    calculate_s(data,K-1,M,0)
    print(r)

#Create a series of for-loops
def calculate_s(data,K,M,s):
    if K >= 0:
        for x in data[K]:
            calculate_s(data,K-1,M,s+(x*x))
    else:
        global r
        if s%M > r:
            r = s%M

def get_list():
#Get the K and M
    tmp = input()
    k_m = tmp.split()
    K = int(k_m[0])
    M = int(k_m[1])

#Get the data
    data = [None] * K
    for i in range(K):
        tmp = input()
        tmp = tmp.split()
        data[i] = list(map(int,tmp[1:]))

    return data, K, M

main()
