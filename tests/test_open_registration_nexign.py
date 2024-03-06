from qa_guru_python_15.model.pages.registration_page import RegistrationPage
import allure
from allure_commons.types import Severity


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Open registation form')
@allure.link('https://nexign.com/ru', name='Testing')
def test_open_registration_form():
    registration = RegistrationPage()

    registration.open()

    registration.open_registration_form()
    registration.should_required_items()
