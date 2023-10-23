from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

profile = webdriver.FirefoxProfile()
profile.set_preference("intl.accept_languages", "en-US, en")

options = Options()
options.headless = True
options.profile = profile

driver = webdriver.Firefox(options=options)

usernames = []

with open("usernames.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        username = line.split(":")[0].strip()  
        usernames.append(username)

for username in usernames:
    url = f"https://www.op.gg/summoners/na/{username}"
    driver.get(url)
    driver.implicitly_wait(10)

    try:
        level_element = driver.find_element(By.CLASS_NAME, "level")
        level = level_element.text
        print(f"{username}: Level {level}")
    except Exception as e:
        print(f"{username}: Level not found")

driver.quit()
