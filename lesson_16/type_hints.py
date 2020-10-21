from typing import Tuple, Dict, Union, Optional, Any, Iterable

# def check_string(string: str = 'qwe') -> bool:
#     return string.isupper()
#
#
# class Cart:
#
#     def __init__(self, products: list):
#         self.products = products
#
#
# def do_shop(cart: Cart):
#     for product in cart:
#         print(product)


# print(check_string(123))
#
#
# cart_ = Cart([1, 2, 3, 4, 5])
#
# do_shop()


# def iter_cart(products: Tuple[str, ...]):
#     print(products)
#
#
# products_ = ('tomato', 'cucumber', 'cherry', 'potato')
# iter_cart(products_)


def calculate_products_sum(products_: Dict[str, Union[float, int]]) -> Union[float, int]:
    return sum(products_.values())


def test(b: Iterable[Tuple[int, float]], a: Optional[int] = 5):
    print(a)


products = {
    'carrot': 20,
    'banana': 40.0,
}


i = [(1, 2.0), (2, 3.0)]
test(i)
calculate_products_sum(products)
