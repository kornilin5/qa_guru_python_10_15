## Проект UI автотестов Nexign


<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="vscode" src="images/vscode.png"></code>
  <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/jira.png"></code>
  <code><img width="5%" title="Postman" src="images/postman.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>


<!-- Тест кейсы -->

### Что проверяем
* Открытие пункта "услуги" из главной панели 
* Открытие пункта "о компании" из главной панели 
* Открытие пункта "store" из главной панели 
* Открытие пункта "Контакты" из главной панели 



<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.png"> Запуск проекта в Jenkins

### [Задача в jenkins](https://jenkins.autotests.cloud/job/010-kornilin5-home_work_15/)

##### При нажатии на "Build with parameters" появится выбор для стенда, послего чего начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](images/jenkins_work.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report

``##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/allure_suites.png)

##### Видео прохождение теста
![This is an image](images/tests_ui.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/4104/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/jira_project.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/tg_bot.png)
