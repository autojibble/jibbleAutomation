import logging
import azure.functions as func
from selenium import webdriver

# import requests
# from selenium import webdriver
# # # # import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# # import json
# import requests
# print("Azure Launched") 
# from testAutomation import url 
# def test_func():
# #     result = "Rahoof Khan"
# #     return result



# def connect():

#         chrome_options.add_argument("--window-size=1920,1080")
#         chrome_options.add_argument("--start-maximized")
#         chrome_options.add_argument("--headless=new")
#         browser = webdriver.chrome(options=chrome_options) 
#         browser.get('https://www.jibble.io/app/login')
#         element_email = browser.find_element(By.css_selector, '[data-testid="emailorphone"]').send_keys("" + Keys.enter)
#         element_password = browser.find_element(By.css_selector, '[name="password"]').send_keys("" + Keys.enter)
#         # print("login successful")
#         # time.sleep(5)
#         statement = "login successful"
#         return statement

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()

        except ValueError:
            pass
        else:
            name = req_body.get('name')
             

    if name:
        # result = connect()
        return func.HttpResponse(f"Hello, {name}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
