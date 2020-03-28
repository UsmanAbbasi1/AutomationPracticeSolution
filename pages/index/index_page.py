from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class IndexPage(BasePage):
    def enter_search_text(self, text):
        search_bar = self.driver.find_element_by_id('search_query_top')
        search_bar.clear()
        search_bar.send_keys(text)

    def click_search_button(self):
        search_bar = self.driver.find_element_by_css_selector('form[id="searchbox"]>button[name="submit_search"]')
        search_bar.click()

    def click_item_from_search_result(self, index=0):
        item = self.get_search_result_items_list()[index]
        item.find_element_by_css_selector('a[class="products-block-image content_img clearfix"]').click()

    def click_login_link(self):
        self.driver.find_element_by_link_text('Sign in').click()

    def click_create_account_and_enter_email_address(self, email_address):
        self.driver.find_element_by_id('email_create').send_keys(email_address)
        self.driver.find_element_by_id('SubmitCreate').click()

    def fill_sign_up_form(self):
        self._fill_sign_up_personal_info()
        self._fill_sign_up_address_info()

    def search_item(self, text):
        self.enter_search_text(text)
        self.click_search_button()

    def get_search_result_items_list(self):
        items_list = self.driver.find_elements_by_css_selector(
            'div[id="best-sellers_block_right"] ul[class="block_content products-block"]>li[class="clearfix"]')
        return items_list

    @property
    def sign_out_button(self):
        return self.driver.find_element_by_link_text('Sign out')

    @property
    def customer_account_button(self):
        return self.driver.find_element_by_css_selector('a[title="View my customer account"]')

    def _fill_sign_up_personal_info(self):
        self.driver.find_element_by_id('id_gender1').click()
        self.driver.find_element_by_id('customer_firstname').send_keys('usman')
        self.driver.find_element_by_id('customer_lastname').send_keys('abasi')
        self.driver.find_element_by_id('passwd').send_keys('1234567')

        dob_day_dropdown = Select(self.driver.find_element_by_css_selector('div[id="uniform-days"]>select[id="days"]'))
        dob_day_dropdown.select_by_value('1')

        dob_month_dropdown = Select(
            self.driver.find_element_by_css_selector('div[id="uniform-months"]>select[id="months"]'))
        dob_month_dropdown.select_by_value('3')

        dob_year_dropdown = Select(
            self.driver.find_element_by_css_selector('div[id="uniform-years"]>select[id="years"]'))
        dob_year_dropdown.select_by_value('1993')

    def _fill_sign_up_address_info(self):
        # Frontend automatically fills the name fields when we enter this info in "Personal Info" section
        # self.driver.find_element_by_id('firstname').send_keys('usman')
        # self.driver.find_element_by_id('lastname').send_keys('abasi')

        self.driver.find_element_by_id('address1').send_keys('H#111 Area1')
        Select(self.driver.find_element_by_id('id_country')).select_by_value('21')

        self.driver.find_element_by_id('city').send_keys('ABC')
        Select(self.driver.find_element_by_id('id_state')).select_by_visible_text('Maryland')

        self.driver.find_element_by_id('postcode').send_keys('54000')
        self.driver.find_element_by_id('phone_mobile').send_keys('+12 345 678')
        self.driver.find_element_by_css_selector('input[name="alias"][id="alias"]').send_keys('H#111 Area1')

        self.driver.find_element_by_id('submitAccount').click()
