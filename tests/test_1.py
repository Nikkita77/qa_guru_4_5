from selene import browser, have, be


def test_ui_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov@mail.ru')
    browser.element('//*[@id="genterWrapper"]/div[2]/div[1]/label').click()
    browser.element('#userNumber').type(1234567891)
    browser.element('#dateOfBirthInput').clear()

    # browser.element('//*[@id="subjectsContainer"]/div').type('Math')
    browser.element('//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()

    browser.element('#currentAddress').type('Moscow')
    browser.element('//*[@id="state"]/div/div[1]/div[1]').click()
    browser.element('//*[@id="react-select-3-option-1"]').click()
    browser.element('//*[@id="city"]/div/div[1]').click()
    browser.element('//*[@id="react-select-4-option-1"]').click()


    # browser.element('#submit').click()




    # browser.element('#firstName').type('Ivan').press_enter()
