import pytest
from playwright.sync_api import BrowserContext

from test_UI_ikamyshanova_pw.pages.cart_page import CartPage
from test_UI_ikamyshanova_pw.pages.first_desk_page import FirstDeskPage
from test_UI_ikamyshanova_pw.pages.product_page import ProductPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Настройка прокси сервера для доступа к сайту из РФ"""
    return {
        **browser_context_args,
        "proxy": {
            "server": "http://14.143.222.113:10168"
        },
        "viewport": {'width': 1920, 'height': 1080}
    }


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    return page


@pytest.fixture()
def cart_page(page):
    return CartPage(page)


@pytest.fixture()
def product_page(page):
    return ProductPage(page)


@pytest.fixture()
def first_desk_page(page):
    return FirstDeskPage(page)
