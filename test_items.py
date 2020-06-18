import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary")
    assert button, "Кнопка не найдена"
