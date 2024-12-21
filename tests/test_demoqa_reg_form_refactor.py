from demoqa_tests.model.page.registration_page import RegistrationPage
import allure


@allure.title('Успешная регистрация')
def test_student_registration_form(setup_browser):
    with allure.step('Открыть форму регистрации'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('Заполнить поле First Name'):
        registration_page.type_first_name('Lucy')

    with allure.step('Заполнить поле Last Name'):
        registration_page.type_last_name('Bechtel')

    with allure.step('Заполнить поле Email'):
        registration_page.type_user_email('aslavret87@gmail.com')

    with allure.step('Выбрать значение для Gender'):
        registration_page.select_gender('[for=gender-radio-2]')

    with allure.step('Заполнить поле Mobile'):
        registration_page.type_user_number('0123456789')

    with allure.step('Заполнить поле Date of Birth'):
        registration_page.select_date_of_birth('[value = "6"]', '[value = "2005"]')

    with allure.step('Заполнить поле Subjects'):
        registration_page.type_subjects('Arts', 'En')

    with allure.step('Выбрать значение для Hobbies'):
        registration_page.select_hobbies('[for=hobbies-checkbox-2]')

    with allure.step('Выбрать файл для Picture'):
        registration_page.upload_picture('original.jpg')

    with allure.step('Заполнить поле Current Address'):
        registration_page.type_current_address('426 Jordy Lodge Cartwrightshire, SC 88120-6700')

    with allure.step('Выбрать значение для State'):
        registration_page.select_state('Haryana')

    with allure.step('Выбрать значение для City'):
        registration_page.select_city('Panipat')

    with allure.step('Нажать на кнопку для отправки формы'):
        registration_page.submit_button_click()

    with allure.step('Проверить результат заполнения формы регистрации'):
        registration_page.should_have_registered(
            [
                'Student Name Lucy Bechtel',
                'Student Email aslavret87@gmail.com',
                'Gender Female',
                'Mobile 0123456789',
                'Date of Birth 20 July,2005',
                'Subjects Arts, English',
                'Hobbies Reading',
                'Picture original.jpg',
                'Address 426 Jordy Lodge Cartwrightshire, SC 88120-6700',
                'State and City Haryana Panipat'
            ]
        )

        registration_page.close_button_click()
