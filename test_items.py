from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button is not None, 'Нельзя добавить в корзину! Ошибка!'