## About Notimmy

Notimmy is a small & lightweight software to get binance P2P notifications.

It uses a scheduler to fetch data from binance API and selects the best price for you.

I spend most of my time on the PC, so I did this because I was tired of checking the binance website for a better price.

## Install

- First, you need to have python 3.8 or higher
- run
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Notimmy has set some default env variables

```
COUNTRY="ecuador"
TRADE_TYPE="SELL"
PAYMENT_FILTER=['Produbanco']
```

You can change for your own values, it should work !

## Run

Running the application is very easy, just run the following command in the base path:

```
py main.py
```

For the next update, I plan to configure running this software in the background.

## Tests

To run the tests, execute: `pytest`

## Goals

- Add integrations tests
- Add E2E tests
- Improve README