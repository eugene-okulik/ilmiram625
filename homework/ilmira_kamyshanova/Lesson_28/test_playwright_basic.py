from playwright.sync_api import Page, expect


def test_internet_heroku_app(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('tomsmith')
    page.get_by_role('textbox', name='Password').fill('SuperSecretPassword!')
    page.get_by_role('button').click()
    secret_area = page.get_by_role('heading', name='Welcome to the Secure Area.')
    expect(secret_area).to_be_enabled()


def test_demo_qa(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', wait_until="domcontentloaded")
    page.get_by_role('textbox', name='First Name').fill('Kate')
    page.get_by_role('textbox', name='Last Name').fill('Well')
    page.get_by_role('textbox', name='name@example.com').fill('kate_well@test.test')
    page.get_by_text('Female').click()
    page.get_by_role('textbox', name='Mobile Number').fill('1234456778')
    page.locator('#dateOfBirthInput').fill('28 Jan 2000')
    page.locator('#subjectsInput').fill('math')
    page.get_by_text('Maths', exact=True).click()
    page.locator('#subjectsInput').fill('g')
    page.get_by_text('Biology', exact=True).click()
    page.locator('#subjectsInput').fill('en')
    page.get_by_text('English', exact=True).click()
    page.get_by_text('Sports').click()
    page.get_by_role('textbox', name='Current Address').fill('Russia')
    page.locator('#state > .css-yk16xz-control > .css-1wy0on6 > .css-tlfecz-indicatorContainer').click()
    page.get_by_text('Uttar Pradesh', exact=True).click()
    page.locator('#city > .css-yk16xz-control > .css-1wy0on6 > .css-tlfecz-indicatorContainer > .css-19bqh2r').click()
    page.get_by_text('Lucknow', exact=True).click()
    page.get_by_role('button', name='Submit').click()
    expect(page.locator('#example-modal-sizes-title-lg')).to_contain_text('Thanks for submitting the form')
