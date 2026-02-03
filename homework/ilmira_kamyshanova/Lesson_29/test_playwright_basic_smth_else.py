import pytest
from playwright.sync_api import Page, expect, BrowserContext


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Настройка прокси сервера для доступа к сайту из РФ"""
    return {
        **browser_context_args,
        "proxy": {
            "server": "http://167.88.161.13:7777"
        }
    }


def test_qa_practice_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    result = page.locator('#result-text')
    expect(result).not_to_be_visible()
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role('link', name='Click').click()
    expect(result).to_be_visible()
    expect(result).to_have_text('Ok')


def test_qa_practice_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        click_button.click()
    new_tab = new_page_event.value
    result = new_tab.locator('#result-text')
    expect(result).to_be_visible()
    expect(result).to_have_text('I am a new page in a new tab')
    page.bring_to_front()
    expect(click_button).to_be_enabled()


def test_demo_qa_red_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', wait_until="domcontentloaded")
    red_button = page.locator('#colorChange')
    expect(red_button).to_be_enabled()
    expect(red_button).to_have_css('color', 'rgb(220, 53, 69)', timeout=7000)
    red_button.click()
