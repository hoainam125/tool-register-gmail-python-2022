import os
import random
import string
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
driver_path = os.getcwd() + '\chrome_driver\chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
API_KEY = str(input('Type your API KEY. GET API KEY HERE: https://chothuesimcode.com/account/login '))


def get_phone_number():
    API_VALUE = 'https://chothuesimcode.com/api?act=number&apik={}&appId=1005&prefix=097'.format(API_KEY)
    response = requests.get(API_VALUE).json()
    if (response['ResponseCode'] == 0):
        return response['Result']['Id'], response['Result']['Number']


def get_code(id):
    API_VALUE = 'https://chothuesimcode.com/api?act=code&apik={0}&id={1}'.format(API_KEY, id)
    response = requests.get(API_VALUE).json()
    if (response['ResponseCode'] == 0):
        return response['Result']['Code']
    else:
        time.sleep(2)
        return get_code(id)

def reg_account():
        # #
    # create data
    REG_LINK = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
    driver.get(REG_LINK)
    last_name = random.choice(open('names.txt').read().splitlines())
    first_name = random.choice(open('names.txt').read().splitlines())
    user_name = (last_name + first_name[0:3] + str(random.randint(1000, 999999))).lower()
    password = ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + str(random.randint(999, 9999))
    print(password)
    print(user_name)

    # fill the form
    driver.find_element(by=By.XPATH, value='//*[@id="lastName"]').send_keys(last_name)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="firstName"]').send_keys(first_name)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(user_name)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="confirm-passwd"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(random.randint(2, 5))
    # move to next page
    driver.find_element(by=By.XPATH, value='//*[@id="accountDetailsNext"]/div/button/span').click()

    # fill phone number
    phone_number = list(get_phone_number())
    print(phone_number)

    time.sleep(random.randint(2, 5))
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div[2]/div[1]/label/input').send_keys(
        phone_number[1])
    driver.find_element(by=By.XPATH,
                        value='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(random.randint(2, 5))
    code = get_code(phone_number[0])
    print('code:', code)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="code"]').send_keys(
        code)
    time.sleep(2)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="day"]').send_keys(random.randint(1, 29))
    time.sleep(random.randint(1, 3))
    select = Select(driver.find_element(by=By.XPATH,
                                        value='//*[@id="month"]'))
    select.select_by_value(str(random.randint(1, 12)))
    time.sleep(random.randint(1, 3))
    driver.find_element(by=By.XPATH,
                        value='//*[@id="year"]').send_keys(random.randint(1970, 1999))
    select = Select(driver.find_element(by=By.XPATH,
                                        value='//*[@id="gender"]'))
    select.select_by_value(str(random.randint(1, 2)))
    time.sleep(3)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,
                        value='/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/span').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH,
                        value='//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

    # append account info to file
    file_object = open('account.txt', 'a')
    acc_in4 = str('\n' + user_name + '@gmail.com' + '\t' + password + '\t' + phone_number[1] + '\t')
    file_object.write(acc_in4)
    print(acc_in4)
if __name__ == '__main__':

    number_account = int(input('Number of account: ')
    for i in range(number_account):
        reg_account()
   
