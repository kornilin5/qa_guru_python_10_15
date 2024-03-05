from qa_guru_python_15.model.registration_form.registratiom_form_page import Registration
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Open registation form')
@allure.link('https://nexign.com/ru', name='Testing')
def test_open_registration_form():
    registration = Registration()

    with allure.step('Открытие страницы'):
        registration.open()

    with allure.step('Открытие формы регистрации'):
        registration.open_registration_form()

    with allure.step('Проверка обязательных полей'):
        registration.should_required_items()
