class Book:
    def __init__(self, title, total_pages):
        self.title = title
        # Use an internal variable to bypass setter print triggers during initialization
        self._page_count = total_pages

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._page_count = value
        # Triggers when the test alters the property later
        if not isinstance(value, int):
            print("page_count must be an integer")

    def turn_page(self):
        # Must print directly to stdout instead of returning a string
        print("Flipping the page...wow, you read fast!")
