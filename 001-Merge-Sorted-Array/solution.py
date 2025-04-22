def merge_sorted_arrays(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        elif nums2[j] > nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1  
        else :
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1

print(merge_sorted_arrays([1,2,3,0,0,0], 3, [2,5,6], 3))  # [1, 2, 2, 3, 5, 6]
