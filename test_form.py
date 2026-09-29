from selenium.webdriver.common.by import By


def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text


def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "Your password is invalid!" in driver.find_element(By.ID, "flash").text