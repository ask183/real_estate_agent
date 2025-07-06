import os
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv

load_dotenv()

def send_email(listings, user_email):
    if not listings:
        print("No listings to email.")
        return

    html = "<h2>🏡 Today's Listings</h2><ul>"
    for l in listings:
        html += f"<li><b>${l['price']}</b> | {l['beds']} beds, {l['baths']} baths | {l['sqft']} sqft - <a href='{l['link']}'>View</a></li>"
    html += "</ul>"

    msg = MIMEText(html, 'html')
    msg['Subject'] = "🏠 Daily Real Estate Listings - Austin"
    msg['From'] = os.getenv('FROM_EMAIL')
    msg['To'] = user_email

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        print("✅ Email sent successfully.")