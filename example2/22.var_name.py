from modulo_calculadora import __name__ as __name__calculadora__     

print(__name__) # modulo principal q ejecuto es decir 22.var_name
print(__name__calculadora__) #modulo principal de modulo_calculadora

if __name__ == '__main__': # para saber q es el principal
    print("es el principal")