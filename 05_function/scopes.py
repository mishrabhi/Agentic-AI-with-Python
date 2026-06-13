# Scope

# Scopes and Name resolution
# Local - inside a function
# Enclosing from outer function if nested
# global - Top level script
# Built in

def serve_chai():
    chai_type = "Masala"  #local scope
    print(f"Inside function {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"Outside function: {chai_type}")

def chai_counter():
    chai_order = 'lemon' #Enclosing scope
    def print_order():
        chai_order = 'Ginger'
        print("Inner:", chai_order)
    print_order()
    print("Outer:", chai_order)


chai_order = "Tulsi" #Global scope
chai_counter()
print(f"Global: ", chai_order)