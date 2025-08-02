import csv
from datetime import datetime

# Hardcoded stock prices
prices = {"AAPL": 180, "TSLA": 250, "MSFT": 320}
symbols = ["AAPL", "TSLA", "MSFT"]

# Collect user input for quantities
portfolio = {}
for symbol in symbols:
    qty = int(input(f"Enter quantity for {symbol}: "))
    portfolio[symbol] = qty

# Calculate total investment
total_investment = sum(prices[symbol] * qty for symbol, qty in portfolio.items())
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Prepare data row
result_row = [timestamp] + [portfolio[symbol] for symbol in symbols] + [total_investment]

# Save to CSV (append mode)
csv_filename = "portfolio_tracker.csv"
header = ["Timestamp"] + symbols + ["Total Investment"]
try:
    with open(csv_filename, "x", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
except FileExistsError:
    pass  # File already exists, don't rewrite header

with open(csv_filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(result_row)

# Save to TXT (append mode)
txt_filename = "portfolio_tracker.txt"
with open(txt_filename, "a") as txtfile:
    txtfile.write(f"{timestamp} | "
                  + " | ".join([f"{symbol}: {portfolio[symbol]}" for symbol in symbols])
                  + f" | Total: {total_investment}\n")

print(f"Total investment value: ${total_investment}")
print("Results saved to portfolio_tracker.csv and portfolio_tracker.txt")