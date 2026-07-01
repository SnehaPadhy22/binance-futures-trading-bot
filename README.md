# Binance Futures Testnet Trading Bot

A Python-based CLI Trading Bot that places BUY and SELL orders on the Binance Futures Testnet (USDT-M). The application supports Market and Limit orders, validates user input, logs API requests/responses, and handles errors gracefully.

---

## Features

- Place Market Orders
- Place Limit Orders
- Supports BUY and SELL operations
- Command Line Interface (CLI)
- Input Validation
- API Request & Response Logging
- Error Handling
- Binance Futures Testnet Integration

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── cli.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.10+
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret Key

---

## Installation

### Clone Repository

```bash
git clone <https://github.com/SnehaPadhy22/binance-futures-trading-bot.git>
cd trading_bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Open `bot/client.py` and configure your Binance Testnet credentials:

```python
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
```

Testnet URL:

```python
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
```

---

## Running the Application

### Place a Market Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

Example:

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### Place a Limit Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

Example:

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000
```

---

## Sample Output

```text
===== ORDER SUMMARY =====
Symbol: BTCUSDT
Side: BUY
Type: LIMIT
Quantity: 0.001

===== ORDER RESPONSE =====
Order ID     : 18255687287
Status       : NEW
Executed Qty : 0.0000
Avg Price    : N/A

SUCCESS
```

---

## Logging

All API requests, responses, and errors are stored in:

```text
logs/trading_bot.log
```

Example:

```text
MARKET ORDER REQUEST: symbol=BTCUSDT, side=BUY, quantity=0.001

MARKET ORDER RESPONSE:
{'orderId': 18255632552, ...}

LIMIT ORDER REQUEST:
symbol=BTCUSDT, side=BUY, quantity=0.001, price=50000

LIMIT ORDER RESPONSE:
{'orderId': 18255687287, ...}
```

---

## Validation

The application validates:

- Order Side (BUY/SELL)
- Order Type (MARKET/LIMIT)
- Quantity > 0
- Price required for LIMIT orders

---

## Error Handling

The application handles:

- Invalid order side
- Invalid order type
- Missing limit order price
- API exceptions
- Network failures
- Invalid user inputs

---

## Assumptions

- Binance Futures Testnet account is active.
- API credentials are valid.
- BTCUSDT is used for testing examples.
- Internet connection is available during execution.

---

## Technologies Used

- Python 3
- python-binance
- argparse
- logging

---

## Author

Sneha Padhy