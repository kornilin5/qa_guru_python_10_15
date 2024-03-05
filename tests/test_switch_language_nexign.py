from qa_guru_python_15.model.switch_language.switch_language_page import SwitchLanguagePage
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Switch language')
@allure.link('https://nexign.com/ru', name='Testing')
def test_switch_language():
    switche_language = SwitchLanguagePage()

    with allure.step('Открытие страницы'):
        switche_language.open()
    with allure.step('Проверка текущего языка'):
        switche_language.should_current_language()
    with allure.step('Переключение языка'):
        switche_language.switch_language()
    with allure.step('Проверка нового языка'):
        switche_language.should_change_language()
