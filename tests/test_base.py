from typing import Union

from selenium.webdriver import Chrome, Firefox, Edge

from pages.about_page import AboutPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.project_edit_page import ProjectEditPage
from pages.project_type_page import ProjectTypePage
from pages.projects_page import ProjectsPage
from pages.templates_page import TemplatesPage


class BaseTest:
    driver: Union[Chrome, Firefox, Edge]
    about_page: AboutPage
    login_page: LoginPage
    projects_page: ProjectsPage
    forget_password_page: ForgotPasswordPage
    templates_page: TemplatesPage
    project_type_page: ProjectTypePage
    project_edit_page: ProjectEditPage
