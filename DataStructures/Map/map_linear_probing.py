from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
def new_map(num_elements, load_factor, prime=109345121):
    c = num_elements/load_factor
    new_map = {"prime": prime,
               "capacity": mf.next_prime(c),
               "scale": 1,
               "shift": 0,
               "table": table(num_elements),
               "current_factor": 0,
               "limit_factor": load_factor,
               "size": 0
               }
    return new_map


def table(num_elements):
    table = al.new_list()
    for i in range(num_elements):
        element=me.new_map_entry(None, None)
        al.add_last(table, element)
    return table

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)
    find_slot(my_map, key, hash_value)
    
def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail
    
def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1