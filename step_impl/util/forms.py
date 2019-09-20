
def fill_in_multipage_form(page, responses):
    def walk(t):
        if "action" in t:
            # it's a leaf
            t = t.copy()
            # do the action
            getattr(page, t.pop("action"))(**t)
            page.click_button("Save and continue")
        else:
            # it's a tree
            for link, ts in t.items():
                page.click_link(link)
                walk(ts)

    walk(responses)
