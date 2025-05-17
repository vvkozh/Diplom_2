from faker import Faker
import random

faker = Faker()

def generate_email():
    return faker.email()

def generate_password():
    return faker.password()

def generate_name():
    return faker.first_name()

def generate_list_ingredients(list_size, list_ingredients):
    ingredients = random.sample(list_ingredients, list_size)
    return ingredients