class Money:
    def __init__(self, rubles, kopecks=0):
        if rubles < 0 or kopecks < 0:
            raise ValueError()
        total_kopecks = rubles * 100 + kopecks
        self._rubles = total_kopecks // 100
        self._kopecks = total_kopecks % 100

    @property
    def rubles(self):
        return self._rubles

    @property
    def kopecks(self):
        return self._kopecks

    def _to_kopecks(self):
        return self._rubles * 100 + self._kopecks

    def __add__(self, other):
        if isinstance(other, Money):
            total = self._to_kopecks() + other._to_kopecks()
            return Money(0, total)
        return NotImplemented

    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Money):
            total = self._to_kopecks() - other._to_kopecks()
            if total < 0:
                raise ValueError()
            return Money(0, total)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, float):
            raise TypeError()
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise ValueError()
        return Money(0, self._to_kopecks() * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def split(self, n):
        if not isinstance(n, int) or n < 1:
            raise ValueError()
        total = self._to_kopecks()
        base = total // n
        remainder = total % n
        parts = []
        for i in range(n):
            current_kopecks = base + (1 if i < remainder else 0)
            parts.append(Money(0, current_kopecks))
        return parts

    def __eq__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() == other._to_kopecks()
        return False

    def __lt__(self, other):
        if isinstance(other, Money):
            return self._to_kopecks() < other._to_kopecks()
        return NotImplemented

    def __repr__(self):
        return f"Money({self._rubles}, {self._kopecks})"

    def __str__(self):
        return f"{self._rubles} руб. {self._kopecks:02d} коп."
