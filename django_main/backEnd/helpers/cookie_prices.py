class CookiePrices:
    @classmethod
    def get_cookie_price(cls, cookie_name):
        cookie_prices = {
            "buns": 1.1,
            "donuts": 1.5
        }
        return cookie_prices.get(cookie_name)


