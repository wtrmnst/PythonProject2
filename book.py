class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError("Число страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self._available = True
        self._last_read_pages = 0

    @property
    def is_available(self):
        return self._available

    @property
    def last_read_pages(self):
        return self._last_read_pages

    def borrow(self):
        if not self._available:
            raise ValueError("Книга уже выдана.")
        self._available = False

    def give_back(self, pages_read):
        if self._available:
            raise ValueError("Книга уже на полке.")
        if not (0 <= pages_read <= self.pages):
            raise ValueError(f"В книге всего {self.pages} страниц.")
        self._last_read_pages = pages_read
        self._available = True

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})"
        
            
