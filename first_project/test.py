#import random
from faker import Faker

fakegen = Faker()

for i in range(5):
    print(fakegen.first_name(), " ", fakegen.last_name())