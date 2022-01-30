# stock = 2
# dates = [1, 10]
# supplies= [10, 100]
# k =11 -> 공장이 멈추게 해서는 안되기 때문에 10, 100 순서
# 현재 재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루중 제일 많은 밀가루를 받는게 목표
# 1. 현재 재고상태에 따라 최고값을 받아야함 -> 동적으로 변경되는 상황
# 2. 제일 많은값, 제일 큰값을 뽑아내야한다.

# 1. 데이터를 넣을 때마다 최댓값을 동적으로 변경시키며
# 2. 최소/최댓값을 바로 꺼낼 수 있는 구조를 사용하면 좋다 -> 힙

import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0 # supplies에서 최소로 공급받을 수 있는 횟수
    last_added_date_index = 0 # 가장 마지막에 더했던 날짜의 인덱스
    max_heap = []

    while stock <= k: # stock이 k보다 낮을 때 까지
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock: # 공장을 멈추지 않기 위해서 dates보다는 stock이 많아야한다. -> 특정인덱스의 date가 stock보다 클때까지 반
            heapq.heappush(max_heap, -supplies[last_added_date_index]) # [20]
            last_added_date_index += 1

        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))