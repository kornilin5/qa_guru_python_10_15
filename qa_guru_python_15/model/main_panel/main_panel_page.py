from selene import browser, have


class Panel():

    def open(self):
        browser.open('/')

    def should_contacts(self):
        browser.element('.menu-item > a[href^="/ru/contact-us"]').click()
        browser.element(
            '.part-world__mail[href^="mailto:office@nexign.com"]').should(
                have.exact_text('office@nexign.com'))

    def should_services(self):
        browser.element(".menu-new > .menu-item:nth-child(2) > span").click()
        browser.all('.active > .menu .menu-item').should(
            have.texts("Комплексное внедрение", "Managed Services",
                       "Техническое сопровождение"))

    def should_about_company(self):
        browser.element(".menu-new > .menu-item:nth-child(4) > span").click()
        browser.all('.active > .menu .menu-item').should(
            have.texts('О Nexign', 'Новости', 'Истории успеха', 'СМИ о нас',
                       'Конференции и выставки', 'Блог', 'Устойчивое развитие',
                       'Годовые отчеты', 'Признание в отрасли',
                       'Сертификаты качества', 'Вид деятельности', 'Вакансии'))

    def should_store(self):
        browser.element('.store > span').click()
        browser.all('.active > .menu .menu-item').should(
            have.texts(
                "Продукты для разработчиков",
                "Личный кабинет",
            ))
