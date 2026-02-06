class TestCartPage:
    def test_cart_page(self, cart_page, product_page):
        cart_page.open()
        cart_page.is_checkout_button_visible()
        cart_page.is_cart_to_be_empty()

        product_page.open()
        product_page.add_to_cart()
        product_page.is_cart_not_empty()

        cart_page.remove_items()

        cart_page.is_cart_to_be_empty()

