class Hero:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._xp = 0
        self._max_hp = 100
        self._hp = 100

    @property
    def level(self):
        return self._level

    @property
    def xp(self):
        return self._xp

    @property
    def hp(self):
        return self._hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def is_alive(self):
        return self._hp > 0

    def gain_xp(self, points):
        if not self.is_alive:
            raise ValueError()
        if points <= 0:
            raise ValueError()

        self._xp += points
        leveled_up = False

        while self._xp >= self._level * 100:
            self._xp -= self._level * 100
            self._level += 1
            self._max_hp += 20
            leveled_up = True

        if leveled_up:
            self._hp = self._max_hp

    def take_damage(self, amount):
        if amount <= 0:
            raise ValueError()
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        if not self.is_alive:
            raise ValueError()
        if amount <= 0:
            raise ValueError()
        self._hp = min(self._max_hp, self._hp + amount)

    def attack(self, other):
        if not isinstance(other, Hero):
            return NotImplemented
        if not self.is_alive:
            raise ValueError()
        if not other.is_alive:
            raise ValueError()
        if self is other:
            raise ValueError()

        damage = 10 * self._level
        other.take_damage(damage)

        if not other.is_alive:
            reward_xp = 50 * other.level
            self.gain_xp(reward_xp)

    def __repr__(self):
        return f"Hero('{self._name}', level={self._level}, xp={self._xp}, hp={self._hp}/{self._max_hp})"
