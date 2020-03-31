import json
from unittest import TestCase
from cart_calculator import *


class TestCartCalculator(TestCase):
    def setUp(self):
        self.VALUES_JSON = "tests/test_data.json" #noqa
        self.VALUES_JSON_OBJECT = json.load(open(self.VALUES_JSON, "r")) #noqa

        self.READABLE_PRICES = {
            article["id"]: article["price"]
            for article in self.VALUES_JSON_OBJECT["articles"]
        }

        self.READABLE_DISCOUNTS = {
            discount["article_id"]: (
                discount["type"], discount["value"]
            )
            for discount in self.VALUES_JSON_OBJECT["discounts"]
        }
    
    def test_if_calculated_subtotal_is_right(self):
        cart_1_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 1)
        cart_2_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 2)
        cart_3_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 3)
        cart_4_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 4)
        cart_5_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 5)

        self.assertEqual(cart_1_subtotal, 2000)
        self.assertEqual(cart_2_subtotal, 1400)
        self.assertEqual(cart_3_subtotal, 1998)
        self.assertEqual(cart_4_subtotal, 378)
        self.assertEqual(cart_5_subtotal, 441)
    
    def test_if_shipping_fee_is_right(self):
        cart_1_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 1)
        cart_2_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 2)
        cart_3_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 3)
        cart_4_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 4)
        cart_5_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 5)

        calculate_shipping_fee_cart_1 = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_1_subtotal)
        calculate_shipping_fee_cart_2 = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_2_subtotal)
        calculate_shipping_fee_cart_3 = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_3_subtotal)
        calculate_shipping_fee_cart_4 = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_4_subtotal)
        calculate_shipping_fee_cart_5 = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_5_subtotal)

        self.assertEqual(calculate_shipping_fee_cart_1, 400)
        self.assertEqual(calculate_shipping_fee_cart_2, 400)
        self.assertEqual(calculate_shipping_fee_cart_3, 400)
        self.assertEqual(calculate_shipping_fee_cart_4, 800)
        self.assertEqual(calculate_shipping_fee_cart_5, 800)
    

    def test_if_calculated_discount_is_right(self):
        cart_1_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 1)
        cart_2_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 2)
        cart_3_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 3)
        cart_4_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 4)
        cart_5_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 5)

        self.assertEqual(cart_1_discount, 50)
        self.assertEqual(cart_2_discount, 25)
        self.assertEqual(cart_3_discount, 599.4)
        self.assertEqual(cart_4_discount, 94.5)
        self.assertEqual(cart_5_discount, 44.1)
    
    def test_if_cart_total_is_right(self):
        cart_1_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 1)
        cart_2_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 2)
        cart_3_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 3)
        cart_4_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 4)
        cart_5_subtotal = calculate_products_subtotal(self.VALUES_JSON_OBJECT, 5)

        cart_1_shipping = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_1_subtotal)
        cart_2_shipping = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_2_subtotal)
        cart_3_shipping = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_3_subtotal)
        cart_4_shipping = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_4_subtotal)
        cart_5_shipping = calculate_shipping_fee(self.VALUES_JSON_OBJECT, cart_5_subtotal)

        cart_1_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 1)
        cart_2_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 2)
        cart_3_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 3)
        cart_4_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 4)
        cart_5_discount = calculate_products_discount(self.VALUES_JSON_OBJECT, 5)

        cart_1_total = int(cart_1_subtotal + cart_1_shipping - cart_1_discount)
        cart_2_total = int(cart_2_subtotal + cart_2_shipping - cart_2_discount)
        cart_3_total = int(cart_3_subtotal + cart_3_shipping - cart_3_discount)
        cart_4_total = int(cart_4_subtotal + cart_4_shipping - cart_4_discount)
        cart_5_total = int(cart_5_subtotal + cart_5_shipping - cart_5_discount)

        self.assertEqual(cart_1_total, 2350)
        self.assertEqual(cart_2_total, 1775)
        self.assertEqual(cart_3_total, 1798)
        self.assertEqual(cart_4_total, 1083)
        self.assertEqual(cart_5_total, 1196)