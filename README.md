# Simplified Trading Bot (Binance Futures Demo)

## Overview

This project is a Python-based trading bot that allows users to place BUY and SELL orders on Binance Futures Demo using a CLI.

## Features

* Supports MARKET and LIMIT orders
* Accepts user input via CLI
* Connects to Binance API
* Displays order details and status

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Add your API keys in config.py:
   API_KEY = "your_api_key"
   API_SECRET = "your_secret_key"
   BASE_URL = "https://demo-fapi.binance.com"

## Run

python main.py

## Example Input

BTCUSDT, BUY, MARKET, 0.001

## Output

Displays order ID, status, executed quantity, and price

## Note

This project uses Binance Demo environment (no real money)
