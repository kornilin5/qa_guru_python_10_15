from selene import browser, query, have
import allure


class SwitchLanguagePage:
    CURRENT_LANGUAGE: str
    NEW_LANGUAGE: str

    with allure.step('Открытие страницы'):

        def open(self):
            browser.open('/')

    with allure.step('Проверка текущего языка'):

        def should_current_language(self):
            self.CURRENT_LANGUAGE = browser.element(
                '.header__language .language').get(query.text)

    with allure.step('Переключение языка'):

        def switch_language(self):
            if self.CURRENT_LANGUAGE == 'RUS':
                browser.element('.header__language .language').click()
                browser.element('.language_white .language-link').click()
                self.NEW_LANGUAGE = self.should_current_language()
            elif self.CURRENT_LANGUAGE == 'ENG':
                browser.element('.header__language .language').click()
                browser.element('.language_white .language-link').click()
                self.NEW_LANGUAGE = self.should_current_language()
            else:
                raise ValueError('Wrong language')

    with allure.step('Проверка нового языка'):

        def should_change_language(self):
            assert self.CURRENT_LANGUAGE != self.NEW_LANGUAGE

            if self.NEW_LANGUAGE == 'RUS':
                browser.element('.welcome-banner__content-title').should(
                    have.exact_texts('Расширяем', 'возможности'))
            elif self.NEW_LANGUAGE == 'ENG':
                browser.element('.welcome-banner__content-title').should(
                    have.exact_texts('Empower', 'Change'))
                assert self.NEW_LANGUAGE == 'RUS'
