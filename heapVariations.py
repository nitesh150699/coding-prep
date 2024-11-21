import heapq

def main():
    nums = [5, 3, 8, 1, 2]
    heapq.heapify(nums)

    heapq.heappush(nums, 4)

    min_element = heapq.heappop(nums)


    peek_element = nums[0] if nums else None
   
    pushed_popped = heapq.heappushpop(nums, 0)
  
    replaced_element = heapq.heapreplace(nums, 6)
  
    smallest = heapq.nsmallest(2, nums)
    largest = heapq.nlargest(2, nums)
   

    # Step 8: Max-Heap Implementation
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)  # Negate to simulate max-heap

    largest_from_max_heap = -heapq.heappop(max_heap)

if __name__ == "__main__":
    main()
