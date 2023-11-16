"""Memory profiling for task №1"""
from memory_profiler import profile
from task1.person import Person
from task1.slots_person import SlotsPerson
from task1.weak_person import WeakPerson


@profile
def run_person(n_iters):
    persons = [Person(30, 180, 'teacher') for i in range(n_iters)]
    for person in persons:
        person.age = 40


@profile
def run_slots_person(n_iters):
    persons = [SlotsPerson(30, 180, 'teacher') for i in range(n_iters)]
    for person in persons:
        person.age = 40


@profile
def run_weak_person(n_iters):
    persons = [WeakPerson(30, 180, 'teacher') for i in range(n_iters)]
    for person in persons:
        person.age = 40


if __name__ == "__main__":
    N = 100_000
    print(f"number of objects: {N}")
    run_person(N)
    run_slots_person(N)
    run_weak_person(N)
