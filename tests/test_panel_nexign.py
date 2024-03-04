import allure
from allure_commons.types import Severity
from qa_guru_python_15.model.main_panel.MainPanelTest import PanelTest


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Contacts')
@allure.story('contacts information')
@allure.link('https://nexign.com/ru', name='Testing')
def test_panel():
    main_panel = PanelTest()

    with allure.step('Открытие страницы'):
        main_panel.open()

    with allure.step('Проверка раздела контактов'):
        main_panel.should_contacts()

    with allure.step('Проверка раздела услуг'):
        main_panel.should_services()

    with allure.step('Проверка раздела о компании'):
        main_panel.should_about_company()

    with allure.step('Проверка раздела store'):
        main_panel.should_store()
