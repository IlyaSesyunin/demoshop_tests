import allure
from selene import browser, have
from model.card_page import add_item_to_cart

url_add_to_card = 'https://demowebshop.tricentis.com/addproducttocart/details'


def test_add_jewerly_to_cart():
    with allure.step('Add book to cart'):
        add_item_to_cart.open_cart_with_items(
            url=f'{url_add_to_card}/14/1')
    browser.open('/')
    with allure.step('Open cart with jewerly'):
        add_item_to_cart.open_cart()

    browser.element('.product-name').should(have.text('Black & White Diamond Heart'))
    browser.element('.product-subtotal').should(have.text('130.00'))
    browser.element('.product-unit-price').should(have.text('130.00'))


def test_add_book_to_cart():
    with allure.step('Add book to cart'):
        add_item_to_cart.open_cart_with_items(
            url=f'{url_add_to_card}/22/1')
    browser.open('/')
    with allure.step('Open cart with book'):
        add_item_to_cart.open_cart()

    browser.element('.product-name').should(have.text('Health Book'))
    browser.element('.product-subtotal').should(have.text('10.00'))
    browser.element('.product-unit-price').should(have.text('10.00'))
