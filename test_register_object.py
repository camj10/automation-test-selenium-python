from selenium import webdriver
from pages.actions.register_actions import RegisterActions


def test_fill_form():
    driver = webdriver.Chrome()
    register = RegisterActions(driver)
    register.load("https://www.testertestarudo.com/sandbox-para-pruebas-automatizadas")

    register.type_user("Testname")
    register.type_email("email@testertestarudo.com")
    register.type_age("20")
    register.click_to_register()
    register.user_is_logged()