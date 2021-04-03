# agrega mayor funcionlidad
# funcion que crea funciones
# por lo menos deben hacer 3 funciones // my_decorator / func / wrapper

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()
print("codigo ejecutando")

#---------------------
print("********************************")

def decorador(is_valid = True):
    def _decorador(func):

        def before_action():
            print("Open DB")
        
        def after_action():
            print("Close DB")
        
        def nueva_funcion(*args, **kwargs):
            if is_valid:
                before_action()

            resultado = func(*args, **kwargs)
            
            after_action()
            return resultado
        return nueva_funcion
    return _decorador

@decorador
def suma(v1,v2):
    return v1+v2

resultado = suma(False)
print("codigo ejecutando")
