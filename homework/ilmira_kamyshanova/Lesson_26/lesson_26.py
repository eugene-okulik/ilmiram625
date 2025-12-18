from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(40)
    chrome_driver.maximize_window()
    yield chrome_driver
    sleep(3)


def test_item_in_cart_new_tab(driver):
    driver.get('http://testshop.qa-practice.com')
    wait = WebDriverWait(driver, 100)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="text-primary text-decoration-none"]')))
    chosen_item = driver.find_element(By.CSS_SELECTOR, 'a[class="text-primary text-decoration-none"]')
    chosen_item.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.ENTER)
    chosen_item_text = chosen_item.text
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="btn btn-secondary"]'))).click()
    sleep(3)
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, 'a[aria-label="eCommerce cart"]').click()
    item_in_cart = driver.find_element(By.CSS_SELECTOR, 'h6[class="d-inline align-top h6 fw-bold"]')
    assert chosen_item_text in item_in_cart.text


def test_item_in_cart(driver):
    driver.get('http://testshop.qa-practice.com')
    wait = WebDriverWait(driver, 100)
    actions = ActionChains(driver)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="Customizable Desk"]')))
    chosen_item = driver.find_element(By.CSS_SELECTOR, 'a[class="btn btn-primary a-submit"]')
    sleep(2)
    actions.move_to_element(chosen_item).perform()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[class="btn btn-primary a-submit"]'))).click()
    item_in_cart = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'strong.product-name.product_display_name')))
    sleep(3)
    assert chosen_item.text in item_in_cart.text
