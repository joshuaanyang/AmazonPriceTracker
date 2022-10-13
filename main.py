import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

apple_mac_url = "https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5M7S6K/ref=sr_1_1?crid=1ASMCUA871M3E&keywords=macbook&qid=1645389223&sprefix=mac%2Caps%2C947&sr=8-1&th=1"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}


response = requests.get(url=apple_mac_url, headers=header)
amazon_link = response.text

soup = BeautifulSoup(amazon_link, "lxml")
order_price = soup.find("span", class_="a-offscreen")
price = float(order_price.getText().split("$")[1])

title = soup.find("span", id="productTitle").getText()
print(title)

email = "youremailaddresshere@gmail.com"
pss = "yourpasswordhere"
X_PRICE = 1000
if X_PRICE > price:
    message = f"{title} is now selling at {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        login_deets = connection.login(user=email, password=pss)
        connection.sendmail(
            from_addr=email,
            to_addrs="email_for_alert_to_be_sent_to",
            msg=f"Subject: Amazon Price Tracker!\n\n{message}\n{apple_mac_url}".encode("utf-8")
        )


