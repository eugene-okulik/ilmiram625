import allure
from playwright.sync_api import expect

from test_UI_ikamyshanova_pw.pages.base_page import BasePage


class FirstDeskPage(BasePage):
    PAGE_URL = '/shop/category/desks-1'
    PRODUCTS = '.o_wsale_products_item_title.mb-2'
    FIRST_PRODUCT = "a:has-text('Customizable Desk')"
    CART_ICON = "a[aria-label='eCommerce cart']"

    @allure.step('Check count products in the page')
    def check_product_count(self):
        expect(self.find_element(self.PRODUCTS)).to_have_count(9)

    @allure.step('Check first product name')
    def check_first_product_name(self):
        expect(self.find_element(self.FIRST_PRODUCT)).to_have_text('Customizable Desk')

    @allure.step('Check of visibility Cart icon')
    def is_cart_icon_displayed(self):
        expect(self.find_element(self.CART_ICON)).to_be_visible()
