from pages.index.index_page import IndexPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):
    def setUp(self):
        super().setUp()
        self.index_page = IndexPage(self.driver)
        self.driver.get(self.index_page.base_url)

    def test_search_returns_data(self):
        self.index_page.search_item('shirts')
        search_result_items_list = self.index_page.get_search_result_items_list()
        self.assertGreater(len(search_result_items_list), 0)

    def test_item_details(self):
        self.index_page.search_item('shirts')
        self.index_page.click_item_from_search_result()
        self.assertIsNotNone(self.driver.find_element_by_id('product_reference'))
        self.assertIsNotNone(self.driver.find_element_by_id('product_condition'))
        self.assertIsNotNone(self.driver.find_element_by_id('short_description_block'))
