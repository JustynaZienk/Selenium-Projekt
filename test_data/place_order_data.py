from faker import Faker
import csv


def get_csv_data(filename):
    rows = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        # Pomiń pierwszy wiersz
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows


class PlaceOrderDataGenerator:
    """
    Generate data from Faker
    """
    def __init__(self):
        self.faker = Faker()
        self.NAME= self.faker.name()
        self.CREDIT_CARD= self.faker.credit_card()