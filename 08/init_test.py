import time
from person import Person
from slots_person import SlotsPerson
from weak_person import WeakPerson


N = 1_000_000
print(f"Number of objects: {N}")

start = time.time()
for i in range(N):
    Person(30, 180, 'teacher')
end = time.time()

print(f"Init time for Person: {end - start:.4f}")


start = time.time()
for i in range(N):
    SlotsPerson(30, 180, 'teacher')
end = time.time()

print(f"Init time for SlotsPerson: {end - start:.4f}")


start = time.time()
for i in range(N):
    WeakPerson(30, 180, 'teacher')
end = time.time()

print(f"Init time for WeakPerson: {end - start:.4f}")

