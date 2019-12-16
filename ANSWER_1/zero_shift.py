# The time complexity (Big-O) of this algorithm is <Answer: O(n) or Big-O(n) because you touch every item in the list once>

def zero_shift(a_list):
    count = 0
    for x in range(len(a_list)):
        if a_list[x] != 0:
            a_list[count] = a_list[x]
            count += 1
    while count < len(a_list):
        a_list[count] = 0
        count +=1
    return a_list


if __name__ == "__main__":
    # pass
    #
    values = [3, 0, 9, 10, 0, 1, 0, 7]
    print(zero_shift(values))
    
    other_list = [0, 0, 110, 5, 0, 3 ,77, 0, 0, 13]
    print(zero_shift(other_list))
    # assert values == [3, 9, 10, 1, 7, 0, 0, 0]
