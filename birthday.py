import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    prob = 1.0
    for i in range(people):
        prob = prob * (365 - i) / 365

    return 1.0 - prob

def simulate_birthday(people, trials):
    coincidences = 0
    for _ in range(trials):
        birthdays = []
        for _ in range(people):
            birthdays.append(random.randint(1, 365))

        if len(set(birthdays)) < people:
            coincidences = coincidences + 1
    return coincidences / trials

if __name__ == "__main__":
    for p in range(5, 61, 5):
        exact = birthday_probability(p)
        sim = simulate_birthday(p, 100000)
        print(p, exact, sim)

        for p in range(1, 100):
            if birthday_probability(p) > 0.5:
                print(p)
                break

