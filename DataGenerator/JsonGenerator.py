import json
from faker import Faker


class JsonGenerator:
    def __init__(self):
        self.fake = Faker(['en_US'])

    def generate_profile(self):
        profile = self.fake.profile()
        profile['birthdate'] = profile['birthdate'].strftime('%Y-%m-%d %H:%M:%S')
        profile['current_location'] = [int(x) for x in profile['current_location']]
        return profile

    def generate(self, size):
        data = self.fake.json(
            data_columns={
                    'name': 'name',
                    'address': 'address',
                    'email': 'email',
                    'job': 'job',
                    'company': 'company',
                    'phone': 'phone_number'
            },
            num_rows=size,
        )
        return data


if __name__ == '__main__':
    generator = JsonGenerator()
    generator.generate(10)
