from memory_profiler import profile
from task1.person import Person
from task1.slots_person import SlotsPerson
from task1.weak_person import WeakPerson


@profile
def run_person(n):
    persons = [Person(30, 180, 'teacher') for i in range(n)]
    for person in persons:
        person.age = 40


@profile
def run_slots_person(n):
    persons = [SlotsPerson(30, 180, 'teacher') for i in range(n)]
    for person in persons:
        person.age = 40


@profile
def run_weak_person(n):
    persons = [WeakPerson(30, 180, 'teacher') for i in range(n)]
    for person in persons:
        person.age = 40


if __name__ == "__main__":
    n = 100_000
    print(f"number of objects: {n}")
    run_person(n)
    run_slots_person(n)
    run_weak_person(n)
