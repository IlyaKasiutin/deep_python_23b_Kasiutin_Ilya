import json
import time
import os

import cjson


start = time.time()
for file in os.listdir('jsons/'):
    with open('jsons/' + file, "r") as fp:
        sample = json.load(fp)
        res = json.dumps(sample)
        json.loads(res)
end = time.time()

print("Execution time for json: ", end - start)


start = time.time()
for file in os.listdir('jsons/'):
    with open('jsons/' + file, "r") as fp:
        sample = json.load(fp)
        res = cjson.dumps(sample)
        cjson.loads(res)
end = time.time()
print("Execution time for cjson: ", end - start)
