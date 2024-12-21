from demoqa_tests.model.data_sources import resources
from selene_in_action_py13.conditions import match
from selene import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.element('#genterWrapper')
        self.user_number = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.day_of_birth = browser.element('.react-datepicker__day--020')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element('#hobbiesWrapper')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.close_button = browser.element('#closeLargeModal')

    def open(self):
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def type_first_name(self, value):
        self.first_name.should(match.blank)
        self.first_name.type(value)

    def type_last_name(self, value):
        self.last_name.should(match.blank)
        self.last_name.type(value)

    def type_user_email(self, value):
        self.user_email.should(match.blank)
        self.user_email.type(value)

    def select_gender(self, value):
        self.gender.element(value).click()

    def type_user_number(self, value):
        self.user_number.should(match.blank)
        self.user_number.type(value)

    def select_date_of_birth(self, month, year):
        self.date_of_birth.click()

        self.month_of_birth.click()
        self.month_of_birth.element(month).should(match.text('July')).click()

        self.year_of_birth.click()
        self.year_of_birth.element(year).should(match.text('2005')).click()

        self.day_of_birth.should(match.text('20')).click()

    def type_subjects(self, value1, value2):
        self.subjects.should(match.blank)
        self.subjects.type(value1).press_enter()
        self.subjects.type(value2).press_enter()

    def select_hobbies(self, value):
        self.hobbies.element(value).click()

    def upload_picture(self, value):
        self.picture.set_value(resources.path(value))

    def type_current_address(self, value):
        self.current_address.should(match.blank)
        self.current_address.type(value)

    def select_state(self, value):
        self.state.click()
        self.state.all('#state div').element_by(match.text(value)).click()

    def select_city(self, value):
        self.city.click()
        self.city.all('#city div').element_by(match.text(value)).click()

    def submit_button_click(self):
        self.submit_button.click()

    def should_have_registered(self, text):
        browser.element('#example-modal-sizes-title-lg').should(match.text('Thanks for submitting the form'))
        browser.all('tbody tr').should(match.exact_texts(text))

    def close_button_click(self):
        self.close_button.click()
