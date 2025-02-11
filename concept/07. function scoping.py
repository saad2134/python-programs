def outer_function():
    outer_var = "I am in the outer function"
    
    def inner_function():
        inner_var = "I am in the inner function"
        print(inner_var)  # Accessible inside inner function
        print(outer_var)  # Accessible inside inner function (enclosing scope)
    
    inner_function()
    # print(inner_var)  # This would cause an error because inner_var is local to inner_function

outer_function()

# Global Scope
global_var = "I am a global variable"

def global_scope_function():
    print(global_var)  # Accessible inside the function

global_scope_function()

# Local Scope
def local_scope_function():
    local_var = "I am a local variable"
    print(local_var)  # Accessible inside the function

local_scope_function()
# print(local_var)  # This would cause an error because local_var is local to local_scope_function
