class TestFirstDeskPage:
    def test_first_desk_page(self, first_desk_page):
        first_desk_page.open()

        first_desk_page.is_contact_us_displayed()
        first_desk_page.is_cart_icon_displayed()

        assert first_desk_page.get_product_count() == 9
        assert first_desk_page.select_first_product_name() == 'Customizable Desk'
