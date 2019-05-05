# InstaBot
A bot that emulates an Instagram User liking a post on another account.

## How to Run

1. Make sure you have python installed
2. Install dependencies from requirements.txt `pip install -r requirements.txt`
3. Setup selenium web driver:
   1. Choose the driver based on your choice of Web Browser:
       - Chrome: [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
       - Edge: [WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
       - Firefox: [Geckodriver](https://github.com/mozilla/geckodriver/releases)
       - Safari: [WebDriver](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
   2. Copy and paste the executable into the `Instabot/src/` directory
4. Open a console window (bash, powershell, cmd, etc) 
5. Change cwd(current working directory) to `Instabot/src/`
6. Run `python3 Instabot.py`
7. Enter your Instagram Credentials as prompted
8. Enter the username/handle of the account whose post you want the bot to like.
9. Now watch it do this.
**NOTE:** _it pauses for 3 to 5 seconds between each consecutive action for page to complete it's response._

_**Warning:**_ **This script may stop working over time when instagram makes some changes to the elements which are being utilised in this script and if this script isn't updated with those changes**