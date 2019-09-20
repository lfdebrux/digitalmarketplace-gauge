
import functools

from capybara.dsl import DSLMixin, page


class PageMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        has_methods = {}
        for name, attr in clsdict.items():
            if hasattr(attr, "__has__"):
                has_methods[f"has_{name}"] = functools.partialmethod(attr.__has__)
        clsdict.update(has_methods)
        return super().__new__(cls, clsname, bases, clsdict)


class Element:
    def __init__(self, *args, **kwargs):
        self.locator = (args, kwargs)

    def __get__(self, page, pagetype):
        return page.find(*self.locator[0], **self.locator[1])

    def __has__(self, page):
        return page.assert_selector(*self.locator[0], **self.locator[1])


class Section(DSLMixin, metaclass=PageMeta):
    def __init__(self, *args, **kwargs):
        self.locator = (args, kwargs)

    def __get__(self, page, pagetype):
        with page.scope(*self.locator[0], **self.locator[1]):
            return self


class BasePage(DSLMixin, metaclass=PageMeta):
    URL = ""

    def visit(self, *args, **kwargs):
        page.visit(self.URL)
