from selene import browser, have, be
import os


def test_form_submit_checker():
    browser.open("/automation-practice-form")
    browser.should(have.title_containing('DEMOQA'))

    # WHEN

    browser.element('#firstName').should(be.blank)
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('ivanov@mail.com')
    browser.all('[for*=gender-radio]').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('8925239563')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('June')
    browser.element('.react-datepicker__year-select').type('1988')
    browser.element('.react-datepicker__day--001').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("tests/resources/1.jpeg"))
    browser.element('#currentAddress').type('Leskova street,8')
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#subjectsInput').type('English').press_enter()

    browser.element('#submit').press_enter()

    # THEN

    browser.all('tbody tr td:last-child').should(have.exact_texts('Ivan Ivanov',
                                                                  'ivanov@mail.com', 'Male', '8925239563',
                                                                  '01 June,1988',
                                                                  'English',
                                                                  'Reading', '1.jpeg', 'Leskova street,8',
                                                                  'Uttar Pradesh Agra'))
