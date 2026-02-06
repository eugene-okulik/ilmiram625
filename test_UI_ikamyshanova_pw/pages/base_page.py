from playwright.sync_api import Page, expect
import allure


class BasePage:
    CONTACT_US = 'a[href="/contactus"]'
    BASE_PAGE = 'http://testshop.qa-practice.com'
    PAGE_URL = ''

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open(self):
        self.page.goto(f'{self.BASE_PAGE}{self.PAGE_URL}', timeout=60000)

    @allure.step('Find element by locator')
    def find_element(self, locator):
        return self.page.locator(locator)

    @allure.step('Check "Contact us" text')
    def is_contact_us_displayed(self):
        contact_us = self.find_element(self.CONTACT_US)
        expect(contact_us).to_be_visible()
        expect(contact_us).to_have_text('Contact Us')
