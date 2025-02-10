import smtplib
import time
import yfinance as yf

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email notification.
    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body/content of the email
    """
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, recipient_email, message)
        print("Notification email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def get_stock_price(ticker):
    """
    Fetches the current stock price for a given ticker symbol.
    :param ticker: Stock ticker symbol (e.g., 'AAPL' for Apple)
    :return: Current stock price
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")
    return data['Close'].iloc[-1]

def monitor_stock(ticker, threshold, sender_email, sender_password, recipient_email):
    """
    Monitors the stock price and sends an email notification when it crosses the threshold.
    :param ticker: Stock ticker symbol
    :param threshold: Price threshold for notification
    :param sender_email: Email address of the sender
    :param sender_password: Password for the sender's email account
    :param recipient_email: Email address of the recipient
    """
    while True:
        try:
            price = get_stock_price(ticker)
            print(f"Current price of {ticker}: ${price:.2f}")
            if price >= threshold:
                subject = f"Stock Alert: {ticker} Price Above Threshold"
                body = f"The price of {ticker} is now ${price:.2f}, which is above your threshold of ${threshold:.2f}."
                send_email(sender_email, sender_password, recipient_email, subject, body)
                break  # Stop monitoring after sending the notification
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    # Get user input
    ticker = input("Enter the stock ticker symbol (e.g., AAPL): ").strip().upper()
    threshold = float(input("Enter the price threshold for notification: "))
    sender_email = input("Enter your email address: ").strip()
    sender_password = input("Enter your email password: ").strip()
    recipient_email = input("Enter the recipient's email address: ").strip()

    # Monitor the stock price
    print(f"Monitoring {ticker} for price above ${threshold:.2f}...")
    monitor_stock(ticker, threshold, sender_email, sender_password, recipient_email)