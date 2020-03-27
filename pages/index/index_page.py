from pages.base_page import BasePage


class IndexPage(BasePage):
    def enter_search_text(self, text):
        search_bar = self.driver.find_element_by_id('search_query_top')
        search_bar.clear()
        search_bar.send_keys(text)

    def click_search_button(self):
        search_bar = self.driver.find_element_by_css_selector('form[id="searchbox"]>button[name="submit_search"]')
        search_bar.click()

    def search_item(self, text):
        self.enter_search_text(text)
        self.click_search_button()

    def click_item_from_search_result(self, index=0):
        item = self.get_search_result_items_list()[index]
        item.find_element_by_css_selector('a[class="products-block-image content_img clearfix"]').click()

    def get_search_result_items_list(self):
        items_list = self.driver.find_elements_by_css_selector(
            'div[id="best-sellers_block_right"] ul[class="block_content products-block"]>li[class="clearfix"]')
        return items_list
