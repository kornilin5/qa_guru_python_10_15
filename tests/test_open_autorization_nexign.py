import allure
from allure_commons.types import Severity
from qa_guru_python_15.model.pages.authorization_page import AuthorizationPage


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Open authorization form')
@allure.link('https://nexign.com/ru', name='Testing')
def test_open_authorization_form():
    authorization = AuthorizationPage()

    authorization.open()

    authorization.open_authorization_form()
    authorization.should_authorization_form()
