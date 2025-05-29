# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest

# @pytest.fixture

# def driver():
#     driver = webdriver.Chrome()
#     driver.get("https://www.testertestarudo.com/sandbox-para-pruebas-automatizadas")
#     yield driver
#     assert "Sandbox para Pruebas Automatizadas | Tester Testarudo" in driver.title
#     driver.quit()

# def test_click_element(driver):
#     alert_button = driver.find_element(By.ID, "alertButton")
#     alert_button.click()
#     alert = driver.switch_to.alert
#     alert.accept()


# def test_fill_form(driver):
#     name_input = driver.find_element(By.XPATH, "//input [@name='name']")
#     name_input.send_keys("Testname")
#     email_input = driver.find_element(By.XPATH, "//input [@name='email']")
#     email_input.send_keys("email@testertestarudo.com")
#     age_input = driver.find_element(By.ID, "ageSlider")
#     age_input.send_keys("20")
#     submit = driver.find_element(By.XPATH, "//input [@type='submit']")
#     submit.click()
