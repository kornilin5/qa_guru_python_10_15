from qa_guru_python_15.model.pages.search_page import SearchPage
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Search functionality')
@allure.link('https://nexign.com/ru', name='Testing')
def test_search_functionality():
    search = SearchPage()

    search.open()

    search.search_element()
    search.should_search_result()
