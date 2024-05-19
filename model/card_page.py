import allure
from selene import browser
from allure import attach
from allure_commons.types import AttachmentType
import requests


class Cart:
    def open_cart(self):
        with allure.step('Open cart'):
            browser.open('/cart')
            return self

    @staticmethod
    def open_cart_with_items(url=None, data=None):
        with allure.step('Open cart with items'):
            result = requests.post(url=url, data=data)
            cookies = result.cookies.get('Nop.customer')
            attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)
            browser.open('https://demowebshop.tricentis.com/cart')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})


add_item_to_cart = Cart()
