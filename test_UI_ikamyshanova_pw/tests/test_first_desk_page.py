class TestFirstDeskPage:
    def test_first_desk_page(self, first_desk_page):
        first_desk_page.open()

        first_desk_page.is_contact_us_displayed()
        first_desk_page.is_cart_icon_displayed()

        first_desk_page.check_product_count()
        first_desk_page.check_first_product_name()
