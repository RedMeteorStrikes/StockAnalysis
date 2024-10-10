import yfinance as yf
import time
from datetime import datetime

serial_number = 1

while True:
    stock = yf.Ticker("RELIANCE.NS")
    stock_data = stock.history(period="1d")
    current_price = stock_data['Close'].iloc[0]
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("stock_prices.txt", "a") as file:
        file.write(f"{serial_number}: {current_time}: {current_price:.2f}\n")
    
    print(f"{serial_number}: {current_time}: {current_price:.2f}")
    
    serial_number += 1
    time.sleep(10)
