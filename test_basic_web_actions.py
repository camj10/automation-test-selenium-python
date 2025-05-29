# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pytest

# @pytest.fixture

# def driver():
#     chrome_options = Options()
#     # # chrome_options.add_argument("--headless")
#     # chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=chrome_options)
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
