from faker import Faker


class RegistrationDataGenerator:
    """
    Generate data from Faker
    """
    def __init__(self):
        self.faker = Faker()
        self.USERNAME = self.faker.user_name()
        self.PASSWORD = self.faker.password()
