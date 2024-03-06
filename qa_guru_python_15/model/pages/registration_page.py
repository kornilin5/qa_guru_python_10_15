from selene import browser, be, have
import allure


class RegistrationPage:

    with allure.step('Открытие страницы'):

        def open(self):
            browser.open('/')

    with allure.step('Открытие формы регистрации'):

        def open_registration_form(self):
            browser.element(
                '.header__client [href="https://nexign.com/ru/personal-accounts"]'
            ).should(be.visible).click()

            browser.all('.event-cards__item-title').element_by(
                have.exact_text('Личный кабинет Nexign Store')).click()

            browser.element('#edit-create-account').click()

            browser.element('[for^=edit-field-type-fiz]').click()
            browser.element('#edit-next').click()
            browser.element('.block-registration h2').should(
                have.exact_text('Регистрация в личном кабинете'))

    with allure.step('Проверка обязательных полей'):

        def should_required_items(self):
            browser.all('.js-form-required').should(
                have.texts('ФИО (полностью) *', 'Email *', 'Номер телефона *',
                           'Даю согласие на обработку персональных данных *',
                           'Какой код на картинке?'))
