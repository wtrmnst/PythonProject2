class Date:
    DAYS_IN_MONTHS = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def __init__(self, day: int, month: int, year: int):
        if not self._is_valid(day, month, year):
            raise ValueError()
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @staticmethod
    def _is_leap(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def _is_valid(cls, day: int, month: int, year: int) -> bool:
        if month < 1 or month > 12:
            return False
        max_days = cls.DAYS_IN_MONTHS[month]
        if month == 2 and cls._is_leap(year):
            max_days = 29
        if day < 1 or day > max_days:
            return False
        return True

    def _to_days(self) -> int:
        y = self._year - 1
        days = y * 365 + y // 4 - y // 100 + y // 400
        for m in range(1, self._month):
            if m == 2 and self._is_leap(self._year):
                days += 29
            else:
                days += self.DAYS_IN_MONTHS[m]
        days += self._day
        return days

    @classmethod
    def _from_days(cls, total_days: int):
        year = total_days // 366
        while True:
            y = year - 1
            days_before_year = y * 365 + y // 4 - y // 100 + y // 400
            days_before_next_year = year * 365 + year // 4 - year // 100 + year // 400
            if days_before_year < total_days <= days_before_next_year:
                break
            year += 1

        y = year - 1
        days_left = total_days - (y * 365 + y // 4 - y // 100 + y // 400)
        
        month = 1
        while True:
            days_in_this_month = 29 if month == 2 and cls._is_leap(year) else cls.DAYS_IN_MONTHS[month]
            if days_left <= days_in_this_month:
                break
            days_left -= days_in_this_month
            month += 1
            
        return cls(days_left, month, year)

    def __add__(self, days_to_add: int):
        if not isinstance(days_to_add, int):
            return NotImplemented
        return Date._from_days(self._to_days() + days_to_add)

    def __sub__(self, other):
        if isinstance(other, Date):
            return self._to_days() - other._to_days()
        return NotImplemented

    def __eq__(self, other) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self._day == other._day and self._month == other._month and self._year == other._year

    def __lt__(self, other) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        if self._year != other._year:
            return self._year < other._year
        if self._month != other._month:
            return self._month < other._month
        return self._day < other._day

    def __repr__(self) -> str:
        return f"Date({self._day}, {self._month}, {self._year})"

    def __str__(self) -> str:
        return f"{self._day:02d}.{self._month:02d}.{self._year}"
