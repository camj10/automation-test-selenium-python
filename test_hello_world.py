# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest

# @pytest.fixture

# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


# def test_visit_testarudo(driver):
#     driver.get("https://www.testertestarudo.com")
#     # driver.refresh()
#     # driver.implicitly_wait(10)
#     assert "Tester Testarudo" in driver.title

# # def test_visit_google(driver):
# #     driver.get("https://www.google.com")
# #     assert "google" in driver.title

# def test_visit_google(driver):
#     driver.get("https://www.google.com")
#     assert "google" in driver.title.lower()

# def test_visit_sandbox_and_explore_elements(driver):
#     driver.get("https://www.testertestarudo.com/sandbox-para-pruebas-automatizadas")
#     driver.find_element(By.XPATH, "//input [@name='name']")
#     driver.find_element(By.CSS_SELECTOR, "input#name")
#     assert "Sandbox para Pruebas Automatizadas | Tester Testarudo" in driver.title

