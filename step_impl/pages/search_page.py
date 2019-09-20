
from step_impl.pages.base import BasePage, Element, Section


class SearchResult(Section):
    title = Element("a.search-result-title")


class SearchPage(BasePage):
    keyword_search = Element("input[name=q]")
    search_results = SearchResult("#js-dm-live-search-results", repeated=True)
