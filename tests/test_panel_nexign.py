import allure
from allure_commons.types import Severity
from qa_guru_python_15.model.pages.panel_page import PanelPage


@allure.tag('nexign')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kornilin5')
@allure.feature('Panel information')
@allure.link('https://nexign.com/ru', name='Testing')
def test_panel():
    main_panel = PanelPage()

    main_panel.open()

    main_panel.should_contacts()
    main_panel.should_services()
    main_panel.should_about_company()
    main_panel.should_store()
