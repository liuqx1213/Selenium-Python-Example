import allure
import pytest
from _pytest.fixtures import FixtureRequest
from assertpy import assert_that

from tests.test_base import BaseTest


@allure.epic("Security")
@allure.story("Forgot Password Feature's Functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.security
class TestForgotPassword(BaseTest):
    @allure.description("Forgot password with a valid email address")
    @allure.title("Forgot Password with valid email test")
    def test_valid_email(self, json_data: dict, request: FixtureRequest):
        email = request.config.getini("username")
        self.about_page.click_login_link()
        self.login_page.click_forgot_password()
        self.forget_password_page.send_password_reset_link(email)
        expected_success_message = json_data["forgot_password"]["success_message"]
        assert_that(expected_success_message).is_equal_to(
            self.forget_password_page.get_success_message()
        )

    @allure.description("Forgot Password with invalid email address")
    @allure.title("Forgot Password with invalid email test")
    def test_invalid_email(self, excel_reader, json_data: dict):
        emails = excel_reader.read_from_excel("Emails")
        self.about_page.click_login_link()
        self.login_page.click_forgot_password()
        self.forget_password_page.send_password_reset_link(emails[0])
        expected_error_message = json_data["forgot_password"]["error_message"]
        assert_that(expected_error_message).is_equal_to(
            self.forget_password_page.get_invalid_email_message()
        )

    @allure.description("Exception catching")
    @allure.title("Exception test")
    def test_expected_exception_on_page_title(self):
        self.about_page.click_login_link()
        self.login_page.click_forgot_password()
        with pytest.raises(AssertionError) as e:
            assert self.forget_password_page.get_page_title() == "something else"
        assert "AssertionError" in str(e)
