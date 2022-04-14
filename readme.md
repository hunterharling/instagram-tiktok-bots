## Py Social Bots
- Includes mass unfollow for Instagram

# To run:
- Get gecko driver (and put it in python folder).
- Create virtualenv and clone repo: https://github.com/mozilla/geckodriver/releases

```bash
virtualenv py-bot && cd py-bot
git clone https://github.com/HunterHarling/py-social-bots
cd py-social-bots
cd scrips && activate && cd ..```

Install requirements
```bash
pip install -r requirements.txt
```

Create a credentials.py and enter passwords/usernames/etc

Finally, run the scripts:
```bash
python insta.py
python tiktok.py
```

NOTE: tiktok.py cannot bypass TikTok's reCaptcha screen. See: https://stackoverflow.com/questions/62721327/how-to-bypass-recaptcha-with-buster-extension-using-selenium-and-python 
and https://medium.com/analytics-vidhya/how-to-bypass-recaptcha-v3-with-selenium-python-7e71c1b680fc 
for potential solutions.