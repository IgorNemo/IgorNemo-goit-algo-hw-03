import random

def get_numbers_ticket(min_number, max_number, quantity_numbers):
    
    s = set()
    while len(s) < quantity_numbers:
        s.add(random.randint(min_number, max_number))
    s = sorted(s)
    return s
  
min = 1
max = 200
quantity = 5
ss = get_numbers_ticket(min, max, quantity)
print(ss)
