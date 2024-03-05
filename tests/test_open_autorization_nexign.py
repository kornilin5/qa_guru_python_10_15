import allure
from allure_commons.types import Severity
from qa_guru_python_15.model.authorization_form.authorization import AuthorizationPage

@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Open authorization form')
@allure.link('https://nexign.com/ru', name='Testing')
def test_open_authorization_form():
    authorization = AuthorizationPage()

    with allure.step('Открытие страницы'):
        authorization.open()

    with allure.step('Открытие формы авторизации'):
        authorization.open_authorization_form()

    with allure.step('Проверка формы авторизации'):
        authorization.should_authorization_form()
