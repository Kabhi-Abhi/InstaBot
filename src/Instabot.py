from selenium import webdriver
import time
from getpass import getpass

user = input("Enter your Instagram username/handle: ")
pswd = getpass("Enter your password (Correctly or it'll crash after openning the browser): ")
hndl = input("Enter instagram handle of account to like a post on: ")

chrome = webdriver.Chrome('./chromedriver.exe')
chrome.get('https://www.instagram.com')
time.sleep(5)

login_button = chrome.find_element_by_xpath("//span[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
login_button.click()
time.sleep(5)

username = chrome.find_element_by_class_name('_2hvTZ ')
username.send_keys(user)

password_field = chrome.find_element_by_name('password')
password_field.send_keys(pswd)

login = chrome.find_element_by_class_name('L3NKy       ')
login.click()
time.sleep(10)

# Decline Desktop Notifications, comment out if allowed
decline = chrome.find_elements_by_class_name('aOOlW         ')[1]
decline.click()

search_field = chrome.find_element_by_class_name(' wUAXj')
search_field.click()

# Change the string to someone's Instagram username
chrome.find_element_by_class_name('XTCLo       ').send_keys(hndl)
time.sleep(5)

# clicks on first result
profile = chrome.find_elements_by_class_name('yCE8d  ')[0]
profile.click()

# Wait for profile to load, increase time if on slow connection
time.sleep(5)

# Open First Media on the profile
media = chrome.find_element_by_class_name('v1Nh3             ')
media.click()
time.sleep(5)

# Like it
like = chrome.find_element_by_class_name('            coreSpriteHeartOpen       ')
#like = chrome.find_element_by_class_name('dCJp8 afkep coreSpriteHeartOpen _0mzm-')
like.click()
time.sleep(5)

# Change the media
next_media = chrome.find_element_by_class_name('      coreSpriteRightPaginationArrow')
next_media.click()
time.sleep(8)

# Finish up
# Close Media View
close = chrome.find_element_by_class_name('ckWGn')
close.click()

# Open Logged In profile
user = chrome.find_elements_by_class_name('XrOey')[2]
user.click()
time.sleep(5)

# logout
settings = chrome.find_element_by_class_name('AFWDX')
settings.click()
time.sleep(5)

logout = chrome.find_elements_by_class_name('aOOlW         ')[5]
logout.click()

chrome.delete_all_cookies()
chrome.close()
