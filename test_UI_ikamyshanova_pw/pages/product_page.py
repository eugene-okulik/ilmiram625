import allure
from playwright.sync_api import expect
from test_UI_ikamyshanova_pw.pages.base_page import BasePage


class ProductPage(BasePage):
    PAGE_URL = '/shop/furn-9999-office-design-software-7?category=9'
    ADD_TO_CART = '#add_to_cart'
    NAME = 'h1[itemprop="name"]'
    PRICE = 'span.oe_currency_value'
    NOT_EMPTY_CART = 'sup.my_cart_quantity.badge.text-bg-primary'
    CART = 'a[aria-label="eCommerce cart"]'

    @allure.step('Add product to cart')
    def add_to_cart(self):
        self.find_element(self.ADD_TO_CART).click()

    @allure.step('Open cart')
    def go_to_cart(self):
        self.find_element(self.CART).click()

    @allure.step('Open page')
    def is_cart_not_empty(self):
        expect(self.find_element(self.NOT_EMPTY_CART)).to_be_visible()

    @allure.step('Check number of products in cart')
    def check_number_of_products_in_cart(self):
        expect(self.find_element(self.NOT_EMPTY_CART)).to_have_text('1')

    @allure.step('Check price of product')
    def check_product_price(self):
        expect(self.find_element(self.PRICE)).to_have_text('280.00')

    @allure.step('Check name of product')
    def check_product_name(self):
        expect(self.find_element(self.NAME)).to_have_text('Office Design Software')
