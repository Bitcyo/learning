#permite cojer una funcion o metodo para poder modificarlo levemente sin dañar su ejecucion 
#normal

def decorator(function):
    def mod_function():
        print("call bofore function")
        function()
        print("call after function")
        
    return mod_function

# def salutation():
#     print("i'm dead")
    
# sal_function = decorator(salutation)

# sal_function()

@decorator
def salutation():
    print("i just want be happy,no more")
salutation()