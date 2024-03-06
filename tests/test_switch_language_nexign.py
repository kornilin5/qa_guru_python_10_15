from qa_guru_python_15.model.pages.switch_language_page import SwitchLanguagePage
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Switch language')
@allure.link('https://nexign.com/ru', name='Testing')
def test_switch_language():
    switche_language = SwitchLanguagePage()

    switche_language.open()

    switche_language.should_current_language()
    switche_language.switch_language()
    switche_language.should_change_language()
