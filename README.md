# Level 3 - Backend - JoyJet Challenge

Some products are discounted because of a deal we made with the supplier.

There are two kinds of discounts:
- a direct cut to the article's price, e.g. get 50€ off your 300€ caviar tin and only pay 250€
- a percentage discount, e.g. get 20% off your 5€ creme fraiche and only pay 4€

Write code that generates `output.json` from `data.json`


## How to run

Running is simple, you just need to be using Python 3.6 >.

```
cd level3-backend
python main.py
```

### Running tests

```
cd level3-backend
python -m unittest
```

## How the project is organized

We divided the source-code as shown below.
Tests are in their folder, with the fixture files (the same data.json that is being used in settings.py)

```
.
├── README.md
└── level3-backend
    ├── cart_calculator.py
    ├── data.json
    ├── main.py
    ├── output.json
    ├── settings.py
    └── tests
        ├── __init__.py
        ├── test_calculator.py
        └── test_data.json
```

The `settings.py` file sets variables globally, not allowing circular-imports.

The `main.py` file is the main running application which outputs the file on the required format specification.

The `cart_calculator.py` is the file that contain all main functions to the project, allowing the code
to be reused on other circunstances.
