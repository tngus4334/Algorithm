# 집합은 중복을 허용하지 않는 자료형

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus) # 집합화 시킨다 O(N)
    for order in orders: # m
        if order not in menus_set: # O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)