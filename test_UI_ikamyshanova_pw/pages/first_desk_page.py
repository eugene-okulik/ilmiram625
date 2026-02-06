import allure
from playwright.sync_api import expect

from test_UI_ikamyshanova_pw.pages.base_page import BasePage


class FirstDeskPage(BasePage):
    PAGE_URL = '/shop/category/desks-1'
    PRODUCTS = '.o_wsale_products_item_title.mb-2'
    FIRST_PRODUCT = "a:has-text('Customizable Desk')"
    CART_ICON = "a[aria-label='eCommerce cart']"

    @allure.step('Count products in the page')
    def get_product_count(self):
        products = self.find_element(self.PRODUCTS)
        return len(products)

    def select_first_product_name(self):
        return self.find_element(self.FIRST_PRODUCT).text_content()

    @allure.step('Check of visibility Cart icon')
    def is_cart_icon_displayed(self):
        expect(self.find_element(self.CART_ICON)).to_be_visible()
