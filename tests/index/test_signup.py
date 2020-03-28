from pages.index.index_page import IndexPage
from tests.base_test import BaseTest


class TestSignup(BaseTest):
    def setUp(self):
        super().setUp()
        self.index_page = IndexPage(self.driver)
        self.driver.get(self.index_page.base_url)

    def test_signup_successfully(self):
        self.index_page.click_login_link()
        # Make sure to give new email_address every time when signing up
        self.index_page.click_create_account_and_enter_email_address('testuser+123@gmail.com')
        self.index_page.fill_sign_up_form()

        self.assertIsNotNone(self.index_page.sign_out_button)
        self.assertIsNotNone(self.index_page.customer_account_button)
