from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add2basket_button(browser):
    browser.get(link)
    # sleep(3)
    button = browser.find_elements_by_css_selector("button.btn.btn-add-to-basket")
    assert button, 'Button AddToBasket not found!' # при 0 длине массива тест падает
