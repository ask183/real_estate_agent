# AI Real Estate Agent (Austin, TX)

Daily filtered property listings emailed to you!

## 🛠️ Setup

1. Install Python packages:

```bash
pip install -r requirements.txt
```

2. Set up `.env` file with your SendGrid SMTP details.

3. Customize `user_filters/filters.json` to your needs.

4. Run manually:

```bash
python3 crew.py
```

5. Run daily automation:

```bash
python scheduler.py
```
