from qa_guru_python_15.model.search_functionality.search import SearchPage
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Search functionality')
@allure.link('https://nexign.com/ru', name='Testing')
def test_search_functionality():
    search = SearchPage()

    with allure.step('Открытие страницы'):
        search.open()

    with allure.step('Поиск элемента'):
        search.search_element()

    with allure.step('Проверка результата поиска'):
        search.should_search_result()
