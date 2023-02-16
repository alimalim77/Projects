def count_perfect_sums(arr, given_num):
    arr.sort()  # sort the input array in non-decreasing order
    count = 0
    path = []

    def find_perfect_sums_helper(start_idx, curr_sum, path):
        nonlocal count
        if curr_sum == given_num:
            count += 1
            return
        for i in range(start_idx, len(arr)):
            if arr[i] > given_num - curr_sum:
                break
            path.append(arr[i])
            find_perfect_sums_helper(i+1, curr_sum + arr[i], path)
            path.pop()

    find_perfect_sums_helper(0, 0, path)
    return count

    
print(count_perfect_sums([9,7,3,12,7],14))
print(count_perfect_sums([4,7,8,2,3],12))