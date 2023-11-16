from person import Person
from slots_person import SlotsPerson
from weak_person import WeakPerson
import time


N = 100_000
print(f"Number of objects: {N}")

# Person
persons = [Person(30, 180, 'teacher') for i in range(N)]

start = time.time()
for person in persons:
    person.age = 40
end = time.time()

print(f"Change time for Person: {end - start:.4f}")


# SlotsPerson
persons = [SlotsPerson(30, 180, 'teacher') for i in range(N)]

start = time.time()
for person in persons:
    person.age = 40
end = time.time()

print(f"Change time for SlotsPerson: {end - start:.4f}")


# WeakPerson
persons = [WeakPerson(30, 180, 'teacher') for i in range(N)]

start = time.time()
for person in persons:
    person.age = 40
end = time.time()

print(f"Change time for WeakPerson: {end - start:.4f}")
