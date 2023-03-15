# python3


def build_heap(data):
    n=len(data)
    swaps = []
    n=len(data)
    
    for i in range(n // 2, -1, -1):
        while 2*i+1<n:
            j=2*i+1
            if j+1<n and data[j+1]<data[j]:
                j+=1
            if data[i] <= data[j]:
                break
            swaps.append((i,j))
            data[i], data[j] = data[j], data[i]
            i=j
    return swaps


def main():
    input_type=input()
    
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))
    else:
        raise ValueError("Invalid input type.")

    assert len(data) == n
    assert len(set(data)) == n
    swaps = build_heap(data)


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    print(len(swaps))
    if len(swaps) <= 4*n:
        print("Number of swaps is less than or equal to 4*n")
    else:
        print("Number of swaps is greater than 4*n")


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
#main()
