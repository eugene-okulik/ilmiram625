import json
from playwright.sync_api import Page, expect, Route


def test_apple_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['productName'] = 'яблокофон 17 про'
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 17 про'
        body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = 'яблокофон 17 про'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/step0_iphone**', handle_route)

    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-content-title').locator('nth=0').click()
    product_title = page.locator('.rf-digitalmat-overlay-header.typography-manifesto').locator('nth=0')
    expect(product_title).to_have_text('яблокофон 17 про')
