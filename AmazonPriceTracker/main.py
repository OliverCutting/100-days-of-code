from bs4 import BeautifulSoup
import requests
import smtplib
import config

url = 'https://www.amazon.co.uk/Instant-Pot-Multicooker-Sousvides-dehydrates/dp/B08VNPVFWW'
response = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept-Language" : "en-US,en;q=0.9"})
page = response.text
soup = BeautifulSoup(page, 'html.parser')

price = soup.find(name='span', class_='a-offscreen').get_text()
price = float(price[1::])


if price < 150:
    message = "Your tracked item has fell below the target price!"

    with smtplib.SMTP(config.provider, port=587) as connection:
        connection.starttls()
        result = connection.login(config.email, config.password)
        connection.sendmail(
            from_addr=config.email,
            to_addrs=config.email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}")