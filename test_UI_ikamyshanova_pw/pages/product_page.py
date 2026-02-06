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

    @allure.step('Get number of products in cart')
    def number_of_products_in_cart(self):
        return self.find_element(self.NOT_EMPTY_CART).text_content()

    @allure.step('Get price of product')
    def get_product_price(self):
        price_element = self.find_element(self.PRICE)
        return price_element.text_content()

    @allure.step('Get name of product')
    def get_product_name(self):
        name_element = self.find_element(self.NAME)
        return name_element.text_content()
