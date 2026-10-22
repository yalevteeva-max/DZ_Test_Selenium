import allure
from selenium.webdriver.common.by import By

@allure.title("Успешный вход с валидными данными")
@allure.description("Успешный вход с валидными данными")
def test_successful_login(driver):
    with allure.step("Открыть страницу логина"):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step("Вводим логин и пароль"):
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    with allure.step("Нажимаем кнопку Войти"):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    with allure.step("Проверяем сообщение об успешном входе"):
        assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text


@allure.title("Неуспешный вход с неверным паролем")
@allure.description("Проверяем, что при вводе неверного пароля появляется сообщение об ошибке")
def test_unsuccessful_login(driver):
    with allure.step("Открывается страница логина"):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step("Вводится неверный пароль"):
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("WrongPassword")

    with allure.step("Нажимаем кнопку Войти"):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    with allure.step("Проверяем сообщение об ошибке"):
        assert "Your password is invalid!" in driver.find_element(By.ID, "flash").text