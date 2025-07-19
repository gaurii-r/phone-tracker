# 📱 Phone Tracker (Python Project)

A simple command-line tool to track phone number information including:

- 📍 Region (State/Province)
- 📶 SIM Card Provider
- 🌍 Latitude & Longitude
- 🏠 Street Address, City, and Postal Code

This project uses:
- [`phonenumbers`](https://pypi.org/project/phonenumbers/) – to parse and extract region and carrier info
- [`opencage`](https://opencagedata.com/) – to get address details from coordinates

---

## ⚙️ Requirements

Install the required packages using:

```bash
pip install -r requirements.txt

🚀 How to Run
Clone this repo:

git clone https://github.com/gaurii-r/phone-tracker.git
cd phone-tracker
Set your OpenCage API key in phone_tracker.py

api_key = 'YOUR_OPENCAGE_API_KEY'

python phone_tracker.py
