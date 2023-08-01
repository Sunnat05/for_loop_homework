def main(price):
    for a in list(range(1,11)):
        b=a*price
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    return list(range(price,b+1,price))
print(main(5))