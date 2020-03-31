from settings import (VALUES_JSON, VALUES_JSON_OBJECT, READABLE_PRICES, READABLE_DISCOUNTS)


def calculate_products_subtotal(json_object, cart_id):
    """
    Calculates products subtotal before applied discount
    and shipping fees.
    
    :params:
    json_object: json object
    cart_id: integer
    """
    cart = json_object["carts"][cart_id - 1]

    return sum(
        [
            READABLE_PRICES[item["article_id"]] * item["quantity"] 
            for item in cart["items"]
        ]
    )


def calculate_products_discount(json_object, cart_id):
    """
    Calculates products discount.
    
    :params:
    json_object: json object
    cart_id: integer
    """
    cart = json_object["carts"][cart_id - 1]

    final_discount = 0

    for item in cart["items"]:
        if item["article_id"] not in READABLE_DISCOUNTS.keys():
            continue
        
        discount = READABLE_DISCOUNTS[item["article_id"]]

        if discount[0] == "amount":
            final_discount += item["quantity"] * discount[1]
        else:
            final_discount += item["quantity"] * ((discount[1]/100) * READABLE_PRICES[item["article_id"]])
    
    return final_discount



def calculate_shipping_fee(json_object, products_subtotal):
    """
    Calculates products shipping cost based on products subtotal
    (without any chargeback).
    
    :params:
    json_object: json object
    cart_id: integer
    """
    shipping_fees = json_object["delivery_fees"]

    for idx, fee in enumerate(shipping_fees):
        if fee["eligible_transaction_volume"]["max_price"] >= products_subtotal:
            return fee["price"]


def calculate_every_cart_in_file(json_object):
    """
    Calculates carts final costs based on products subtotal, discount
    and shipping fees.
    
    :params:
    json_object: json object
    """
    final_dict = {"carts":[]}

    for cart_n, cart in enumerate(json_object["carts"], start=1):
        discount_available = calculate_products_discount(json_object, cart_n)
        cart_subtotal_available = calculate_products_subtotal(json_object, cart_n)
        shipping = calculate_shipping_fee(json_object, cart_subtotal_available)
        total = cart_subtotal_available + shipping - discount_available
        final_dict["carts"].append({"id": cart_n, "total": int(total)})
    
    return final_dict
