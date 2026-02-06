class TestProductPage:
    def test_product_page(self, product_page):
        product_page.open()

        product_page.is_contact_us_displayed()
        assert product_page.get_product_name() == 'Office Design Software'
        assert product_page.get_product_price() == '280.00'

        product_page.add_to_cart()

        product_page.is_cart_not_empty()
        assert product_page.number_of_products_in_cart() == 1
