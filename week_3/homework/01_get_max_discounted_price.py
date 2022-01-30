shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    coupons.sort(reverse=True) # reverse=True : 내림차순 정렬
    prices.sort(reverse=True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0 # 최대할인가격

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100 # % 이기때문에 나누기 100 해야함
        price_index += 1
        coupon_index += 1

    while price_index < len(prices): # price도 끝에 갈때까지 반복
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))