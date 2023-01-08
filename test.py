from search_page import SearchPageHelper
from ya_pages import SearchHelper


def test_search(browser):
    ya_main_page = SearchHelper(browser)
    ya_search_page = SearchHelper(browser)
    ya_main_page.go_to_site()
    ya_main_page.enter_word("Hello")
    ya_main_page.click_on_search_button()
    elements = ya_search_page.check_navi_bar()
    assert "Картинка" and "Видео" in elements
