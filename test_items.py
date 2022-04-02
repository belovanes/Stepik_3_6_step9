from time import sleep

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add2basket_button(browser):
    browser.get(link)
    sleep(3)
    assert browser.find_element_by_css_selector("button.btn.btn-add-to-basket")
