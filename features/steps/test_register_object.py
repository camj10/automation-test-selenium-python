from pytest_bdd import given, when, then, scenario
from selenium import webdriver
from pages.actions.register_actions import RegisterActions
import allure 

@scenario("register.feature","Register User with valid credentials")
@allure.suite("Landing Page")
@allure.title("Registration from User")
def test_register_user():
    pass

@given("the User goes to the Website")
def step_open_web(driver):
    register = RegisterActions(driver)
    register.load("https://www.testertestarudo.com/sandbox-para-pruebas-automatizadas")

@when("the User enters with valid credentials")
def step_register_user(driver) -> None:
    register = RegisterActions(driver)
    register.type_user("Testname")
    register.type_email("email@testertestarudo.com")
    register.type_age("20")
    register.click_to_register()

@then("the User is registered succesfully")
def step_user_is_registered_succesfully(driver) -> None:
    register = RegisterActions(driver)
    register.user_is_logged()
