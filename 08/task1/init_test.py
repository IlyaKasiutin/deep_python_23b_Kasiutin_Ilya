"""Init timing"""
import time
from person import Person
from slots_person import SlotsPerson
from weak_person import WeakPerson


N = 100_000
print(f"Number of objects: {N}")


start = time.time()
persons = [Person(30, 180, 'teacher') for i in range(N)]
end = time.time()

print(f"Init time for Person: {end - start:.4f}")


start = time.time()
persons = [SlotsPerson(30, 180, 'teacher') for i in range(N)]
end = time.time()

print(f"Init time for SlotsPerson: {end - start:.4f}")


start = time.time()
persons = [WeakPerson(30, 180, 'teacher') for i in range(N)]
end = time.time()

print(f"Init time for WeakPerson: {end - start:.4f}")
