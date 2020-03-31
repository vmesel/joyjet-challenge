import json

VALUES_JSON = "data.json" #noqa
VALUES_JSON_OBJECT = json.load(open(VALUES_JSON, "r")) #noqa

READABLE_PRICES = {
    article["id"]: article["price"]
    for article in VALUES_JSON_OBJECT["articles"]
}

READABLE_DISCOUNTS = {
    discount["article_id"]: (
        discount["type"], discount["value"]
    )
    for discount in VALUES_JSON_OBJECT["discounts"]
}