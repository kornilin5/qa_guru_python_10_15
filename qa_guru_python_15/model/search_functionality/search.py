from selene import browser, have


class SearchPage:

    def open(self):
        browser.open("/")

    def search_element(self):
        browser.element('.header__search').click()
        browser.element('#edit-search-api-fulltext').type(
            'Регистрация').press_enter()

    def should_search_result(self):
        browser.element(
            '[href="/ru/products/crab"] .line-group-search__title').should(
                have.exact_text('CRAB'))
        browser.element(
            '[href="/ru/products/crab"] .line-group-search__description'
        ).should(
            have.text(
                '… Apache Camel). 3. Интеграция систем c продуктом CRAB: '))
