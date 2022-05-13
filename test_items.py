from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_button_on_page(browser):
    browser.get(link)

    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    add_to_basket_button = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")

    assert len(add_to_basket_button) == 1, "The add to cart button is not on the page"
