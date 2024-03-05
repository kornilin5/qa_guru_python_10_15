from selene import browser, be, have


class AuthorizationPage():

    def open(self):
        browser.open('/')

    def open_authorization_form(self):
        browser.element(
            '.header__client [href="https://nexign.com/ru/personal-accounts"]'
        ).should(be.visible).click()

        browser.all('.event-cards__item-title').element_by(
            have.exact_text('Личный кабинет Nexign Store')).click()

    def should_authorization_form(self):
        browser.element('.block-form').should(
            have.text('Вход в личный кабинет')
        )
        browser.all('#user-login-form').element_by(
            have.exact_texts('Email', 'Пароль'))
