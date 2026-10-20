class Book:
    def __init__(self, title, author, isbn, year, pages):
        if pages <= 0:
            raise ValueError ("Число страниц должно быть положительным.")
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.pages = pages
        self.is_available = True
        self.last_read_pages = 0
        
    @property 
    def is_available(self):
        return self.is_available
    
    @property
    def last_read_pages(self):
        return self.last_read_pages
        
    def borrow(self):
        if not self.is_available:
            raise ErrorValue("Книга уже выдана.")
        self.is_available = False
        
    def give_back(self, pages_read):
        if self.is_available:
            raise ValueError ("Книга уже на полке.")
        if not (0 <= pages_read <= self.pages):
            raise ValueError("В книге всего {self.pages} страниц.")
            
        self.last_read_pages = pages_read
        self.is_available = True
        
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return False
    
    def __lt__(self, other):
        return self.year < other.year
        
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}', {self.year}, {self.pages})
        
            