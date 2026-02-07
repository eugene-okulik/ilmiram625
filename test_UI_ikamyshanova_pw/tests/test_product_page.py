class TestProductPage:
    def test_product_page(self, product_page):
        product_page.open()

        product_page.is_contact_us_displayed()
        product_page.check_product_name()
        product_page.check_product_price()

        product_page.add_to_cart()

        product_page.is_cart_not_empty()
        product_page.check_number_of_products_in_cart()
