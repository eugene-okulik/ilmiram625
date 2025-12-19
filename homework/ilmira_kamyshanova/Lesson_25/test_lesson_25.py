import os
import random

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    print(chrome_driver.title)
    print(chrome_driver.current_url)
    print('________________________END OF TEST____________________________')


def test_text_on_page(driver):
    link = 'https://www.qa-practice.com/elements/input/simple'

    driver.get(link)
    search_input = driver.find_element(By.NAME, 'text_string')
    input_text = 'Hi'
    search_input.send_keys(input_text)
    search_input.submit()

    search_output = driver.find_element(By.ID, 'result-text')
    print(f'My text in input was "{search_output.text}"')
    assert search_output.text == input_text, 'Texts are not equal!'
    driver.quit()


def test_fill_the_form(driver):
    link = 'https://demoqa.com/automation-practice-form'
    faker = Faker()
    file_name = 'for selenium.jpg'
    file_path = os.path.abspath(file_name)

    driver.get(link)
    driver.find_element(By.ID, 'firstName').send_keys(faker.first_name_female())
    driver.find_element(By.ID, 'lastName').send_keys(faker.last_name_female())
    driver.find_element(By.ID, 'userEmail').send_keys(faker.email())

    driver.execute_script("window.scrollBy(0, 100);")
    driver.find_element(By.CLASS_NAME, 'custom-control-label').click()
    driver.find_element(By.ID, 'userNumber').send_keys(faker.random_int(1000000000, 9999999999))
    driver.find_element(By.ID, 'dateOfBirthInput').send_keys(Keys.CONTROL + 'a')
    driver.find_element(By.ID, 'dateOfBirthInput').send_keys(faker.date_of_birth().strftime('%d %b %Y'))
    driver.find_element(By.CLASS_NAME, 'react-datepicker__day--selected').click()
    subject = driver.find_element(By.ID, 'subjectsInput')
    subject.send_keys(random.choice('abcdefghijklmnopqrstuvwxyz'))
    subject.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollBy(0, 200);")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']"))).click()
    driver.find_element(By.ID, 'uploadPicture').send_keys(file_path)
    driver.find_element(By.ID, 'currentAddress').send_keys(faker.address())

    driver.find_element(By.ID, 'submit').click()

    result_table = driver.find_element(By.CSS_SELECTOR,
                                       'table[class="table table-dark table-striped table-bordered table-hover"]')
    print(result_table.text)
    assert result_table


def test_single_select(driver):
    link = 'https://www.qa-practice.com/elements/select/single_select'
    language = 'C#'

    driver.get(link)
    select = driver.find_element(By.CLASS_NAME, 'form-select')
    dropdown = Select(select)
    dropdown.select_by_value(language)
    driver.find_element(By.NAME, 'submit').click()

    result = driver.find_element(By.ID, 'result-text')
    assert result.text == language
    driver.quit()


def test_start_buttom(driver):
    link = 'https://the-internet.herokuapp.com/dynamic_loading/2'

    driver.get(link)
    driver.find_element(By.TAG_NAME, 'button').click()

    wait = WebDriverWait(driver, 20)
    search_output = wait.until(EC.presence_of_element_located((By.ID, 'finish')))
    print(f'Output text: "{search_output.text}"')
    assert search_output.text == 'Hello World!', 'Texts are not equal!'
    driver.quit()
