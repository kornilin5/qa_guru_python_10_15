from selene import browser, have
import allure


class PanelPage:

    with allure.step('Открытие страницы'):

        def open(self):
            browser.open('/')

    with allure.step('Проверка раздела контактов'):

        def should_contacts(self):
            browser.element('.menu-item > a[href^="/ru/contact-us"]').click()
            browser.element(
                '.part-world__mail[href^="mailto:office@nexign.com"]').should(
                    have.exact_text('office@nexign.com'))

    with allure.step('Проверка раздела услуг'):

        def should_services(self):
            browser.element(
                ".menu-new > .menu-item:nth-child(2) > span").click()
            browser.all('.active > .menu .menu-item').should(
                have.texts("Комплексное внедрение", "Managed Services",
                           "Техническое сопровождение"))

    with allure.step('Проверка раздела о компании'):

        def should_about_company(self):
            browser.all('.header__navigation .menu-new>li>span').element_by(
                have.exact_text('О компании')).click()
            browser.all('.active .menu .menu-item').should(
                have.texts('О Nexign', 'Новости', 'Истории успеха',
                           'СМИ о нас', 'Конференции и выставки', 'Блог',
                           'Устойчивое развитие', 'Годовые отчеты',
                           'Признание в отрасли', 'Сертификаты качества',
                           'Вид деятельности', 'Вакансии'))

    with allure.step('Проверка раздела store'):

        def should_store(self):
            browser.element('.store > span').click()
            browser.all('.active > .menu .menu-item').should(
                have.texts(
                    "Продукты для разработчиков",
                    "Личный кабинет",
                ))
