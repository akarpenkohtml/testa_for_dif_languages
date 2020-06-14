import time

class TestPages():
    def test_in(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        add_button = browser.find_element_by_css_selector('.btn-add-to-basket')
        time.sleep(1)
        assert add_button, "No add to cart button at this page!"
