# telephone-routing
Telephone Routing is a Python project that helps find the cheapest operator for a given telephone number based on prefix matching.

## Features

- Efficient prefix matching using a Trie data structure
- Support for multiple operators with different pricing for various prefixes
- Fast lookup of the cheapest operator for any given phone number
- Unit tests to ensure reliability and correctness

## Project Structure

```
telephone-routing/
├── src/
│   └── telephone_routing/
│       ├── model/
│       ├── repository/
│       └── service/
├── tests/
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/yourusername/telephone-routing.git
$ cd telephone-routing
```

2. Set up a virtual environment (optional but recommended):

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

3. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

4. Run the program

```bash
$ python src/telephone_routing/main.py
```

## Testing

1. Run test using pytest command

```bash
$ pytest -s
```

2. Run coverage report

```bash
$ coverage run -m pytest -s
$ coverage report
```