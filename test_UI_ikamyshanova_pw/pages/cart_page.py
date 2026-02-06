import allure
from playwright.sync_api import expect

from test_UI_ikamyshanova_pw.pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_URL = '/shop/cart'
    ORDER_OVERVIEW = '.mb-4'
    EMPTY_CART = '.js_cart_lines.alert.alert-info'
    REVIEW_ORDER = "p:has-text('Review Order')"
    SHIPPING = "p:has-text('Shipping')"
    PAYMENT = "p:has-text('Payment')"
    REMOVE = "a.js_delete_product[title='Remove from cart']"
    CHECKOUT = "a[name='website_sale_main_button']:has-text('Checkout')"

    @allure.step('Clear cart')
    def remove_items(self):
        remove_buttons = self.find_element(self.REMOVE)
        for remove_button in remove_buttons:
            remove_button.click()

    @allure.step('Check of visibility Checkout button')
    def is_checkout_button_visible(self):
        expect(self.find_element(self.CHECKOUT)).to_be_visible()

    @allure.step('Check for empty cart')
    def is_cart_to_be_empty(self):
        expect(self.find_element(self.EMPTY_CART)).to_have_text('Your cart is empty!')
        expect(self.find_element(self.ORDER_OVERVIEW)).to_have_text('Order overview')

