import json

from settings import VALUES_JSON_OBJECT
from cart_calculator import calculate_every_cart_in_file


cart_result_json = calculate_every_cart_in_file(VALUES_JSON_OBJECT)
output_json = open("output_py.json", "a")
json.dump(cart_result_json, output_json)