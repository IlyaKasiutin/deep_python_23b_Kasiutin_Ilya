import random
import json
from faker import Faker


class LoginData:

    def __init__(self):
        fake = Faker()
        self.password = "password@123"
        self.email = fake.email()
        self.username = fake.first_name()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.phone = random.randint(9000000000, 9999999999)
        self.city = fake.city().replace(' ', '_')
        self.about = "This_is_a_sample_text_about"

    def get_json(self):
        p = {
            "password": self.password,
            "email": self.email,
            "username": self.first_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "city": self.city,
            "about": self.about
        }
        return p


def generator():
    logindata = LoginData()
    json_dict = logindata.get_json()
    return json_dict

def save_dict_as_json(js_dict, filename):
    with open(filename, "w") as fp:
        json.dump(js_dict, fp)


def main():
    n_files = 20000
    for i in range(n_files):
        filepath = "jsons/test_json_" + str(i) + ".json"
        json_dict = generator()
        save_dict_as_json(json_dict, filepath)

if __name__ == "__main__":
    main()