import random

def get_numbers_ticket(min_number, max_number, quantity_numbers):
    s = set()
    if min_number >= 1:
        if max_number <= 1000:
            while len(s) < quantity_numbers:
                s.add(random.randint(min_number, max_number))
    s = sorted(s)
    return s
  
min = 3
max = 100000
quantity = 5
ss = get_numbers_ticket(min, max, quantity)
print(ss)
