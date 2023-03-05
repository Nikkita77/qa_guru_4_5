from selene import browser, have, be


def test_ui_form():


    browser.open('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()