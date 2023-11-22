import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def lambda_handler(event, context):
    try:

        event_parsed = json.loads(event["body"])

        username = event_parsed["username"]
        password = event_parsed["password"]
        url = event_parsed["url"]

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        driver.get(url)
        print(driver.title)

        # username
        username_input_element = driver.find_element("xpath", '//*[@id="login_field"]')
        username_input_element.click()
        username_input_element.clear()
        username_input_element.send_keys(username)

        # password
        username_input_element = driver.find_element("xpath", '//*[@id="password"]')
        username_input_element.click()
        username_input_element.clear()
        username_input_element.send_keys(password)

        # button sing in
        current_url = driver.current_url
        print(current_url)
        print(driver.title)

        element = driver.find_element("xpath", '//*[@id="login"]/div[4]/form/div/input[13]')
        element.click()

        current_url = driver.current_url
        print(current_url)
        print(driver.title)

        driver.close()

        return {"statusCode": 200}

    except:
        return {"message": 400}


if __name__ == '__main__':
    event = {
        "body": json.dumps({
            "username": "username",
            "password": "password",
            "url": "https://github.com/login"
        })
    }

    lambda_handler(event, {})
